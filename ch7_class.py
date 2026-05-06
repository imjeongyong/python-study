# Ch.7 클래스와 객체지향
 
# -------------------------------------------------------
# 1. 클래스 기본
# Java: public class Employee { ... }
# -------------------------------------------------------
class Employee:
    def __init__(self, name, age, salary):  # Java: 생성자
        self.name = name        # Java: this.name = name
        self.age = age
        self.salary = salary
 
    def get_info(self):         # Java: public void getInfo()
        print(f"{self.name} / {self.age}세 / {self.salary}만원")
 
emp = Employee("Kim", 35, 5000)
emp.get_info()
# 출력: Kim / 35세 / 5000만원
 
# -------------------------------------------------------
# 2. self - Java this와 동일
# 모든 인스턴스 메서드 첫 번째 파라미터는 self
# -------------------------------------------------------
class Counter:
    def __init__(self):
        self.count = 0
 
    def increment(self):
        self.count += 1
 
    def get(self):
        return self.count
 
c = Counter()
c.increment()
c.increment()
print(c.get())  # 2
 
# -------------------------------------------------------
# 3. 상속
# Java: public class Manager extends Employee
# -------------------------------------------------------
class Manager(Employee):    # Employee 상속
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)     # Java: super()
        self.team_size = team_size
 
    def get_info(self):     # 메서드 오버라이딩
        super().get_info()
        print(f"팀 인원: {self.team_size}명")
 
mgr = Manager("Park", 42, 8000, 10)
mgr.get_info()
# 출력:
# Park / 42세 / 8000만원
# 팀 인원: 10명
 
# -------------------------------------------------------
# 4. 클래스 변수 vs 인스턴스 변수
# Java: static 변수 vs 인스턴스 변수
# -------------------------------------------------------
class Employee:
    company = "ABC Corp"    # 클래스 변수 (Java: static)
 
    def __init__(self, name):
        self.name = name    # 인스턴스 변수
 
emp1 = Employee("Kim")
emp2 = Employee("Lee")
 
print(Employee.company)     # ABC Corp (클래스로 접근)
print(emp1.company)         # ABC Corp (인스턴스로도 접근 가능)
print(emp1.name)            # Kim
print(emp2.name)            # Lee
 
# -------------------------------------------------------
# 5. __str__ - Java toString() 대체
# -------------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def __str__(self):
        return f"Employee({self.name}, {self.salary}만원)"
 
emp = Employee("Kim", 5000)
print(emp)  # Employee(Kim, 5000만원)
 
# -------------------------------------------------------
# 6. 실무 패턴 - 데이터 클래스
# DB 결과를 객체로 매핑할 때
# -------------------------------------------------------
class EmpDTO:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary
 
    def __str__(self):
        return f"[{self.emp_id}] {self.name} / {self.dept} / {self.salary}만원"
 
# DB SELECT 결과를 객체 리스트로
rows = [(1, "Kim", "IT", 5000), (2, "Lee", "HR", 3500)]
emps = [EmpDTO(*row) for row in rows]   # * 언패킹
 
for emp in emps:
    print(emp)
# 출력:
# [1] Kim / IT / 5000만원
# [2] Lee / HR / 3500만원