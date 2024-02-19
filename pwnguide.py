from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import os
def get_selected_page_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        h2_tags = soup.find_all('h2')
        h2_texts = [h2_tag.get_text() for h2_tag in h2_tags]
        links = [urljoin(url, h2_tag.find_next('a').get('href')) for h2_tag in h2_tags]
        print("Select the tutorial you want to see and enter its number below:")
        for i, text in enumerate(h2_texts):
            print(f"{i + 1}. {text}")
        selection = int(input("Enter your choice: ")) - 1
        selected_response = requests.get(links[selection])
        selected_response.raise_for_status()
        selected_soup = BeautifulSoup(selected_response.text, 'html.parser')
        selected_text = selected_soup.get_text(separator='\n')
        unwanted_text = ["Forum", "Toggle theme", "Service Status", "·", "pwn.guide", "Features", "Pricing", "Tutorials", "Documentation", "App", "Loading...", "See all free guides", "Menu", "For educational purposes only"]
        for text in unwanted_text:
            selected_text = selected_text.replace(text, "")
        return selected_text.strip()
    except Exception as e:
        print("Failed:", e)
        return None
url = "https://pwn.guide/free"
selected_page_text = get_selected_page_text(url)
if selected_page_text:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(selected_page_text.split('\n', 9)[-1])
