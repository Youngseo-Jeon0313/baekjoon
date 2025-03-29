-- 코드를 입력하세요
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SALES * B.PRICE) AS TOTAL_SALES
FROM BOOK B JOIN AUTHOR A JOIN BOOK_SALES S ON B.author_id = A.author_id AND B.book_id = S.book_id
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY B.author_id, B.category
ORDER BY AUTHOR_ID, CATEGORY DESC