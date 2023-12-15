#
# Description  : Python Text Summarization
# Author's name: Adrian Statescu
# License      : MIT
#
import requests
from bs4 import BeautifulSoup
from summa import summarizer

def extract_text_from_website( url ):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from paragraphs or other relevant HTML elements
        text_elements = soup.find_all(['p', 'div', 'span'])

        text = ' '.join([element.get_text() for element in text_elements])

        return text
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

def generate_summary(text):
    summary = summarizer.summarize(text)
    return summary

def summarize_website(url):
    website_text = extract_text_from_website(url)

    if website_text:
        summary = generate_summary(website_text)
        return summary
    else:
        return None
# Example usage
website_url = "https://ae.oreilly.com/Python_Data_Science_Handbook_ch1"

website_summary = summarize_website(website_url)

if website_summary:
    print(website_summary)
else:
    print("Failed to summarize the website.")
