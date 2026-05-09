# Ch.13 Pandas 기초
# pip install pandas
 
import pandas as pd
 
# -------------------------------------------------------
# 1. Series - 1차원 데이터
# 인덱스가 있는 리스트라고 생각하면 됨
# -------------------------------------------------------
s = pd.Series([3000, 4500, 5200, 3800])
print(s)
# 0    3000
# 1    4500
# 2    5200
# 3    3800
 
# 인덱스 지정
s = pd.Series([3000, 4500, 5200], index=["Kim", "Lee", "Park"])
print(s["Kim"])     # 3000
print(s.mean())     # 평균
 
# -------------------------------------------------------
# 2. DataFrame - 2차원 데이터 (DB 테이블과 동일한 구조)
# -------------------------------------------------------
data = {
    "name": ["Kim", "Lee", "Park", "Choi"],
    "age":  [35, 28, 42, 30],
    "dept": ["IT", "HR", "IT", "Finance"],
    "salary": [5000, 3500, 7000, 4200],
}
 
df = pd.DataFrame(data)
print(df)
#    name  age     dept  salary
# 0   Kim   35       IT    5000
# 1   Lee   28       HR    3500
# 2  Park   42       IT    7000
# 3  Choi   30  Finance    4200
 
# -------------------------------------------------------
# 3. 기본 정보 확인
# -------------------------------------------------------
print(df.shape)         # (4, 4) 행, 열 수
print(df.dtypes)        # 컬럼별 타입
print(df.describe())    # 수치형 컬럼 통계 요약
print(df.head(2))       # 상위 2행
print(df.tail(2))       # 하위 2행
 
# -------------------------------------------------------
# 4. 컬럼 선택
# -------------------------------------------------------
print(df["name"])               # 단일 컬럼 -> Series
print(df[["name", "salary"]])   # 여러 컬럼 -> DataFrame
 
# -------------------------------------------------------
# 5. 행 필터링 - DB WHERE 절과 동일
# -------------------------------------------------------
# IT 부서만
it_df = df[df["dept"] == "IT"]
print(it_df)
 
# salary 4000 이상
high_df = df[df["salary"] >= 4000]
print(high_df)
 
# 여러 조건 (AND: &, OR: |)
result = df[(df["dept"] == "IT") & (df["salary"] >= 5000)]
print(result)
 
# -------------------------------------------------------
# 6. 정렬
# -------------------------------------------------------
# salary 오름차순
print(df.sort_values("salary"))
 
# salary 내림차순
print(df.sort_values("salary", ascending=False))
 
# -------------------------------------------------------
# 7. 컬럼 추가 / 수정
# -------------------------------------------------------
# 세후 연봉 컬럼 추가
df["net_salary"] = df["salary"] * 0.9
print(df)
 
# -------------------------------------------------------
# 8. 그룹별 집계 - DB GROUP BY와 동일
# -------------------------------------------------------
# 부서별 평균 연봉
print(df.groupby("dept")["salary"].mean())
# dept
# Finance    4200.0
# HR         3500.0
# IT         6000.0
 
# 부서별 인원수
print(df.groupby("dept")["name"].count())
 
# -------------------------------------------------------
# 9. CSV 읽기/쓰기
# -------------------------------------------------------
# CSV 저장
df.to_csv("emp.csv", index=False, encoding="utf-8")
 
# CSV 읽기
df2 = pd.read_csv("emp.csv", encoding="utf-8")
print(df2)
 
# -------------------------------------------------------
# 10. 결측값 처리 - 실무에서 자주 마주침
# -------------------------------------------------------
import numpy as np
 
df_null = pd.DataFrame({
    "name": ["Kim", "Lee", "Park"],
    "salary": [5000, None, 7000],   # None = 결측값
})
 
print(df_null.isnull())             # 결측값 여부 확인
print(df_null.isnull().sum())       # 컬럼별 결측값 개수
 
df_null["salary"].fillna(0)         # 결측값 0으로 채우기
df_null.dropna()                    # 결측값 있는 행 제거