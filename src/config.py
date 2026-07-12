"""Configuracoes do pipeline de dados economicos."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "raw"
PROCESSED_DIR = BASE_DIR / "processed"
ANALYTICS_DIR = BASE_DIR / "analytics"

DUCKDB_PATH = ANALYTICS_DIR / "economico.duckdb"

# Codigos de series do SGS/Banco Central do Brasil (dados publicos e abertos)
SERIES_BCB = {
      "ipca": 433,
      "selic": 432,
      "cambio_dolar": 1,
      "igpm": 189,
}

BCB_API_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"

for _dir in (RAW_DIR, PROCESSED_DIR, ANALYTICS_DIR):
      _dir.mkdir(parents=True, exist_ok=True)
  
