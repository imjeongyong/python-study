# Ch.11 이터레이터와 제너레이터
 
# -------------------------------------------------------
# 1. 이터러블 vs 이터레이터
# 이터러블: 순회 가능한 객체 (list, str, dict, set)
# 이터레이터: next()로 값을 하나씩 꺼낼 수 있는 객체
# -------------------------------------------------------
nums = [1, 2, 3]
 
# iter()로 이터레이터 생성
it = iter(nums)
 
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # StopIteration 에러
 
# for문이 내부적으로 iter() + next() 반복하는 것
for n in nums:
    print(n)
 
# -------------------------------------------------------
# 2. 커스텀 이터레이터
# __iter__, __next__ 구현
# Java: Iterable, Iterator 인터페이스 구현과 동일
# -------------------------------------------------------
class SalaryRange:
    def __init__(self, start, end, step=500):
        self.current = start
        self.end = end
        self.step = step
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value
 
for salary in SalaryRange(3000, 5000, 500):
    print(salary)
# 출력: 3000, 3500, 4000, 4500, 5000
 
# -------------------------------------------------------
# 3. 제너레이터 - yield 사용
# 이터레이터를 훨씬 간단하게 만드는 방법
# 값을 한 번에 메모리에 올리지 않고 필요할 때마다 생성
# 대용량 데이터 처리에 유리
# -------------------------------------------------------
def salary_range(start, end, step=500):
    current = start
    while current <= end:
        yield current       # 여기서 값 반환 후 일시정지
        current += step
 
for salary in salary_range(3000, 5000):
    print(salary)
# 출력: 3000, 3500, 4000, 4500, 5000
 
# -------------------------------------------------------
# 4. 제너레이터 vs 리스트 - 메모리 차이
# -------------------------------------------------------
# 리스트: 100만 개 전부 메모리에 올림
big_list = [i for i in range(1_000_000)]
 
# 제너레이터: 필요할 때 하나씩 생성 (메모리 효율적)
big_gen = (i for i in range(1_000_000))  # () 사용
 
print(type(big_list))   # <class 'list'>
print(type(big_gen))    # <class 'generator'>
 
# 대용량 파일 처리 시 제너레이터가 유리
def read_large_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()  # 한 줄씩만 메모리에 올림
 
# -------------------------------------------------------
# 5. 유용한 내장 함수 - 이터레이터 관련
# -------------------------------------------------------
employees = [
    {"name": "Kim", "salary": 5000},
    {"name": "Lee", "salary": 3500},
    {"name": "Park", "salary": 7000},
]
 
# map - 각 요소 변환 (List Comprehension으로 대체 가능)
names = list(map(lambda e: e["name"], employees))
print(names)    # ['Kim', 'Lee', 'Park']
 
# filter - 조건 필터링
high = list(filter(lambda e: e["salary"] >= 4000, employees))
print(high)     # [{'name': 'Kim'...}, {'name': 'Park'...}]
 
# zip - 두 리스트 묶기
# Java: 없음, 직접 구현해야 했음
names = ["Kim", "Lee", "Park"]
salaries = [5000, 3500, 7000]
 
for name, salary in zip(names, salaries):
    print(f"{name}: {salary}만원")
# 출력:
# Kim: 5000만원
# Lee: 3500만원
# Park: 7000만원
 
# enumerate + zip 동시 활용
for i, (name, salary) in enumerate(zip(names, salaries), 1):
    print(f"{i}. {name}: {salary}만원")