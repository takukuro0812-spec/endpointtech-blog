import requests
import datetime
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

today = datetime.date.today().strftime("%Y-%m-%d")
title = "Intuneの基本をわかりやすく解説"

prompt = f"""
あなたはエンドポイント管理の専門家です。
以下のテーマで初心者向けのブログ記事を書いてください。

タイトル: {title}

構成:
- 導入
- 基本概念
- メリット
- 具体例
- まとめ

Markdown形式で出力してください。
"""

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "google/gemini-flash-1.5",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

# ★ エラー内容を必ず表示する
if "choices" not in data:
    print("OpenRouter API のレスポンス:", data)
    raise SystemExit("OpenRouter がエラーを返しました")

content = data["choices"][0]["message"]["content"]

filename = f"_posts/{today}-intune-basic.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\ntitle: \"{title}\"\ndate: {today}\ncategories: [Intune]\n---\n\n")
    f.write(content)

print("記事生成完了:", filename)
