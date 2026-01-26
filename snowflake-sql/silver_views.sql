USE DATABASE HYPERLIQUID_DB;
USE SCHEMA DEFI_ANALYTICS;

CREATE OR REPLACE VIEW VW_DEFI_DASHBOARD AS
SELECT 
    DATE,
    PROTOCOL,
    TVL_USD,
    CASE 
        WHEN PROTOCOL IN ('hyperswap', 'hybra', 'valantis', 'felix', 'laminar') THEN 'DEX'
        WHEN PROTOCOL IN ('hyperlend', 'sentiment', 'morpho') THEN 'Lending'
        WHEN PROTOCOL IN ('hypurrfi', 'hyperpie') THEN 'Perpetual/Derivatives'
        WHEN PROTOCOL IN ('kinetiq', 'project-x', 'upshift') THEN 'Yield/Strategy'
        ELSE 'Other DeFi'
    END AS CATEGORY,
    -- Calculating daily TVL change
    TVL_USD - LAG(TVL_USD) OVER (PARTITION BY PROTOCOL ORDER BY DATE) AS DAILY_CHANGE_USD
FROM TVL_MASTER;
