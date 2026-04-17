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

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

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
    content = data["
