import requests
from bs4 import BeautifulSoup

# Step 1: URL of the news website
url = "https://www.bbc.com/news"

try:
    # Step 2: Send GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes

    # Step 3: Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 4: Find headline tags
    headlines = soup.find_all("h2")

    # Step 5: Extract text and remove duplicates
    headline_texts = set()

    for headline in headlines:
        text = headline.get_text().strip()
        if text:
            headline_texts.add(text)

    # Step 6: Save to text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("Top News Headlines\n")
        file.write("=" * 40 + "\n\n")

        for index, title in enumerate(headline_texts, start=1):
            file.write(f"{index}. {title}\n")

    print("Headlines successfully saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)
