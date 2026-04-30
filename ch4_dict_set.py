# ============================================================
# Ch.4 딕셔너리와 셋
# Java와 다른 점 위주로 정리
# ============================================================


# ------------------------------------------------------------
# 1. 딕셔너리 기본 - Java HashMap 대체
# Java: Map<String, Object> emp = new HashMap<>();
#       emp.put("name", "Kim");
#       emp.get("name");
# ------------------------------------------------------------
emp = {"name": "Kim", "age": 35, "dept": "IT"}

print(emp["name"])      # Kim
print(emp.get("name"))  # Kim

emp["salary"] = 5000    # 추가
emp["age"] = 36         # 수정
del emp["dept"]         # 삭제
print(emp)


# ------------------------------------------------------------
# 2. get() - KeyError 방지
# Java: getOrDefault()와 동일
# ------------------------------------------------------------
emp = {"name": "Kim", "age": 35}

# print(emp["salary"])        # ❌ KeyError
print(emp.get("salary"))      # None (에러 안 남)
print(emp.get("salary", 0))   # 0   (기본값 지정)


# ------------------------------------------------------------
# 3. 딕셔너리 순회
# ------------------------------------------------------------
emp = {"name": "Kim", "age": 35, "dept": "IT"}

# 키만
for key in emp:
    print(key)

# 값만
for value in emp.values():
    print(value)

# 키 + 값 동시에 (가장 자주 씀)
for key, value in emp.items():
    print(f"{key}: {value}")


# ------------------------------------------------------------
# 4. 딕셔너리 리스트 - DB 결과셋과 동일한 구조
# SELECT 결과를 Python에서 다룰 때 이 패턴이 기본
# ------------------------------------------------------------
employees = [
    {"name": "Kim", "age": 35, "salary": 5000},
    {"name": "Lee", "age": 28, "salary": 3500},
    {"name": "Park", "age": 42, "salary": 7000},
]

for emp in employees:
    print(f"{emp['name']} - {emp['salary']}만원")

# 4000 이상만 필터 (List Comprehension 활용)
high_salary = [e for e in employees if e["salary"] >= 4000]
print(high_salary)


# ------------------------------------------------------------
# 5. 셋(Set) - 중복 제거, Java HashSet과 동일
# ------------------------------------------------------------
tags = {"IT", "HR", "IT", "Finance", "HR"}
print(tags)   # {'IT', 'HR', 'Finance'} 중복 제거됨

# 리스트 중복 제거할 때 자주 씀
depts = ["IT", "HR", "IT", "Finance", "HR"]
unique = list(set(depts))
print(unique)

# 집합 연산 - 두 테이블 데이터 비교할 때 유용
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)   # {3, 4}         교집합
print(a | b)   # {1,2,3,4,5,6}  합집합
print(a - b)   # {1, 2}         차집합
