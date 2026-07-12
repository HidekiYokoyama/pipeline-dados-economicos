"""Orquestrador do pipeline: extract -> transform -> load."""
import logging

from extract import extrair_todas_series
from transform import transformar_todos_arquivos
from load import carregar_para_duckdb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def executar_pipeline() -> None:
    logger.info("Iniciando extracao (camada raw)...")
    extrair_todas_series()

    logger.info("Iniciando transformacao (camada processed)...")
    transformar_todos_arquivos()

    logger.info("Iniciando carga no DuckDB (camada analytics)...")
    carregar_para_duckdb()

    logger.info("Pipeline concluido com sucesso.")


if __name__ == "__main__":
    executar_pipeline()
