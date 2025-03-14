# Simple Web Scraper

## Project Description
AI Web Crawler is a **Streamlit-based web scraping tool** that extracts **headings, paragraphs, and links** from any website. It uses:
- **Requests & BeautifulSoup** for traditional scraping
- **Selenium** as a fallback for JavaScript-heavy pages

---

## Features
- Extract **headings (h1, h2, h3), paragraphs, and links**
- Handles websites blocking direct requests (via **Selenium**)
- Simple UI built with **Streamlit**
- Deployable on **Streamlit Cloud**

---

## Project Structure
```
📁 streamlit_web_scraper/
│── 📄 app.py               # Main Streamlit app
│── 📄 requirements.txt     # Dependencies
│── 📄 README.md            # Project documentation
```

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/prasanth-42/streamlit_web_scraper.git
cd streamlit_web_scraper
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

---

## How to Use
1. **Enter a website URL** in the input box.
2. Click the **"Scrape"** button.
3. View extracted **headings, paragraphs, and links**.

---




