"""Camada ANALYTICS: carga dos dados processados em um banco DuckDB para consultas SQL."""
import logging
from pathlib import Path

import duckdb

from config import PROCESSED_DIR, DUCKDB_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def carregar_para_duckdb(parquet_path: Path = None) -> None:
    """Cria/atualiza a tabela de series economicas no DuckDB a partir do parquet processado."""
    parquet_path = parquet_path or (PROCESSED_DIR / "series_economicas.parquet")

    if not parquet_path.exists():
        raise FileNotFoundError(f"Arquivo processado nao encontrado: {parquet_path}")

    conexao = duckdb.connect(str(DUCKDB_PATH))
    conexao.execute(
        """
        CREATE OR REPLACE TABLE series_economicas AS
        SELECT * FROM read_parquet(?)
        """,
        [str(parquet_path)],
    )

    total = conexao.execute("SELECT COUNT(*) FROM series_economicas").fetchone()[0]
    logger.info("Tabela 'series_economicas' carregada no DuckDB com %d linhas (%s)", total, DUCKDB_PATH)
    conexao.close()


if __name__ == "__main__":
    carregar_para_duckdb()
