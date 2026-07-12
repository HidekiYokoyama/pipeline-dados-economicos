# Pipeline de Dados Economicos

Pipeline de dados economicos construido em Python, organizado em camadas (raw, processed, analytics), com consultas SQL via DuckDB e dashboard final no Power BI.

## Visao geral

O projeto extrai series economicas publicas do Banco Central do Brasil (SGS), realiza a limpeza/padronizacao dos dados e disponibiliza os resultados para analise via SQL (DuckDB) e visualizacao no Power BI.

## Arquitetura em camadas

- raw/: dados brutos extraidos diretamente da API do Banco Central (JSON), sem nenhuma transformacao.
- processed/: dados limpos, tipados e padronizados, salvos em formato Parquet.
- analytics/: banco DuckDB (economico.duckdb) pronto para consultas SQL e para servir de fonte ao Power BI.

## Estrutura do projeto

```
pipeline-dados-economicos/
raw/                  # camada raw (dados brutos)
processed/            # camada processed (dados limpos)
analytics/            # camada analytics (DuckDB)
src/
  config.py         # configuracoes e caminhos
  extract.py        # extracao (raw)
  transform.py      # transformacao (processed)
  load.py           # carga no DuckDB (analytics)
  pipeline.py       # orquestrador do pipeline completo
sql/
  schema.sql             # definicao das tabelas
  analytics_queries.sql  # consultas de exemplo
powerbi/
  README.md         # instrucoes de conexao do Power BI
requirements.txt
README.md
```

## Como executar

1. Crie um ambiente virtual e instale as dependencias:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Execute o pipeline completo:

```
python src/pipeline.py
```

3. Consulte os dados com DuckDB (Python ou CLI):

```python
import duckdb
conexao = duckdb.connect("analytics/economico.duckdb")
conexao.sql("SELECT * FROM series_economicas LIMIT 10").show()
```

4. Conecte o Power BI conforme instrucoes em powerbi/README.md.

## Fonte de dados

Series publicas do SGS (Sistema Gerenciador de Series Temporais) do Banco Central do Brasil, acessadas via API publica: https://api.bcb.gov.br/dados/serie/bcdata.sgs.codigo/dados

## Tecnologias

Python, pandas, requests, DuckDB, SQL, Power BI.
