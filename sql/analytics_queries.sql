-- Exemplos de consultas SQL executadas com DuckDB sobre a camada analytics

-- 1. Ultimo valor disponivel de cada serie
SELECT serie, data_referencia, valor
FROM series_economicas
QUALIFY ROW_NUMBER() OVER (PARTITION BY serie ORDER BY data_referencia DESC) = 1;

-- 2. Media mensal por serie
SELECT
    serie,
    date_trunc('month', data_referencia) AS mes,
    AVG(valor) AS valor_medio
FROM series_economicas
GROUP BY serie, mes
ORDER BY serie, mes;

-- 3. Variacao percentual mes a mes
SELECT
    serie,
    data_referencia,
    valor,
    (valor - LAG(valor) OVER (PARTITION BY serie ORDER BY data_referencia))
        / LAG(valor) OVER (PARTITION BY serie ORDER BY data_referencia) * 100 AS variacao_percentual
FROM series_economicas
ORDER BY serie, data_referencia;
