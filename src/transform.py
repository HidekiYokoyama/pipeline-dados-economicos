"""Camada PROCESSED: limpeza e padronizacao dos dados extraidos."""
import logging
from pathlib import Path

import pandas as pd

from config import RAW_DIR, PROCESSED_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def carregar_json_raw(caminho: Path) -> pd.DataFrame:
    """Le um arquivo JSON da camada raw e retorna um DataFrame."""
    return pd.read_json(caminho)


def padronizar_serie(df: pd.DataFrame, nome_serie: str) -> pd.DataFrame:
    """Padroniza tipos, nomes de colunas e adiciona metadados da serie."""
    df = df.rename(columns={"data": "data_referencia", "valor": "valor"})
    df["data_referencia"] = pd.to_datetime(df["data_referencia"], format="%d/%m/%Y")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["serie"] = nome_serie
    df = df.dropna(subset=["valor"]).sort_values("data_referencia")
    return df[["serie", "data_referencia", "valor"]]


def transformar_todos_arquivos() -> Path:
    """Processa todos os arquivos JSON da camada raw e consolida em um parquet unico."""
    arquivos_raw = sorted(RAW_DIR.glob("*.json"))
    if not arquivos_raw:
        logger.warning("Nenhum arquivo encontrado em %s", RAW_DIR)
        return None

    dataframes = []
    for arquivo in arquivos_raw:
        nome_serie = arquivo.stem.rsplit("_", 1)[0]
        df_bruto = carregar_json_raw(arquivo)
        dataframes.append(padronizar_serie(df_bruto, nome_serie))

    df_final = pd.concat(dataframes, ignore_index=True)
    destino = PROCESSED_DIR / "series_economicas.parquet"
    df_final.to_parquet(destino, index=False)

    logger.info("Dados processados salvos em %s (%d linhas)", destino, len(df_final))
    return destino


if __name__ == "__main__":
    transformar_todos_arquivos()
