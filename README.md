# HyperEVM DeFi Ecosystem Analytics (E2E Pipeline)

## Overview
This project is an End-to-End (E2E) data pipeline designed to track and analyze Total Value Locked (TVL) and token distribution across the HyperEVM DeFi ecosystem. The system processes historical data (19.02.2025 – 24.01.2026) ingested from the DefiLlama API, utilizes Python for processing, Snowflake as the primary data warehouse, and Power BI for final visualization.

## Tech Stack
- **Language:** Python 3.12
- **Data Warehouse:** Snowflake (Cloud Data Platform)
- **ETL/ELT:** Pandas, Snowflake Python Connector
- **Visualization:** Power BI Desktop
- **Data Source:** DefiLlama API

## Architecture
1. **Extraction:** Python scripts fetch time-series data for all major protocols on the Hyperliquid chain.
2. **Transformation:** Data cleaning and restructuring via Pandas, with a focus on flattening nested JSON responses.
3. **Loading:** Automated bulk loading into Snowflake using the `write_pandas` method for optimized performance.
4. **Modeling:** SQL Views in the Snowflake Silver Layer handle business logic and category classification.
5. **Analytics:** Power BI dashboard focused on WoW/MoM growth metrics and Market Concentration (HHI).

## Key DAX Metrics Implemented
- **Time Intelligence:** Custom WoW, MoM, and YoY growth measures utilizing manual date anchoring to mitigate API data latency.
- **Concentration Index:** Implementation of the Herfindahl-Hirschman Index (HHI) to quantify ecosystem health and protocol dominance.

## Project Structure
- `/data_pipeline`: Python ETL scripts and `requirements.txt`.
- `/snowflake_sql`: DDL and DML scripts for database and view setup.
- `/dashboard`: Power BI `.pbix` file and related documentation.

## Dashboard Preview
- [Main Dashboard](dashboard/dashboard_main_.png)

---

### Live Demo & Links
- [**Dune Analytics - Hyperliquid General Dashboard**](https://dune.com/sogimester/hyperliquid-general)
- [**Dune Analytics - Hype token Advanced Metrics for Long-term Investment**](https://dune.com/sogimester/hype-advanced-metrics)
- [**LinkedIn**](https://www.linkedin.com/in/andr%C3%A1s-%C3%A1goston-9b675288/)
- [**X**](https://x.com/sogimester)

*Developed by sogimester*
