import requests
import datetime
import os

API_KEY = os.getenv("GEMINI_API_KEY")

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

# ★ 最新の無料モデル（2026年時点）
MODEL = "gemini-1.5-flash"

# ★ v1beta → v1 に変更（これが重要）
url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, json=payload)
data = response.json()

# 新しいレスポンス形式に対応
try:
    content = data["candidates"][0]["content"]["parts"][0]["text"]
except Exception as e:
    print("Gemini API のレスポンス:", data)
    raise e

filename = f"_posts/{today}-intune-basic.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"---\ntitle: \"{title}\"\ndate: {today}\ncategories: [Intune]\n---\n\n")
    f.write(content)

print("記事生成完了:", filename)
