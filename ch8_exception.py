# Ch.8 예외처리
 
# -------------------------------------------------------
# 1. 기본 구조
# Java: try / catch / finally
# Python: try / except / finally
# -------------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
finally:
    print("항상 실행")
# 출력:
# 0으로 나눌 수 없음
# 항상 실행
 
# -------------------------------------------------------
# 2. 예외 종류별 처리
# Java: catch (Exception e) 여러 개
# -------------------------------------------------------
def parse_salary(value):
    try:
        return int(value)
    except ValueError:
        print(f"숫자 변환 실패: {value}")
        return 0
    except TypeError:
        print("잘못된 타입")
        return 0
 
print(parse_salary("5000"))     # 5000
print(parse_salary("abc"))      # 숫자 변환 실패: abc -> 0
print(parse_salary(None))       # 잘못된 타입 -> 0
 
# -------------------------------------------------------
# 3. 예외 메시지 출력
# Java: catch (Exception e) { e.getMessage(); }
# -------------------------------------------------------
try:
    data = {"name": "Kim"}
    print(data["salary"])
except KeyError as e:
    print(f"키 없음: {e}")     # 키 없음: 'salary'
 
# -------------------------------------------------------
# 4. 예외 발생시키기
# Java: throw new IllegalArgumentException()
# -------------------------------------------------------
def set_salary(salary):
    if salary < 0:
        raise ValueError("연봉은 0 이상이어야 합니다")
    return salary
 
try:
    set_salary(-1000)
except ValueError as e:
    print(e)    # 연봉은 0 이상이어야 합니다
 
# -------------------------------------------------------
# 5. 커스텀 예외
# Java: class CustomException extends Exception
# -------------------------------------------------------
class SalaryError(Exception):
    def __init__(self, salary):
        super().__init__(f"잘못된 연봉: {salary}")
        self.salary = salary
 
def set_salary(salary):
    if salary < 0:
        raise SalaryError(salary)
    return salary
 
try:
    set_salary(-500)
except SalaryError as e:
    print(e)    # 잘못된 연봉: -500
 
# -------------------------------------------------------
# 6. 실무 패턴 - DB 연동 시 예외처리
# -------------------------------------------------------
def get_emp(employees, emp_id):
    try:
        emp = next(e for e in employees if e["id"] == emp_id)
        return emp
    except StopIteration:
        print(f"사원 없음: {emp_id}")
        return None

employees = [
    {"id": 1, "name": "Kim", "salary": 5000},
    {"id": 2, "name": "Lee", "salary": 3500}
]

emp = get_emp(employees, 1)
print(emp)    # {'id': 1, 'name': 'Kim', 'salary': 5000}

emp = get_emp(employees, 99)
print(emp)    # 사원 없음: 99 -> None