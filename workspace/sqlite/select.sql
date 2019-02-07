-- 테이블값 모두 가져오기
SELECT * FROM classmate;

-- 테이블의 특정컬럼만 가져오기
SELECT id, name FROM classmate;

-- 가져오는 row(레코드)개수 지정하기
SELECT id, name FROM classmate LIMIT 2;

-- 가져오는 레코드에 시작점 지정(2칸 뛰고 1개 출력)
SELECT * FROM classmate LIMIT 1 OFFSET 2;

-- 특정한 값을 가진 row만 조회하기
SELECT * FROM classmate WHERE address='서울';
SELECT * FROM classmate WHERE id=2;

-- 서울에 사는 사람의 이름은?
SELECT name FROM classmate WHERE address='서울';