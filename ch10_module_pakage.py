# Ch.10 모듈과 패키지
 
# -------------------------------------------------------
# 1. 모듈 - .py 파일 하나 = 모듈 하나
# Java: import com.example.Employee
# -------------------------------------------------------
 
# 같은 폴더에 emp_utils.py 가 있다고 가정
# emp_utils.py 내용:
# def get_tax(salary):
#     return salary * 0.1
#
# def get_net(salary):
#     return salary * 0.9
 
# 전체 import
import emp_utils
print(emp_utils.get_tax(5000))  # 500.0
 
# 특정 함수만 import
from emp_utils import get_net
print(get_net(5000))            # 4500.0
 
# 별칭 사용
import emp_utils as eu
print(eu.get_tax(5000))         # 500.0
 
# -------------------------------------------------------
# 2. 표준 라이브러리 - pip 없이 바로 사용 가능
# -------------------------------------------------------
import os
import sys
import datetime
import math
import random
 
# os - 파일/디렉토리 다루기
print(os.getcwd())                  # 현재 작업 경로
print(os.path.exists("emp.txt"))    # 파일 존재 여부
os.makedirs("data", exist_ok=True)  # 폴더 생성
 
# datetime - 날짜/시간
today = datetime.date.today()
now = datetime.datetime.now()
print(today)                        # 2024-01-01
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 포맷 지정
 
# 날짜 계산
from datetime import timedelta
tomorrow = today + timedelta(days=1)
print(tomorrow)
 
# math
print(math.ceil(4.1))   # 5  올림
print(math.floor(4.9))  # 4  내림
print(math.sqrt(16))    # 4.0 제곱근
 
# random
print(random.randint(1, 10))        # 1~10 랜덤 정수
print(random.choice(["IT", "HR", "Finance"]))   # 랜덤 선택
 
# -------------------------------------------------------
# 3. 패키지 - 폴더 구조로 모듈 관리
# Java: 패키지 구조와 동일한 개념
# -------------------------------------------------------
# 폴더 구조:
# project/
# ├── main.py
# └── utils/
#     ├── __init__.py   ← 이 파일이 있어야 패키지로 인식
#     ├── emp_utils.py
#     └── file_utils.py
 
# main.py 에서 import
# from utils.emp_utils import get_tax
# from utils import file_utils
 
# -------------------------------------------------------
# 4. __name__ == "__main__"
# Java: public static void main(String[] args) 와 동일한 역할
# 이 파일이 직접 실행될 때만 아래 코드 실행
# 모듈로 import 될 때는 실행 안 됨
# -------------------------------------------------------
def main():
    print("메인 실행")
 
if __name__ == "__main__":
    main()
 
# -------------------------------------------------------
# 5. 실무 패턴 - 프로젝트 구조
# -------------------------------------------------------
# project/
# ├── main.py
# ├── config/
# │   ├── __init__.py
# │   └── settings.py      # DB 접속 정보 등 설정
# ├── utils/
# │   ├── __init__.py
# │   ├── file_utils.py    # 파일 처리
# │   └── date_utils.py    # 날짜 처리
# └── data/
#     ├── emp.csv
#     └── emp.json
 
# settings.py 예시
# DB_HOST = "localhost"
# DB_PORT = 8629          # Tibero 기본 포트
# DB_NAME = "tibero"
 
# main.py 에서
# from config.settings import DB_HOST, DB_PORT