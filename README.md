# OrgPulse

## AI-Powered Organizational Intelligence System

OrgPulse is an AI-powered organizational intelligence system designed to identify organizational problems, discover problem categories, analyze weekly trends, detect emerging issues, and assess organizational risk.

## Key Features

- Semantic analysis of organizational reports
- Unsupervised problem clustering
- Automated problem categorization
- Weekly trend analysis
- Emerging problem detection
- Organizational risk scoring
- Interactive Streamlit dashboard

## Technology Stack

- Python
- Pandas
- Machine Learning
- NLP / Semantic Embeddings
- Unsupervised Learning
- Streamlit

## System Workflow

Organizational Reports  
→ Data Processing  
→ Semantic Analysis  
→ Clustering  
→ Problem Categorization  
→ Trend Analysis  
→ Risk Assessment  
→ Interactive Dashboard

## Project Structure

- `app.py` — Streamlit dashboard
- `OrgPulse_company_data_1000_v2.csv` — input organizational reports
- `orgpulse_processed_data.csv` — processed data
- `orgpulse_risk_analysis.csv` — organizational risk analysis
- `orgpulse_weekly_trends.csv` — weekly trend data
- `requirements.txt` — required Python libraries

## Running the Project

```bash
pip install -r requirements.txt
streamlit run app.py
Objective

The goal of OrgPulse is to transform organizational reports into structured, actionable insights that can support management and department-level decision making.
