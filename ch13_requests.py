# ============================================================
# Ch.13 requests - HTTP API 호출 (온라인 버전)
# 실제 HTTP 요청을 보내는 버전 - 인터넷 연결 필요
# pip install requests
# ============================================================
 
import requests
 
 
# ------------------------------------------------------------
# 1. 기본 GET 요청
# Java: restTemplate.getForObject(url, String.class)
# Python: requests.get(url) 한 줄로 끝
# ------------------------------------------------------------
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
 
print(response.status_code)          # 200
print(response.json())               # dict 반환
print(response.json()["title"])      # sunt aut facere...
 
 
# ------------------------------------------------------------
# 2. 쿼리 파라미터 - params 딕셔너리로 전달
# Java: UriComponentsBuilder.queryParam("userId", 1)
# Python: params={"userId": 1} → ?userId=1 자동 변환
# ------------------------------------------------------------
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
 
print(response.url)                  # 실제 요청된 URL 확인 (?userId=1 붙어있는지)
print(len(response.json()))          # userId=1의 게시글 수
print(response.json()[0]["title"])   # 첫 번째 게시글 제목
 
 
# ------------------------------------------------------------
# 3. 요청 헤더 / 인증 토큰
# 공공 API Key는 주로 헤더 또는 params에 담아 전송
# Java: headers.set("Authorization", "Bearer " + token)
# ------------------------------------------------------------
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers={
        "Authorization": "Bearer MY_TOKEN",
        "Accept": "application/json",
    }
)
 
print(response.status_code)         # 200 (이 API는 토큰 검증 안 함)
 
# 공공데이터포털은 params에 serviceKey 넣는 방식
# response = requests.get(url, params={"serviceKey": "YOUR_KEY", "pageNo": 1})
 
 
# ------------------------------------------------------------
# 4. POST 요청 - JSON 전송
# Java: restTemplate.postForObject(url, requestEntity, Response.class)
# json= 으로 전달하면 Content-Type: application/json 자동 설정
# ------------------------------------------------------------
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "새 게시글", "body": "내용", "userId": 1}
)
 
print(response.status_code)         # 201 Created
print(response.json())              # 생성된 리소스 (id: 101)
 
 
# ------------------------------------------------------------
# 5. 응답 상태 코드 처리
# raise_for_status() : 4xx/5xx면 HTTPError 자동 발생
# DE 파이프라인에서 선호 - 조용히 실패하는 버그 방지
# ------------------------------------------------------------
 
# 200 정상 케이스
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response.raise_for_status()         # 200대면 아무 일 없음
print(response.status_code)        # 200
 
# 404 케이스 (없는 ID)
response = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(response.status_code)        # 404
try:
    response.raise_for_status()    # HTTPError 발생
except requests.exceptions.HTTPError as e:
    print(f"에러: {e}")            # 에러: 404 Client Error
 
 
# ------------------------------------------------------------
# 6. 예외 처리 - 네트워크 오류 대비
# DE 파이프라인은 항상 timeout 설정 + 예외처리 필수
# ------------------------------------------------------------
def call_api(url):
    try:
        response = requests.get(url, timeout=(3, 5))   # 연결3초, 응답5초
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("타임아웃")
        return None
    except requests.exceptions.ConnectionError:
        print("연결 실패")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 오류: {e}")
        return None
 
# 정상
print(call_api("https://jsonplaceholder.typicode.com/posts/1"))
 
# 타임아웃 유도 (응답시간 0.0001초로 설정 → 무조건 타임아웃)
try:
    requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=0.0001)
except requests.exceptions.Timeout:
    print("타임아웃 발생 확인")
 
# 연결 실패 유도 (존재하지 않는 도메인)
try:
    requests.get("https://this-domain-does-not-exist-abc123.com", timeout=3)
except requests.exceptions.ConnectionError:
    print("연결 실패 확인")
 
 
# ------------------------------------------------------------
# 7. Session - 반복 요청 시 연결 재사용
# Java Connection Pool과 유사
# 공통 헤더/쿠키를 세션에 한 번만 설정하면 모든 요청에 자동 포함
# ------------------------------------------------------------
with requests.Session() as session:
    session.headers.update({"Accept": "application/json"})  # 공통 헤더 1번만
 
    for i in range(1, 4):
        data = session.get(
            f"https://jsonplaceholder.typicode.com/posts/{i}",
            timeout=5
        ).json()
        print(f"post {i}: {data['title']}")
 
 
# ------------------------------------------------------------
# 8. 공통 fetch 함수 - 토이 프로젝트 Ingest 레이어 기본 틀
# 이 함수를 기반으로 공공 API 수집 스크립트 작성
# ------------------------------------------------------------
def fetch_api_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=(3, 10))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"[ERROR] Timeout: {url}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP {e.response.status_code}: {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] 요청 실패: {e}")
        return None
 
data = fetch_api_data(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
print(f"수집 {len(data)}건")        # 수집 10건
 
 
# ------------------------------------------------------------
# 9. 공공데이터포털 응답 파싱 패턴 (참고용 - 실행 X)
# 실제 공공 API는 항상 response > header > body 구조
# resultCode "00" = 성공
# ------------------------------------------------------------
 
# url = "https://apis.data.go.kr/B552584/..."
# data = fetch_api_data(url, params={"serviceKey": "YOUR_KEY", "pageNo": 1})
#
# if data["response"]["header"]["resultCode"] == "00":
#     items = data["response"]["body"]["items"]["item"]
#     for item in items:
#         print(item)