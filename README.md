# hyperliquid-defi-analytics
End-to-end data pipeline for biggest Hyperliquid protocols: Python (API) -> Snowflake -> Power BI.
# Hyperliquid DeFi Ecosystem Analytics (E2E Pipeline)



## 📊 Overview
This project is an End-to-End (E2E) data pipeline designed to track and analyze the Total Value Locked (TVL) and token distribution across the Hyperliquid L1 DeFi ecosystem. It ingests historical data (56,000+ rows) from the DefiLlama API, processes it via Python, stores it in a Snowflake Data Warehouse, and visualizes insights in Power BI.



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
- **Time Intelligence:** Custom WoW and MoM growth measures using manual date anchoring to handle API data latency.
- **Market Share %:** Dynamic protocol dominance calculation using `ALL` and `CALCULATE` context transition.
- **Concentration Index:** Herfindahl-Hirschman Index (HHI) implementation to measure ecosystem health.

## 📂 Project Structure
- `/data_pipeline`: Python ETL scripts and `requirements.txt`.
- `/snowflake_sql`: DDL and DML scripts for database setup.
- `/dashboard`: Power BI `.pbix` file and screenshots.

## 📝 Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r data_pipeline/requirements.txt`.
3. Execute `snowflake_sql/table_setup.sql` in your Snowflake worksheet.
4. Configure your `.env` file with Snowflake credentials.
5. Run the loader: `python data_pipeline/final_loader.py`.

## 📈 Dashboard Preview
- [Main Dashboard](dashboard/dashboard_main_.png)

---
### 🔗 Live Demo & Links
- [**Dune Analytics - Hyperliquid General Dashboard**](https://dune.com/sogimester/hyperliquid-general)
- [**Dune Analytics - Hype token Advanced Metrics for Long-term Investment**](https://dune.com/sogimester/hype-advanced-metrics)
- [**LinkedIn**](https://www.linkedin.com/in/andr%C3%A1s-%C3%A1goston-9b675288/)
- [**X**](https://x.com/sogimester)

*Developed by sogimester*
