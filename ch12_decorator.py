# Ch.12 데코레이터와 컨텍스트 매니저
 
# -------------------------------------------------------
# 1. 데코레이터 기본 개념
# 함수에 기능을 추가하는 문법
# Java: AOP(Aspect Oriented Programming)와 유사한 개념
# -------------------------------------------------------
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[시작] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[종료] {func.__name__}")
        return result
    return wrapper
 
@log_decorator
def get_emp(emp_id):
    print(f"사원 조회: {emp_id}")
    return {"id": emp_id, "name": "Kim"}
 
emp = get_emp(1)
# 출력:
# [시작] get_emp
# 사원 조회: 1
# [종료] get_emp
 
# -------------------------------------------------------
# 2. 실행 시간 측정 데코레이터
# 성능 측정할 때 자주 씀
# -------------------------------------------------------
import time
 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행시간: {end - start:.4f}초")
        return result
    return wrapper
 
@timer
def process_data(data):
    time.sleep(0.1)     # 처리 시뮬레이션
    return [d * 2 for d in data]
 
result = process_data([1, 2, 3, 4, 5])
# 출력: process_data 실행시간: 0.1001초
 
# -------------------------------------------------------
# 3. 데코레이터 중복 적용
# 아래서 위 순서로 적용됨
# -------------------------------------------------------
@log_decorator
@timer
def heavy_job():
    time.sleep(0.05)
    print("작업 완료")
 
heavy_job()
# 출력:
# [시작] wrapper      <- log_decorator 먼저
# heavy_job 실행시간: 0.05초  <- timer
# 작업 완료
# [종료] wrapper
 
# -------------------------------------------------------
# 4. 파라미터 있는 데코레이터
# -------------------------------------------------------
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
 
@repeat(3)
def say_hello(name):
    print(f"안녕, {name}")
 
say_hello("Kim")
# 출력:
# 안녕, Kim
# 안녕, Kim
# 안녕, Kim
 
# -------------------------------------------------------
# 5. 컨텍스트 매니저
# with 문을 직접 만드는 방법
# Java: try-with-resources와 동일한 개념
# -------------------------------------------------------
class DBConnection:
    def __init__(self, host):
        self.host = host
 
    def __enter__(self):
        print(f"DB 연결: {self.host}")
        return self         # with ~ as 에 전달되는 값
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("DB 연결 종료")
        return False        # True면 예외 무시, False면 예외 전파
 
with DBConnection("localhost") as db:
    print(f"쿼리 실행 중... {db.host}")
# 출력:
# DB 연결: localhost
# 쿼리 실행 중... localhost
# DB 연결 종료
 
# -------------------------------------------------------
# 6. 실무 패턴 - 데이터 연계 업무에서 자주 쓰는 조합
# -------------------------------------------------------
import functools
 
def retry(max_count=3):
    def decorator(func):
        @functools.wraps(func)      # 원본 함수명 유지
        def wrapper(*args, **kwargs):
            for attempt in range(max_count):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"재시도 {attempt + 1}/{max_count}: {e}")
            print("최대 재시도 초과")
            return None
        return wrapper
    return decorator
 
@retry(max_count=3)
def fetch_data(url):
    raise ConnectionError("연결 실패")  # 실패 시뮬레이션
 
fetch_data("http://api.example.com")
# 출력:
# 재시도 1/3: 연결 실패
# 재시도 2/3: 연결 실패
# 재시도 3/3: 연결 실패
# 최대 재시도 초과