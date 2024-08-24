WITH 
DIFFER_YEAR AS(
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR
)

SELECT YEAR(ED.DIFFERENTIATION_DATE) AS YEAR, DY.MAX_SIZE-ED.SIZE_OF_COLONY AS YEAR_DEV, ED.ID
FROM ECOLI_DATA ED
JOIN DIFFER_YEAR DY
ON YEAR(ED.DIFFERENTIATION_DATE) = DY.YEAR
ORDER BY 1,2;