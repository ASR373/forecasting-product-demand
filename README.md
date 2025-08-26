# 📈 Product Demand Forecasting using AWS

This project builds a **smart, end-to-end demand forecasting system** using real sales data and the AWS ecosystem.

We use a **time-series machine learning model** to predict how many products (like soda, chips, chocolate) will be sold in the future — helping stores avoid overstock or stockouts.

---

## 🧠 Real-World Use Case

Big retailers like Amazon, Walmart, and Flipkart use demand forecasting to:
- Keep the right inventory in stock
- Reduce costs by avoiding overproduction
- Improve delivery and supply chain planning
- Ensure customer satisfaction

---

## 🗺️ Project Overview

| Stage | Description |
|-------|-------------|
| 📥 **Data Upload** | Upload raw sales CSVs to Amazon S3 |
| 🧹 **ETL with Glue** | Clean and reformat the data using AWS Glue |
| 🤖 **Model Training** | Forecast future demand using Amazon Forecast or SageMaker DeepAR |
| 📊 **Visualization** | Plot results using QuickSight or Python |
| 🔁 **Automation** | Schedule monthly retraining with EventBridge |

---

## 🛠️ Tech Stack

- **Amazon S3** – store raw and processed data  
- **AWS Glue** – clean and reformat for model ingestion  
- **Amazon Forecast** – managed ML model for time series forecasting  
- **Amazon SageMaker** – custom model training with DeepAR  
- **Amazon QuickSight / matplotlib** – dashboards or plots for forecast results  
- **EventBridge** – automation for monthly retraining

---

## 🗂️ Folder Structure

.
.
.
.
.
.






---

## 📂 Dataset

**Source:** [Favorita Grocery Sales Forecasting – Kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data)  
**Includes:** store ID, product family, sales, date, promotion flag, holidays, oil prices  
**Target:** `sales` column (units sold per store and family, per day)

---

## 🔍 Problem to Solve

> "How many units of each product family will each store sell tomorrow, next week, and next month?"

We aim to build a forecast model that captures:
- **Seasonality**
- **Weekends and holidays**
- **Promotions**
- **Store-level trends**

---

## 📅 Progress Tracker

| Day | Milestone |
|-----|-----------|
| ✅ Day 1 | Uploaded raw sales data to S3 |
| ✅ Day 2 | Cleaned and reformatted data using AWS Glue job |
| ✅ Day 3 | Trained DeepAR model on SageMaker, deployed endpoint, performed live forecast & plotted output |
| 🔜 Day 4 | Automate retraining pipeline with EventBridge |

---

## 📸 Sample Output

- ✅ Actual vs Forecasted Sales Plot  
![Sample Forecast](images/sample_forecast_plot.png)  
(*Forecast for item_id: 1_GROCERY I using SageMaker DeepAR*)

---

## 📌 Future Enhancements

- Real-time inference with SageMaker endpoints  
- Lambda alerts for low-stock predictions  
- CI/CD pipeline for model updates  

---

## 🤝 Credits

- Dataset: Corporación Favorita (via Kaggle)
- Built by: Leo Das 🚀  
- Stack: AWS S3, Glue, Forecast, SageMaker, QuickSight

---

