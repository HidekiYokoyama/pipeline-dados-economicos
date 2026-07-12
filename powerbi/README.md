# Dashboard Power BI

Este diretorio contem as instrucoes para conectar o Power BI a camada analytics do pipeline.

## Como conectar

1. Execute o pipeline (python src/pipeline.py) para gerar o arquivo analytics/economico.duckdb.
2. No Power BI Desktop, use o conector ODBC ou o conector nativo do DuckDB (via extensao/community connector) apontando para o arquivo .duckdb.
3. Alternativamente, importe diretamente o arquivo processed/series_economicas.parquet usando o conector de Parquet do Power BI.
4. Monte visuais com as colunas serie, data_referencia e valor (ex: graficos de linha por serie ao longo do tempo, cards com o ultimo valor, etc.).

## Sugestoes de visuais

- Evolucao temporal da SELIC, IPCA, cambio e IGP-M.
- Comparativo de variacao percentual mensal entre indicadores.
- Tabela com os valores mais recentes de cada serie.
