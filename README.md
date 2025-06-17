# 🛠️ AWS S3 to Lambda ETL Pipeline

This project demonstrates a simple **serverless ETL pipeline** using **AWS S3** and **AWS Lambda**, where raw CSV files are cleaned and saved into a processed S3 bucket automatically upon upload.

---

## 📌 Project Overview

🔹 When a CSV file is uploaded to the **raw-data S3 bucket**,  
🔹 An **AWS Lambda function** is triggered via S3 event,  
🔹 The function reads the file, removes rows with missing values,  
🔹 And stores the cleaned file in a separate **processed-data S3 bucket**.

---

## 🧰 Tech Stack

- **AWS S3** – Object storage for raw and processed files  
- **AWS Lambda** – Serverless compute to perform ETL logic  
- **Python (Boto3)** – Used inside Lambda to process files  
- **CloudWatch Logs** – For monitoring and debugging

---



