"""Camada RAW: extracao de series economicas publicas do Banco Central do Brasil (SGS)."""
import json
import logging
from datetime import datetime
from pathlib import Path

import requests

from config import BCB_API_URL, SERIES_BCB, RAW_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extrair_serie(nome: str, codigo: int) -> Path:
    """Baixa uma serie do SGS/BCB e salva o JSON bruto na camada raw."""
    url = BCB_API_URL.format(codigo=codigo) + "?formato=json"
    logger.info("Extraindo serie '%s' (codigo %s) de %s", nome, codigo, url)

    resposta = requests.get(url, timeout=30)
    resposta.raise_for_status()
    dados = resposta.json()

    data_execucao = datetime.now().strftime("%Y%m%d")
    destino = RAW_DIR / f"{nome}_{data_execucao}.json"
    destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")

    logger.info("Serie '%s' salva em %s (%d registros)", nome, destino, len(dados))
    return destino


def extrair_todas_series() -> list:
    """Extrai todas as series configuradas em SERIES_BCB."""
    arquivos = []
    for nome, codigo in SERIES_BCB.items():
        try:
            arquivos.append(extrair_serie(nome, codigo))
        except requests.RequestException as exc:
            logger.error("Falha ao extrair serie '%s': %s", nome, exc)
    return arquivos


if __name__ == "__main__":
    extrair_todas_series()
