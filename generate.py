name: Auto Generate Blog Post

on:
  workflow_dispatch:
  schedule:
    - cron: "0 3 * * *"   # 毎日3時に自動実行

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install requests

      - name: Generate article with Gemini
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: python generate.py

      - name: Commit and push
        run: |
          git config --local user.email "actions@github.com"
          git config --local user.name "GitHub Actions"
          git add .
          git commit -m "Auto-generated article" || echo "No changes"
          git push

