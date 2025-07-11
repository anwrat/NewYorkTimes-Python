import requests
from datetime import datetime

API_BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_KEY = "OsBhT3Ae8fRTGG7fflqqdf0xMk8LvA3X"

def main():
    now = datetime.now()
    current_date = now.date()
    day = now.strftime("%A") # %A means weekday full version like Sunday, while %a means Sun (short version)
    print(f"{current_date} {day}")
    print("Hello this is New York Times")
    search_term = input("Enter a search term: ")
    print("Displaying results.....")
    print("\n\n")
    search_results = search_articles(search_term)
    display_results(search_results)

def search_articles(search_term):
    #Creating a dictionary to fill the "?q=election&api-key=yourkey" using requests library
    params = {
        "q": search_term,
        "api-key": API_KEY
    }
    response = requests.get(API_BASE_URL, params)
    return response.json()

def display_results(search_results):
    # The docs dictionary inside reponse contains all the articles
    docs = search_results["response"]["docs"]
    i = 0
    # Iterating through each article
    for doc in docs:
        i += 1
        article_web_url = doc["web_url"]
        article_headline = doc["headline"]["main"]
        print(f"Article no {i}")
        print(article_headline)
        print(f"URL: ({article_web_url})")
        print("\n\n")

if __name__ == '__main__':
    main()