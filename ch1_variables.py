# ============================================================
# Ch.1 변수와 타입
# Java와 다른 점 위주로 정리
# ============================================================


# ------------------------------------------------------------
# 1. 변수 선언 - 타입 선언 없음 (동적 타이핑)
# ------------------------------------------------------------
# Java: String name = "Kim";
name = "Kim"
age = 30
salary = 5000.5
is_active = True   # Java: true -> Python: True (대문자)
dept = None        # Java: null -> Python: None

print(name, age, salary, is_active, dept)


# ------------------------------------------------------------
# 2. 동적 타이핑 - 변수에 다른 타입 재할당 가능
# Java는 컴파일 에러, Python은 가능
# ------------------------------------------------------------
x = 100
print(type(x), x)   # <class 'int'>

x = "Tibero"
print(type(x), x)   # <class 'str'>

x = [1, 2, 3]
print(type(x), x)   # <class 'list'>


# ------------------------------------------------------------
# 3. 기본 타입
# Java int/long/BigInteger -> Python int (크기 제한 없음)
# Java float/double       -> Python float
# Java String             -> Python str
# Java boolean            -> Python bool
# Java null               -> Python None
# Java char               -> 없음 (길이 1짜리 str)
# ------------------------------------------------------------
big_num = 99999999999999999999999999999
print(big_num * big_num)  # 그냥 됨 (Java는 BigDecimal 필요)


# ------------------------------------------------------------
# 4. None 비교 - is 사용 (== 아님)
# None은 싱글톤 객체라 is로 비교하는 게 권장
# Java: obj == null   -> Python: obj is None
# ------------------------------------------------------------
result = None

if result is None:
    print("값 없음")    # 권장
if result == None:
    print("값 없음")    # 작동은 하지만 비추


# ------------------------------------------------------------
# 5. 진리값 (Truthiness) - Java에 없는 개념
# Falsy: False, None, 0, 0.0, "", [], {}, ()
# 그 외 전부 Truthy
# ------------------------------------------------------------
data = []
if data:
    print("데이터 있음")
else:
    print("데이터 없음")   # 빈 리스트는 Falsy

count = 0
if not count:
    print("0은 Falsy")


# ------------------------------------------------------------
# 6. 타입 힌트 - 선택사항, 강제 아님 (IDE/리뷰어용 문서)
# Java처럼 타입을 명시하고 싶을 때 사용
# ------------------------------------------------------------
emp_name: str = "Kim"
emp_age: int = 35
salaries: list[int] = [3000, 4000, 5000]

def get_age(emp_id: str) -> int:
    return 35
