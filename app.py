import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Install required packages
# Run the following command before executing the script:
# pip install streamlit requests beautifulsoup4 selenium

def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 406:
            # Use Selenium as fallback
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html = driver.page_source
            driver.quit()
            soup = BeautifulSoup(html, 'html.parser')
        else:
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        
        headings = [h.get_text() for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        return headings, paragraphs, links
    except Exception as e:
        return str(e), [], []

st.title("AI WEB CRAWLER")

url = st.text_input("Enter website URL:")

if st.button("Scrape"):
    if url:
        headings, paragraphs, links = scrape_website(url)
        
        if isinstance(headings, str):
            st.error(f"Error: {headings}")
        else:
            st.subheader("Headings")
            st.write(headings if headings else "No headings found.")
            
            st.subheader("Paragraphs")
            st.write(paragraphs if paragraphs else "No paragraphs found.")
            
            st.subheader("Links")
            st.write(links if links else "No links found.")
    else:
        st.warning("Please enter a valid URL.")