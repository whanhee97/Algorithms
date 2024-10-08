WITH
BEST_MEMBER AS(
    SELECT * FROM(
    SELECT MEMBER_ID,COUNT(MEMBER_ID) CNT, RANK() OVER(ORDER BY COUNT(MEMBER_ID) DESC) AS RANK_A
    FROM REST_REVIEW
    GROUP BY MEMBER_ID)X
    WHERE X.RANK_A = 1
    -- ORDER BY CNT DESC
)

SELECT MEMBER_NAME,REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM BEST_MEMBER BM
JOIN REST_REVIEW RR
ON BM.MEMBER_ID = RR.MEMBER_ID
JOIN MEMBER_PROFILE MP
ON BM.MEMBER_ID = MP.MEMBER_ID
WHERE 1=1
ORDER BY REVIEW_DATE, REVIEW_TEXT
;