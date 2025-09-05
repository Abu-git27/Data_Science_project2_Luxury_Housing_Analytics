import pandas as pd
from sqlalchemy import create_engine
import os
import numpy as np

# Load dataset
df = pd.read_csv("C:/Users/HP/Downloads/Education/Data Science/GUvI/projects/Capstone project 2 All Details A to Z/luxury_housing/Luxury_Housing_Bangalore.csv")
print(df.head())
print(df.info())



print("********1.property_id column check********")
print(df['Property_ID'].head())  
print("total null values in property_id:",df['Property_ID'].isna().sum())



print("********2.Micro_market column check********")
print(df['Micro_Market'].head())
print("total null values in Micro_market:",df['Micro_Market'].isna().sum())
df['Micro_Market'] = df['Micro_Market'].str.strip().str.title()
print(df['Micro_Market'])



print("********3.project_name column check********")
print(df['Project_Name'].head())  
print("total null values in project_name:",df['Project_Name'].isna().sum())



print("********4.Developer_name column check********")
print(df['Developer_Name'].head())          
print("total null values in Developer_name:",df['Developer_Name'].isna().sum()) 



print("********5.unit_size_sqft column check********")
print(df['Unit_Size_Sqft'].head())        
print("total null values in unit_size_sqft:",df['Unit_Size_Sqft'].isna().sum())      
df['Unit_Size_Sqft'] = df['Unit_Size_Sqft'].fillna(df['Unit_Size_Sqft'].median())
print("total null values in unit_size_sqft (after fill):",df['Unit_Size_Sqft'].isna().sum())
print(df['Unit_Size_Sqft'])


print("********6.configuration column check********")
print(df['Configuration'].head())
print("total null values in configuration:",df['Configuration'].isna().sum())
print(df['Configuration'].value_counts().head())
df['Configuration'] = df['Configuration'].str.strip().str.upper()
df['Configuration'] = df['Configuration'].replace({
    '3 BHK': '3BHK',
    '3BHK+': '3BHK+',
    '2 BHK': '2BHK',
    '2BHK+': '2BHK+',
    '4 BHK': '4BHK',
    '4BHK+': '4BHK+'
})
print(df['Configuration'])




print("******** 7. Ticket_price column check ********")
print(df['Ticket_Price_Cr'].head())
print("Total null values in Ticket_price_cr:", df['Ticket_Price_Cr'].isna().sum())
df['Ticket_Price_Cr'] = (
    df['Ticket_Price_Cr']
    .astype(str)
    .str.replace(r'[₹,CcRr]', '', regex=True)
    .str.strip()
)
df['Ticket_Price_Cr'] = pd.to_numeric(df['Ticket_Price_Cr'], errors='coerce')
median_val = df['Ticket_Price_Cr'].median()
df['Ticket_Price_Cr'] = df['Ticket_Price_Cr'].fillna(median_val)
print("Total null values in Ticket_price_cr (after fill):", df['Ticket_Price_Cr'].isna().sum())
print(df['Ticket_Price_Cr'])


print("********8.Transaction_type column check********")
print(df['Transaction_Type'].head())
print("total null values in Transaction_type:",df['Transaction_Type'].isna().sum())
df['Transaction_Type'] = df['Transaction_Type'].str.strip().str.title()
df['Transaction_Type'] = df['Transaction_Type'].replace({
    'Primary': 'Primary',
    'Secondary': 'Secondary'
})



print("********9.Buyer_type column check********")
print(df['Buyer_Type'].head()) 
print(df['Buyer_Type'].unique())       
print("total null values in Buyer_type:",df['Buyer_Type'].isna().sum())   
print(df['Buyer_Type'].value_counts()) 



print("********10.purchase_quarter column check********")
print(df['Purchase_Quarter'].head())
print(df['Purchase_Quarter'].unique())    # check unique values
print("total null values in purchase_quarter:",df['Purchase_Quarter'].isna().sum())  # count missing values
df['Purchase_Quarter'] = pd.to_datetime(df['Purchase_Quarter'], errors='coerce')



print("********11.connectivity_score column check********")
print(df['Connectivity_Score'].head())
print(df['Connectivity_Score'].unique())     # check unique values
print("total null values in connectivity_score:",df['Connectivity_Score'].isna().sum()) # count missing values
print(df['Connectivity_Score'].describe())   # get basic stats



print("********12.Amenity_score column check********")
print(df['Amenity_Score'].head())
print(df['Amenity_Score'].unique())     # check unique values
print("total null values in Amenity_score:",df['Amenity_Score'].isna().sum()) # count missing values
print(df['Amenity_Score'].describe())   # summary stats
df['Amenity_Score'] = df['Amenity_Score'].fillna(df['Amenity_Score'].median())
print("total null values in Amenity_score (After fill):",df['Amenity_Score'].isna().sum())



print("********13.possession_status column check********")
print(df['Possession_Status'].head())
print(df['Possession_Status'].unique())      # check unique values
print("total null values in possession_status:",df['Possession_Status'].isna().sum())  # count missing values
print(df['Possession_Status'].value_counts())



print("********14.sales_channel column check********")
print(df['Sales_Channel'].head())
print(df['Sales_Channel'].unique())       # check unique values
print("total null values in sales_channel:",df['Sales_Channel'].isna().sum())   # count missing values
print(df['Sales_Channel'].value_counts())



print("********15.nri_buyer column check********")
print(df['NRI_Buyer'].head())
print(df['NRI_Buyer'].unique())       # check unique values
print("total null values in Nri_buyer:",df['NRI_Buyer'].isna().sum())   # count missing values
print(df['NRI_Buyer'].value_counts())



print("********16.Locality_infra_score column check********")
print(df['Locality_Infra_Score'].head())
print(df['Locality_Infra_Score'].unique())     # check unique values
print("total null values in Locality_infra_score:",df['Locality_Infra_Score'].isna().sum()) # count missing values
print(df['Locality_Infra_Score'].describe())   # summary stats



print("********17.Avg_traffic_time_min column check********")
print(df['Avg_Traffic_Time_Min'].head())
print(df['Avg_Traffic_Time_Min'].unique())     # check unique values
print("total null values in Avg_traffic_time_min:",df['Avg_Traffic_Time_Min'].isna().sum()) # count missing values
print(df['Avg_Traffic_Time_Min'].describe())   # summary stats



print("********18.Buyer_comments column check********")
print(df['Buyer_Comments'].head())      
print("total null values in Buyer_comments:",df['Buyer_Comments'].isna().sum())   # count missing values
df['Buyer_Comments'] = df['Buyer_Comments'].fillna('No Comment')
df['Buyer_Comments'] = df['Buyer_Comments'].astype(str).str.strip()
print("total null values in Buyer_comments (after fill):",df['Buyer_Comments'].isna().sum())
print(df['Buyer_Comments'].head())



print("********Duplicate_check in all columns********")
print("Number of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Number of duplicate rows (after drop):", df.duplicated().sum())
print("Shape after removing duplicates:", df.shape)



#Derived columns
print("1.derived column(Price_per_Sqft)")
df['Price_per_Sqft'] = ((df['Ticket_Price_Cr'] * 1e7) / df['Unit_Size_Sqft']).round(2)
print(df['Price_per_Sqft'])



print("2.derived column(Quarter_Number)")
df['Purchase_Quarter'] = pd.to_datetime(df['Purchase_Quarter'], format='%d-%m-%Y')
df['Quarter_Number'] = df['Purchase_Quarter'].dt.quarter



print("3.derived column(Booking_Flag)")
df['Booking_Flag'] = df['Transaction_Type'].apply(lambda x: 1 if x.lower() == 'primary' else 0)
print(df[['Transaction_Type', 'Booking_Flag']].head(10))




df.to_csv("C:/Users/HP/Downloads/Education/Data Science/GUvI/projects/Capstone project 2 All Details A to Z/luxury_housing/Luxury_Housing_Bangalore_Cleaned.csv", index=False)
print("Cleaned dataset saved successfully!")


username = 'root'
password = '12345'
host = 'localhost'
port = 3306
database = 'luxury_housing_bangalore_db'  
df = pd.read_csv("C:/Users/HP/Downloads/Education/Data Science/GUvI/projects/Capstone project 2 All Details A to Z/luxury_housing/Luxury_Housing_Bangalore_Cleaned.csv")
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
df.to_sql('luxury_properties', con=engine, if_exists='replace', index=False)
print("Data inserted successfully into SQL!")

