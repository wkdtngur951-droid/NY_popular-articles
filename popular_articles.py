import os
import requests
from datetime import datetime

# 1. 환경 변수에서 API Key 가져오기
api_key = os.getenv("NYT_API_KEY")
# Most Popular - Viewed API (최근 1일간 가장 많이 본 기사)
url = f"https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}"

def fetch_nyt_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

def update_readme(articles):
    # README에 기록할 내용 생성
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    readme_content = f"## 📰 NYTimes Most Popular (Updated: {now})\n\n"
    
    for idx, article in enumerate(articles[:10]): # 상위 10개만 추출
        title = article.get("title")
        url = article.get("url")
        abstract = article.get("abstract")
        readme_content += f"{idx+1}. [{title}]({url})\n{abstract}\n\n\n"
    
    # README.md 파일 쓰기 (기존 내용을 덮어씌웁니다)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    data = fetch_nyt_data()
    if data:
        update_readme(data)
        print("README.md updated successfully!")