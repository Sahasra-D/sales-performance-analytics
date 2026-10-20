# SQL Analysis Report – Sales Performance Analytics

## 1. Introduction

The purpose of this phase was to analyse the sales dataset using SQL and understand how sales performance varies across products, regions, and months. After cleaning the dataset in Python, I imported the cleaned data into MySQL and used SQL queries to calculate key business metrics and identify useful trends.

## 2. Dataset Overview

The dataset contains 9,994 records with information about customer orders, products, sales, discounts, quantities, and profits. It includes columns such as Order ID, Order Date, Ship Date, Region, Category, Product Name, Sales, Quantity, Discount, and Profit.

The cleaned dataset was stored in a MySQL table named `sales` in the `sales_performance` database.

## 3. Tools Used

- **MySQL 8.0:** For storing the dataset and performing SQL analysis.
- **MySQL Command Line Client:** For executing queries and checking results.
- **Visual Studio Code:** For maintaining SQL scripts and project documentation.

## 4. Analysis Performed

### 4.1 Overall Sales Performance

I calculated total sales, the number of unique orders, and average order value. These metrics provide a basic overview of the business's sales performance.

### 4.2 Top Five Products by Sales

I grouped the data by product name, calculated the total sales for each product, and sorted the results in descending order. The top five products were selected to identify which products generated the highest sales.

### 4.3 Monthly Sales Analysis

I used the order date to group sales by month and calculate monthly sales totals. This helped identify the month with the highest sales.

### 4.4 Regional Sales Analysis

I grouped sales by region to compare performance across different geographical areas. Sorting the results made it easier to identify the regions with higher and lower sales.

### 4.5 Month-to-Month Sales Changes

I used the `LAG()` window function to compare each month's sales with the previous month's sales. The difference helped identify periods when sales increased or decreased.

### 4.6 Filtering Sales Records

I used the `WHERE` clause to filter transactions with sales greater than 500 in the South region. This demonstrated how SQL can be used to retrieve records that meet specific conditions.

### 4.7 Sales Categorisation Using CASE

I used the `CASE` statement to classify sales records into different categories based on sales values. This made it possible to group transactions into meaningful ranges for further analysis.

### 4.8 Filtering Groups Using HAVING

I used the `HAVING` clause to identify regions whose total sales exceeded 100,000. Unlike `WHERE`, which filters individual rows, `HAVING` filters groups after aggregation.

### 4.9 Joining Sales and Product Tables

To practise joins, I created a separate `products` table using distinct product IDs, product names, and categories from the sales data. I then joined it with the `sales` table using Product ID to retrieve order details alongside product information.

## 5. SQL Concepts Used

The main SQL concepts used in this phase were:

- Aggregate functions: `SUM()`, `COUNT()`, and `ROUND()`
- Grouping and sorting: `GROUP BY` and `ORDER BY`
- Filtering: `WHERE` and `HAVING`
- Limiting results: `LIMIT`
- Conditional logic: `CASE`
- Date formatting: `DATE_FORMAT()`
- Window functions: `LAG()`
- Table joins: `JOIN`

## 6. Key Learnings

During this phase, I learned how SQL can be used to analyse a dataset beyond simply retrieving records. Grouping and aggregate functions helped summarise sales data, while date functions made monthly analysis possible. I also gained practical experience with window functions and joins.

I encountered a few issues while importing the CSV file and working with column names that were not present in the MySQL table. Resolving these issues helped me understand the importance of checking table structures and ensuring that SQL queries match the available data.

## 7. Conclusion

The SQL analysis phase helped me examine overall sales performance, compare products and regions, and study changes in monthly sales. It also gave me practical experience writing and executing SQL queries in MySQL. The results from this phase can be used in the next stage of the project to create visualisations and a sales performance dashboard.

## Validation: MySQL vs Pandas

The results obtained using MySQL were compared with the results calculated using Pandas in Python. Both tools used the same dataset and formulas.

### Validation Results

- **Total Revenue**
  - Pandas: 2,297,201.07
  - MySQL: 2,297,201.07
  - Status: Match

- **Number of Orders**
  - Pandas: 5,009
  - MySQL: 5,009
  - Status: Match

- **Average Order Value**
  - Pandas: 458.61
  - MySQL: 458.61
  - Status: Match

### Conclusion

All three metrics matched between Pandas and MySQL. This confirms that the calculations were consistent across both tools and provides confidence in the accuracy of the sales analysis.
