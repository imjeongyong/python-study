# Ch.9 파일 입출력
 
# -------------------------------------------------------
# 1. 파일 쓰기
# Java: FileWriter, BufferedWriter
# Python: open() + write()
# -------------------------------------------------------
# mode: 'w' 쓰기(덮어씀), 'a' 추가, 'r' 읽기
with open("emp.txt", "w", encoding="utf-8") as f:
    f.write("Kim,35,IT,5000\n")
    f.write("Lee,28,HR,3500\n")
    f.write("Park,42,IT,7000\n")
# with 블록 끝나면 자동으로 파일 닫힘 (Java: try-with-resources)
 
# -------------------------------------------------------
# 2. 파일 읽기
# -------------------------------------------------------
# 전체 읽기
with open("emp.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
 
# 한 줄씩 읽기 (대용량 파일에 적합)
with open("emp.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())     # strip()으로 \n 제거
 
# 줄 단위 리스트로 읽기
with open("emp.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
# ['Kim,35,IT,5000\n', 'Lee,28,HR,3500\n', 'Park,42,IT,7000\n']
 
# -------------------------------------------------------
# 3. 파일 추가 모드
# mode 'a': 기존 내용 유지하고 뒤에 추가
# -------------------------------------------------------
with open("emp.txt", "a", encoding="utf-8") as f:
    f.write("Choi,30,HR,4000\n")
 
# -------------------------------------------------------
# 4. CSV 파일 처리 - 데이터 연계에서 자주 씀
# -------------------------------------------------------
import csv
 
# CSV 쓰기
employees = [
    ["name", "age", "dept", "salary"],
    ["Kim", 35, "IT", 5000],
    ["Lee", 28, "HR", 3500],
    ["Park", 42, "IT", 7000],
]
 
with open("emp.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees)
 
# CSV 읽기
with open("emp.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # 헤더를 키로 사용
    for row in reader:
        print(f"{row['name']} / {row['dept']} / {row['salary']}만원")
# 출력:
# Kim / IT / 5000만원
# Lee / HR / 3500만원
# Park / IT / 7000만원
 
# -------------------------------------------------------
# 5. JSON 파일 처리 - API 연동, 설정파일에서 자주 씀
# -------------------------------------------------------
import json
 
# JSON 쓰기
data = {
    "employees": [
        {"name": "Kim", "age": 35, "salary": 5000},
        {"name": "Lee", "age": 28, "salary": 3500},
    ]
}
 
with open("emp.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
# ensure_ascii=False: 한글 깨짐 방지
# indent=2: 들여쓰기 (보기 좋게)
 
# JSON 읽기
with open("emp.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
 
for emp in loaded["employees"]:
    print(f"{emp['name']} - {emp['salary']}만원")
# 출력:
# Kim - 5000만원
# Lee - 3500만원
 
# -------------------------------------------------------
# 6. 예외처리 포함 - 실무 패턴
# -------------------------------------------------------
def read_emp_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"파일 없음: {filepath}")
        return []
 
lines = read_emp_file("emp.txt")
lines_not_found = read_emp_file("nothing.txt")  # 파일 없음: nothing.txt