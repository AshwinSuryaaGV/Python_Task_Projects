from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def fetch_headlines():
    try:
        url = "https://www.bbc.com/news"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("h2")

        unique_headlines = []

        for h in headlines:
            text = h.get_text().strip()
            if text and text not in unique_headlines:
                unique_headlines.append(text)

        return unique_headlines

    except Exception as e:
        return ["Error fetching headlines: " + str(e)]



@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to News Headlines API",
        "endpoints": {
            "/headlines": "Get latest headlines",
            "/save": "Save headlines to file"
        }
    })


@app.route("/headlines")
def get_headlines():
    headlines = fetch_headlines()
    return jsonify({
        "count": len(headlines),
        "headlines": headlines
    })


@app.route("/save")
def save_headlines():
    headlines = fetch_headlines()

    with open("headlines.txt", "w", encoding="utf-8") as f:
        f.write("News Headlines\n")
        f.write("="*40 + "\n")
        f.write("Generated on: " + str(datetime.now()) + "\n\n")

        for i, title in enumerate(headlines, 1):
            f.write(f"{i}. {title}\n")

    return jsonify({
        "message": "Headlines saved successfully!",
        "total_saved": len(headlines)
    })


if __name__ == "__main__":
    app.run(debug=True)
