CREATE DATABASE iphone_india_analytics;

USE iphone_india_analytics;

CREATE TABLE iphone_annual_shipments (
    Year INT PRIMARY KEY,
    Country VARCHAR(50) NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    Product_Category VARCHAR(50) NOT NULL,
    Annual_Shipments_Million DECIMAL(5,2) NULL, -- Allow NULL for 2026 pending full-year data
    Data_Status VARCHAR(50) NOT NULL,
    Source_Name VARCHAR(255) NOT NULL,
    Source_Date DATE NULL
);

INSERT INTO iphone_annual_shipments (Year, Country, Brand, Product_Category, Annual_Shipments_Million, Data_Status, Source_Name, Source_Date) VALUES
(2020, 'India', 'Apple', 'Smartphone', 3.20, 'Estimated', 'Counterpoint Research (reported by Statista)', '2021-01-27'),
(2021, 'India', 'Apple', 'Smartphone', 5.40, 'Reported estimate', 'CMR (reported by Business Standard)', '2022-01-17'),
(2022, 'India', 'Apple', 'Smartphone', 6.70, 'Reported estimate', 'IDC (reported by Economic Times)', '2023-03-21'),
(2023, 'India', 'Apple', 'Smartphone', 9.00, 'Estimated', 'IDC (reported by Mint)', '2023-10-31'),
(2024, 'India', 'Apple', 'Smartphone', 12.00, 'Reported estimate', 'IDC (reported by Indian Express)', '2025-02-10'),
(2025, 'India', 'Apple', 'Smartphone', 14.00, 'Estimated', 'Market data reported by TechCrunch', '2026-01-23'),
(2026, 'India', 'Apple', 'Smartphone', NULL, 'Pending full-year data', 'Not yet verified', NULL);

SELECT Year, Annual_Shipments_Million, Data_Status
FROM iphone_annual_shipments
ORDER BY Year ASC;

SELECT Year, Annual_Shipments_Million, Source_Name
FROM iphone_annual_shipments
WHERE Annual_Shipments_Million IS NOT NULL
ORDER BY Annual_Shipments_Million DESC
LIMIT 1;

SELECT 
    Year, 
    Annual_Shipments_Million,
    LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year) AS Previous_Year_Shipments,
    (Annual_Shipments_Million - LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year)) AS Absolute_Increase_Million
FROM iphone_annual_shipments;

SELECT 
    Year, 
    Annual_Shipments_Million,
    ROUND(
        ((Annual_Shipments_Million - LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year)) / 
         LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year)) * 100, 2
    ) AS YoY_Growth_Pct
FROM iphone_annual_shipments;

SELECT 
    Year, 
    Annual_Shipments_Million,
    RANK() OVER (ORDER BY Annual_Shipments_Million DESC) AS Shipment_Rank
FROM iphone_annual_shipments
WHERE Annual_Shipments_Million IS NOT NULL;

SELECT 
    COUNT(Year) AS Total_Historical_Years,
    ROUND(AVG(Annual_Shipments_Million), 2) AS Avg_Annual_Shipments_Million
FROM iphone_annual_shipments
WHERE Year BETWEEN 2020 AND 2025;

WITH GrowthCalculation AS (
    SELECT 
        Year, 
        Annual_Shipments_Million,
        LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year) AS Prev_Year
    FROM iphone_annual_shipments
)
SELECT 
    Year, 
    Annual_Shipments_Million,
    ROUND(((Annual_Shipments_Million - Prev_Year) / Prev_Year) * 100, 2) AS YoY_Growth_Pct
FROM GrowthCalculation
WHERE ((Annual_Shipments_Million - Prev_Year) / Prev_Year) * 100 > 30;

SELECT 
    Year, 
    Annual_Shipments_Million,
    SUM(Annual_Shipments_Million) OVER (ORDER BY Year ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS Cumulative_Shipments_Million
FROM iphone_annual_shipments
WHERE Annual_Shipments_Million IS NOT NULL;

SELECT 
    Data_Status, 
    COUNT(*) AS Record_Count,
    MIN(Annual_Shipments_Million) AS Min_Shipment,
    MAX(Annual_Shipments_Million) AS Max_Shipment
FROM iphone_annual_shipments
GROUP BY Data_Status;

SELECT 
    Year, 
    Annual_Shipments_Million
FROM iphone_annual_shipments
WHERE Annual_Shipments_Million IS NOT NULL 
  AND Data_Status != 'Pending full-year data'
ORDER BY Year;

WITH YoY_Table AS (
    SELECT 
        Year,
        Annual_Shipments_Million,
        LAG(Annual_Shipments_Million, 1) OVER (ORDER BY Year) AS Prev_Shipments
    FROM iphone_annual_shipments
),
Growth_Ranked AS (
    SELECT 
        Year,
        Annual_Shipments_Million,
        ROUND(((Annual_Shipments_Million - Prev_Shipments) / Prev_Shipments) * 100, 2) AS Growth_Pct,
        RANK() OVER (ORDER BY ((Annual_Shipments_Million - Prev_Shipments) / Prev_Shipments) DESC) as Growth_Rank
    FROM YoY_Table
    WHERE Prev_Shipments IS NOT NULL
)
SELECT * FROM Growth_Ranked;

SELECT 
    Year, 
    Annual_Shipments_Million,
    Data_Status,
    CASE 
        WHEN Annual_Shipments_Million IS NULL THEN 'Missing Value / Pending Data'
        WHEN Source_Date IS NULL THEN 'Missing Publication Date'
        ELSE 'Data Complete'
    END AS Quality_Audit_Status
FROM iphone_annual_shipments;


-- Identify missing years between 2020 and 2026

WITH RECURSIVE Year_List AS
(
    SELECT 2020 AS Year

    UNION ALL

    SELECT Year + 1
    FROM Year_List
    WHERE Year < 2026
)

SELECT Year
FROM Year_List
WHERE Year NOT IN
(
    SELECT DISTINCT Year
    FROM iphone_annual_shipments
)
ORDER BY Year;

SELECT `Year`, Annual_Shipments_Million
FROM iphone_annual_shipments
ORDER BY `Year`;

SELECT COUNT(*) AS Total_Records
FROM iphone_annual_shipments;