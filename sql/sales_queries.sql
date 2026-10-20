-- Q1: What are the total sales, number of orders, and average order value?
SELECT
    SUM(Sales) AS total_sales,
    COUNT(DISTINCT `Order ID`) AS total_orders,
    ROUND(
        SUM(Sales) / COUNT(DISTINCT `Order ID`),
        2
    ) AS average_order_value
FROM sales;

-- Q2: Which five products generate the highest total sales?
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 5;

-- Q3: Which month has the highest total sales?
SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
    ROUND(SUM(Sales), 2) AS monthly_sales
FROM sales
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY monthly_sales DESC
LIMIT 1;

-- Q4: Which regions contribute the most sales?
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- Q5: How did monthly sales change from the previous month?
SELECT
    sales_month,
    monthly_sales,
    ROUND(
        monthly_sales -
        LAG(monthly_sales) OVER (ORDER BY sales_month),
        2
    ) AS change_from_previous_month
FROM (
    SELECT
        DATE_FORMAT(`Order Date`, '%Y-%m') AS sales_month,
        SUM(Sales) AS monthly_sales
    FROM sales
    GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
) AS monthly_summary
ORDER BY sales_month;

-- Q6: Which product records have sales above 500 in the South region?
SELECT
    `Order ID`,
    `Product Name`,
    Region,
    Sales
FROM sales
WHERE Sales > 500
  AND Region = 'South'
ORDER BY Sales DESC;

-- Q7: How can product records be classified by sales value?
SELECT
    `Order ID`,
    `Product Name`,
    Sales,
    CASE
        WHEN Sales >= 1000 THEN 'Large'
        WHEN Sales >= 300 THEN 'Medium'
        ELSE 'Small'
    END AS sales_size
FROM sales;

-- Q8: Which categories have total sales above 100000?
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Category
HAVING SUM(Sales) > 100000
ORDER BY total_sales DESC;