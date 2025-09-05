# 🏡 Luxury Housing Analytics: End-to-End Data Pipeline (100K+ Records)

## 📌 Project Overview
This project replicates an **enterprise-style analytics pipeline** for the Bangalore luxury housing market.  
The goal is to **clean, store, and visualize** a large housing dataset (100K+ records) and generate actionable insights for real estate stakeholders.  

The project demonstrates skills across **data cleaning, feature engineering, database integration, and business intelligence visualization**.  
All Python code was implemented in **VS Code**.  

---

## 🧩 Business Use Cases
- **Market Intelligence:** Identify high-performing localities, builder-wise trends, and configuration demand shifts.  
- **Sales Optimization:** Use booking and inquiry data to uncover drop-off patterns.  
- **Buyer Persona Building:** Segment customers by Buyer Type and Comment sentiment.  
- **Competitive Pricing:** Analyze pricing strategies across builders and market segments.  
- **Amenity Score & Conversion:** Determine correlation between amenities and booking rates.  
- **Quarterly Trend Tracking:** Track real estate patterns across fiscal quarters to aid investment decisions.

---

## 🔧 Tech Stack
- **Python (Pandas, NumPy):** Data cleaning, feature engineering, and CSV manipulation.  
- **SQL (MySQL):** Structured data storage, schema creation, and querying.  
- **SQLAlchemy:** Python-to-SQL connection and automated insertion.  
- **Power BI:** Interactive dashboards, DAX measures, maps, and KPI visualizations.  
- **VS Code:** Python coding and project execution environment.  
- **Data Sources:** Raw & cleaned CSV files, GitHub for version control.  

---

## 🛠 Data Cleaning & Preprocessing
- Checked all columns for **nulls, duplicates, and inconsistent values**.  
- Filled missing numerical values using **median or mean** depending on the column (e.g., `Unit_Size_Sqft` → median, `Amenity_Score` → median, `Avg_Traffic_Time_Min` → mean).  
- Normalized string columns: `Micro_Market`, `Configuration`, `Transaction_Type`.  
- Standardized configuration labels: `'3 BHK' → '3BHK'`, `'4BHK+' → '4BHK+'`, etc.  
- Handled missing comments: `Buyer_Comments` filled with `'No Comment'`.  
- Removed duplicate rows to ensure dataset consistency.  

---

## ⚡ Derived Columns
- **Price_per_Sqft:** `Price_per_Sqft = (Ticket_Price_Cr * 1e7) / Unit_Size_Sqft`  
- **Quarter_Number:** Extracted fiscal quarter from `Purchase_Quarter`  
- **Booking_Flag:** `1` if `Transaction_Type` is "Primary", else `0`  

---

## 🗄 Database Integration
- Created a MySQL database `luxury_housing_bangalore_db`  
- Inserted cleaned dataset into table `luxury_properties` using **SQLAlchemy**  
- Validated data insertion with `COUNT`, `GROUP BY`, and `AVG` queries  
- Ensured normalized structure for efficient querying  

---

## 📊 Visualization in Power BI
- Connected Power BI directly to MySQL database  
- Builted **interactive dashboards**

---

## 📂 Project Workflow
1. **Load dataset** → Raw CSV  
2. **Data cleaning & preprocessing** → Handling nulls, string normalization, removing duplicates  
3. **Feature engineering** → Derived columns (`Price_per_Sqft`, `Quarter_Number`, `Booking_Flag`)  
4. **Save cleaned dataset** → Cleaned CSV  
5. **Database integration** → Load cleaned data into MySQL using SQLAlchemy  
6. **Power BI visualization** → Direct SQL connection for interactive dashboards  

---

## 📊 Power BI Visuals
1. **Market Trends:** Line chart of quarterly bookings per micro-market  
2. **Builder Performance:** Bar chart/table showing total ticket sales and average ticket size by builder  
3. **Amenity Impact:** Scatter plot of Amenity_Score vs Booking_Conversion_Rate (bubble size = project count)  
4. **Booking Conversion:** Stacked column chart showing % booking status per micro-market  
5. **Configuration Demand:** Pie/Donut chart of housing configurations vs booking count  
6. **Sales Channel Efficiency:** 100% stacked column chart of sales channels vs booking status  
7. **Quarterly Builder Contribution:** Matrix of builder performance by quarter  
8. **Possession Status Analysis:** Clustered column chart of possession status vs booking status by buyer type  
9. **Geographical Insights:** Map visualization of micro-market concentration  
10. **Top Performers:** Card visuals/KPI indicators for top 5 builders in revenue and booking success  

---

## ✅ Results
- Cleaned and normalized dataset stored in **MySQL**  
- Live, interactive Power BI dashboard connected to SQL  
- Analytical insights for real estate stakeholders (builders, investors, buyers)  
- Hands-on experience with Python, MySQL, and Power BI in an **end-to-end data pipeline**  

---

## 📂 File Structure
## 📂 File Structure
LUXURY_HOUSING_ANALYTICS/
│
├── Data_clean_and_MySQL_Insertion.py
├── Luxury_Housing_Bangalore.csv
├── Luxury_Housing_Bangalore_Cleaned.csv
├── Queries.sql
├── README.md
└── requirements.txt



---

## 📌 How to Run
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt

2. Run Python script: python Data_clean_and_MySQL_Insertion.py


3. Open Power BI and connect to luxury_housing_bangalore_db to explore dashboards.

---

## 📚 Dataset Source

Synthetic / Real estate dataset of Bangalore luxury housing (100K+ records) by Guvi

---

## 📜 License
This project is for educational purposes only.