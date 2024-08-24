WITH
GRADE_INFO AS(
    SELECT 
        EMP_NO,
        CASE 
        WHEN SUM(SCORE) / COUNT(HALF_YEAR) >= 96 THEN 'S'
        WHEN SUM(SCORE) / COUNT(HALF_YEAR) >= 90 THEN 'A'
        WHEN SUM(SCORE) / COUNT(HALF_YEAR) >= 80 THEN 'B'
        ELSE 'C' END AS GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT
    GI.EMP_NO,
    HE.EMP_NAME,
    GI.GRADE,
    CASE GI.GRADE
    WHEN 'S' THEN HE.SAL*0.2
    WHEN 'A' THEN HE.SAL*0.15
    WHEN 'B' THEN HE.SAL*0.1
    ELSE 0 END AS BONUS
FROM HR_EMPLOYEES HE
JOIN GRADE_INFO GI
ON GI.EMP_NO = HE.EMP_NO
ORDER BY GI.EMP_NO