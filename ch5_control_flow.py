# Ch.5 조건문과 반복문
 
# -------------------------------------------------------
# 1. if / elif / else
# -------------------------------------------------------
score = 85
 
if score >= 90:
    print("A")
elif score >= 80:   # Java: else if -> Python: elif
    print("B")
else:
    print("C")
# 출력: B
 
# -------------------------------------------------------
# 2. 삼항 연산자
# Java: score >= 60 ? "합격" : "불합격"
# -------------------------------------------------------
result = "합격" if score >= 60 else "불합격"
print(result)
# 출력: 합격
 
# -------------------------------------------------------
# 3. for + range
# Java: for (int i = 0; i < 5; i++)
# -------------------------------------------------------
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)
 
for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)
 
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step)
    print(i)
 
# -------------------------------------------------------
# 4. 컬렉션 순회
# -------------------------------------------------------
names = ["Kim", "Lee", "Park"]
 
for name in names:              # 값만
    print(name)
 
for i, name in enumerate(names, 1):    # 인덱스 + 값 (1부터 시작)
    print(f"{i}. {name}")
# 출력:
# 1. Kim
# 2. Lee
# 3. Park
 
emp = {"name": "Kim", "age": 35}
for key, value in emp.items():  # 딕셔너리 순회
    print(f"{key}: {value}")
 
# -------------------------------------------------------
# 5. while
# Java: count++ 없음, += 사용
# -------------------------------------------------------
count = 0
while count < 5:
    print(count)
    count += 1  # count++ 없음
 
# -------------------------------------------------------
# 6. break / continue
# -------------------------------------------------------
for i in range(10):
    if i == 5:
        break       # 루프 탈출
    print(i)        # 0, 1, 2, 3, 4
 
for i in range(5):
    if i == 2:
        continue    # 건너뛰기
    print(i)        # 0, 1, 3, 4
 
# -------------------------------------------------------
# 7. 실무 패턴 - DB 결과 처리
# -------------------------------------------------------
employees = [
    {"name": "Kim", "salary": 5000},
    {"name": "Lee", "salary": 3500},
    {"name": "Park", "salary": 7000},
]
 
# 연봉 합계
total = 0
for emp in employees:
    total += emp["salary"]
print(f"총 연봉: {total}만원")  # 15500만원
 
# 특정 직원 찾기 - 찾으면 break로 탈출
target = "Lee"
for emp in employees:
    if emp["name"] == target:
        print(f"찾음: {emp}")
        break