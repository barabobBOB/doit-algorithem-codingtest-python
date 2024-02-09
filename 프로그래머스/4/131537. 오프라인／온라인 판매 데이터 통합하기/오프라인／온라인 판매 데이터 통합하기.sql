SELECT
    DATE_FORMAT(combined_sales.SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
    combined_sales.PRODUCT_ID,
    combined_sales.USER_ID,
    SUM(combined_sales.SALES_AMOUNT) AS SALES_AMOUNT
FROM (
    SELECT
        PRODUCT_ID,
        SALES_AMOUNT,
        SALES_DATE,
        USER_ID
    FROM
        ONLINE_SALE
    UNION ALL
    SELECT
        PRODUCT_ID,
        SALES_AMOUNT,
        SALES_DATE,
        NULL AS USER_ID
    FROM
        OFFLINE_SALE
) AS combined_sales
WHERE
    combined_sales.SALES_DATE LIKE '2022-03%'
GROUP BY
    DATE_FORMAT(combined_sales.SALES_DATE, "%Y-%m-%d"),
    combined_sales.PRODUCT_ID,
    combined_sales.USER_ID
ORDER BY
    DATE_FORMAT(combined_sales.SALES_DATE, "%Y-%m-%d") ASC,
    combined_sales.PRODUCT_ID ASC,
    combined_sales.USER_ID ASC;
