# ============================================================
# Ch.3 리스트와 튜플
# Java와 다른 점 위주로 정리
# ============================================================


# ------------------------------------------------------------
# 1. 리스트 기본 - Java ArrayList 대체
# Java: List<String> names = new ArrayList<>();
# ------------------------------------------------------------
names = ["Kim", "Lee", "Park"]  # 선언과 동시에 초기화
names.append("Choi")            # 추가 (Java: add())
print(names)

# 타입 섞기도 가능 (Java는 불가)
mixed = [1, "hello", True, None, 3.14]


# ------------------------------------------------------------
# 2. 주요 메서드 - Java 비교
# Java add(x)              -> append(x)
# Java add(i, x)           -> insert(i, x)
# Java remove(x)           -> remove(x)
# Java size()              -> len(list)
# Java contains(x)         -> x in list
# Java Collections.sort()  -> list.sort()
# Java get(i)              -> list[i]
# ------------------------------------------------------------
nums = [3, 1, 4, 1, 5, 9]

nums.append(2)       # 끝에 추가
nums.insert(0, 99)   # 0번 위치에 삽입
nums.remove(1)       # 값 1 첫 번째 것 삭제
nums.sort()          # 정렬
print(len(nums))     # 길이
print(5 in nums)     # True


# ------------------------------------------------------------
# 3. 슬라이싱 - 문자열과 동일하게 적용
# ------------------------------------------------------------
nums = [10, 20, 30, 40, 50]

print(nums[1:3])   # [20, 30]
print(nums[:3])    # [10, 20, 30]
print(nums[2:])    # [30, 40, 50]
print(nums[-1])    # 50 (마지막)
print(nums[::-1])  # [50, 40, 30, 20, 10] 역순


# ------------------------------------------------------------
# 4. List Comprehension - Java에 없는 강력한 문법
# Java: for문 + if + add() 여러 줄
# Python: 한 줄로 해결
# 구조: [표현식 for 변수 in 리스트 if 조건]
# ------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6]

# 짝수만 추출
evens = [n for n in nums if n % 2 == 0]
print(evens)    # [2, 4, 6]

# 전체 2배
doubled = [n * 2 for n in nums]
print(doubled)  # [2, 4, 6, 8, 10, 12]

# 문자열 리스트 가공
names = ["kim", "lee", "park"]
upper = [name.upper() for name in names]
print(upper)    # ['KIM', 'LEE', 'PARK']

# 연봉 10% 인상 (부동소수점 오차 방지: round 사용)
salaries = [3000, 4500, 5200, 2800, 6000]
raised = [round(s * 1.1, 1) for s in salaries]
print(raised)   # [3300.0, 4950.0, 5720.0, 3080.0, 6600.0]


# ------------------------------------------------------------
# 5. 튜플 - 읽기 전용 리스트, 소괄호 ()
# 변경되면 안 되는 데이터, 함수 다중 반환값에 사용
# ------------------------------------------------------------
point = (10, 20)
print(point[0])    # 10
# point[0] = 99   # ❌ TypeError: 수정 불가

# 함수에서 여러 값 반환 - Java는 DTO 만들어야 했음
def get_emp_info():
    return ("Kim", 35, "IT팀")

# 언패킹으로 한번에 받기
name, age, dept = get_emp_info()
print(name, age, dept)   # Kim 35 IT팀

# 딕셔너리 리스트 순회 시 언패킹 활용
emp_list = [("Kim", 35, 5000), ("Lee", 28, 3500), ("Park", 42, 7000)]

for name, age, salary in emp_list:
    print(f"{name} - {age}세 - {salary}만원")
