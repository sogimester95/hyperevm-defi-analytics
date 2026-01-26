# HyperEVM DeFi Ecosystem Analytics (E2E Pipeline)



## 📊 Overview
This project is an End-to-End (E2E) data pipeline designed to track and analyze the Total Value Locked (TVL) and token distribution across the HyperEVM DeFi ecosystem. It ingests historical data (from 19.02.2025 to 24.01.2026) from the DefiLlama API, processes it via Python, stores it in a Snowflake Data Warehouse, and visualizes insights in Power BI.



## 🛠️ Tech Stack
- **Language:** Python 3.12
- **Data Warehouse:** Snowflake (Cloud Data Platform)
- **ETL/ELT:** Pandas, Snowflake Python Connector
- **Visualization:** Power BI Desktop
- **Data Source:** DefiLlama API

## 🏗️ Architecture
1. **Extraction:** Python script fetches time-series data for all major protocols on the Hyperliquid chain.
2. **Transformation:** Data cleaning and restructuring using Pandas (handling nested JSON responses).
3. **Loading:** Automated bulk loading into Snowflake using `write_pandas` for optimized performance.
4. **Modeling:** SQL Views in Snowflake (Silver Layer) for business logic and category classification.
5. **Analytics:** Power BI dashboard featuring WoW/MoM growth metrics and Market Concentration (HHI).

## 🚀 Key DAX Metrics Implemented
- **Time Intelligence:** Custom WoW, MoM and YoY growth measures using manual date anchoring to handle API data latency.
- **Concentration Index:** Herfindahl-Hirschman Index (HHI) implementation to measure ecosystem health.

## 📂 Project Structure
- `/data_pipeline`: Python ETL scripts and `requirements.txt`.
- `/snowflake_sql`: DDL and DML scripts for database setup.
- `/dashboard`: Power BI `.pbix` file and screenshots.
  

## 📈 Dashboard Preview
- [Main Dashboard](dashboard/dashboard_main_.png)

---
### 🔗 Live Demo & Links
- [**Dune Analytics - Hyperliquid General Dashboard**](https://dune.com/sogimester/hyperliquid-general)
- [**Dune Analytics - Hype token Advanced Metrics for Long-term Investment**](https://dune.com/sogimester/hype-advanced-metrics)
- [**LinkedIn**](https://www.linkedin.com/in/andr%C3%A1s-%C3%A1goston-9b675288/)
- [**X**](https://x.com/sogimester)

*Developed by sogimester*
