WITH RECURSIVE GET_HOUR (HOUR)
  AS (SELECT 0
       UNION ALL
      SELECT HOUR+1
        FROM GET_HOUR
       WHERE HOUR < 23
     )
SELECT G.HOUR, IFNULL(COUNT(ANIMAL_ID),'0')
FROM GET_HOUR G
LEFT OUTER JOIN ANIMAL_OUTS A ON G.HOUR = HOUR(DATETIME)
GROUP BY 1
ORDER BY 1