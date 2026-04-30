# ============================================================
# Ch.2 문자열 다루기
# Java와 다른 점 위주로 정리
# ============================================================


# ------------------------------------------------------------
# 1. 문자열 선언 - 홑따옴표/쌍따옴표 둘 다 OK
# ------------------------------------------------------------
a = "쌍따옴표"
b = '홑따옴표'
c = "He said 'hi'"       # 섞어 쓰기 가능
d = '그가 "안녕"이라 했다'

# 여러 줄 문자열 - PL/SQL 쿼리 담을 때 유용
sql = """
    SELECT *
    FROM emp
    WHERE dept_id = 10
"""
print(sql)


# ------------------------------------------------------------
# 2. f-string - Java String.format() 대체
# Java: String.format("%s의 연봉은 %d", name, salary)
# ------------------------------------------------------------
name = "Kim"
salary = 5000

msg = f"{name}의 연봉은 {salary}만원입니다"
print(msg)

# f-string 안에 연산도 가능
print(f"세후 연봉: {salary * 0.9:.1f}")  # :.1f = 소수점 1자리


# ------------------------------------------------------------
# 3. 슬라이싱 - Java substring() 대체
# [start:end] (end는 미포함)
# 음수 인덱스로 뒤에서 접근 가능 (Java에 없는 개념)
# ------------------------------------------------------------
s = "Tibero DB"
#    012345678
#   -9      -1

print(s[0])      # T     (첫 글자)
print(s[-1])     # B     (마지막 글자)
print(s[0:6])    # Tibero
print(s[:6])     # Tibero (처음부터)
print(s[7:])     # DB    (끝까지)
print(s[::-1])   # BD orediT (역순)


# ------------------------------------------------------------
# 4. 주요 메서드 - Java 비교
# Java toUpperCase()  -> upper()
# Java toLowerCase()  -> lower()
# Java trim()         -> strip()
# Java contains("x")  -> "x" in s
# Java length()       -> len(s)
# ------------------------------------------------------------
s = "  tibero_db  "

print(s.strip())                        # "tibero_db"
print(s.strip().upper())                # "TIBERO_DB"
print(s.strip().replace("_", " "))      # "tibero db"

if "tibero" in s:
    print("티베로 포함")


# ------------------------------------------------------------
# 5. split / join - 데이터 연계에서 자주 씀
# DB에서 받은 구분자 데이터 파싱할 때 활용
# ------------------------------------------------------------
# split
data = "10,20,30,40,50"
items = data.split(",")
print(items)    # ['10', '20', '30', '40', '50']

# join - Java String.join()과 동일
result = "|".join(items)
print(result)   # 10|20|30|40|50

# 실무 패턴 - 공백 제거 + 분리 + 합치기
raw = "  hong,35,IT팀  "
print(" / ".join(raw.strip().split(",")))  # hong / 35 / IT팀
