-- Estrutura da camada analytics no DuckDB

CREATE TABLE IF NOT EXISTS series_economicas (
    serie            VARCHAR,
    data_referencia   DATE,
    valor             DOUBLE
);

CREATE INDEX IF NOT EXISTS idx_serie_data ON series_economicas (serie, data_referencia);
