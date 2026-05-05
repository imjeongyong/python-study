# Ch.6 함수
 
# -------------------------------------------------------
# 1. 기본 함수
# Java: public void sayHello(String name)
# -------------------------------------------------------
def say_hello(name):
    print(f"안녕하세요, {name}님")
 
say_hello("Kim")
# 출력: 안녕하세요, Kim님
 
# -------------------------------------------------------
# 2. 반환값
# Java: public int add(int a, int b)
# -------------------------------------------------------
def add(a, b):
    return a + b
 
result = add(3, 5)
print(result)   # 8
 
# -------------------------------------------------------
# 3. 기본값 파라미터
# Java에 없는 기능 - 파라미터 생략 가능
# -------------------------------------------------------
def greet(name, dept="미배정"):
    print(f"{name} / {dept}")
 
greet("Kim", "IT")  # Kim / IT
greet("Lee")        # Lee / 미배정
 
# -------------------------------------------------------
# 4. 다중 반환값
# Java: DTO 만들어야 했음 -> Python: 그냥 반환
# -------------------------------------------------------
def get_emp_info(emp_id):
    return "Kim", 35, "IT팀"   # 튜플로 반환
 
name, age, dept = get_emp_info(1)
print(name, age, dept)  # Kim 35 IT팀
 
# -------------------------------------------------------
# 5. 키워드 인자
# 순서 상관없이 파라미터명으로 전달 가능
# -------------------------------------------------------
def create_emp(name, age, dept):
    print(f"{name} / {age} / {dept}")
 
create_emp(age=35, dept="IT", name="Kim")   # 순서 바꿔도 OK
 
# -------------------------------------------------------
# 6. *args - 가변 인자
# Java: String... args 와 동일
# -------------------------------------------------------
def total_salary(*salaries):
    return sum(salaries)
 
print(total_salary(3000, 4000, 5000))   # 12000
print(total_salary(3000, 4000))         # 7000
 
# -------------------------------------------------------
# 7. **kwargs - 키워드 가변 인자
# 딕셔너리 형태로 받음
# -------------------------------------------------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
print_info(name="Kim", age=35, dept="IT")
# 출력:
# name: Kim
# age: 35
# dept: IT
 
# -------------------------------------------------------
# 8. lambda - 익명 함수
# Java: 람다식과 동일한 개념
# -------------------------------------------------------
# Java: (x) -> x * 2
double = lambda x: x * 2
print(double(5))    # 10
 
# 정렬에서 자주 씀
employees = [
    {"name": "Kim", "salary": 5000},
    {"name": "Lee", "salary": 3500},
    {"name": "Park", "salary": 7000},
]
 
sorted_emps = sorted(employees, key=lambda e: e["salary"])
for emp in sorted_emps:
    print(f"{emp['name']} - {emp['salary']}")
# 출력: Lee(3500) -> Kim(5000) -> Park(7000)