# Gemini-Phi AI Multi-Agent System

## Overview
This project is a **Python-based multi-agent AI system** that leverages **Google Gemini LLM via Phi Agents** to automate financial and web data analysis. The system consists of:

- **Web Agent**: Fetches the latest news articles from the web (via DuckDuckGo).  
- **Finance Agent**: Summarizes analyst recommendations and financial data (via YFinanceTools).  
- **Team Agent**: Combines outputs from web and finance agents into structured summaries.

The system is capable of producing **actionable insights** for stocks (e.g., NVDA) without a UI.

---

## Features

- Multi-agent architecture for task delegation  
- Integration with Google Gemini LLM  
- Fetches and summarizes:
  - Latest news articles  
  - Analyst recommendations (buy, hold, sell ratings)  
- Outputs results in **structured tables** for readability  
- Fully automated and script-based (no UI required)

---

## Technologies Used

- Python 3.10+  
- [Phi Agents](https://phi.ai/)  
- Google Gemini (via `phi.model.google.Gemini`)  
- DuckDuckGo search (`ddgs`)  
- YFinanceTools (`yfinance`)  
- dotenv (`python-dotenv`)  

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/RajShah03/gemini-phi-agent.git
cd gemini_agent
```
Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies
```bash
pip install -r requirements.txt
```

Create a .env file with your Google API key:
```bash
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

Run the script
```bash
python gemini_agent.py
```
# gemini-phi-agent
Multi-agent AI system using Phi and Gemini for finance &amp; web analysis.
