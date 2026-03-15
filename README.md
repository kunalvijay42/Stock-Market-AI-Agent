# 📈 Stock Market AI Agent
 
A **multi-agent AI system** built with CrewAI that autonomously researches live stock market data and generates in-depth analysis with actionable trading recommendations — powered by Groq LLM, yfinance, and an interactive Streamlit UI.
 
---
 
## 🤖 How It Works
 
```
User Input (Stock Ticker e.g. AAPL)
              │
              ▼
┌─────────────────────────────────────────────┐
│                  CrewAI Crew                │
│                                             │
│   ┌─────────────────┐                       │
│   │  Analyst Agent  │  Fetches live stock   │
│   │                 │  data via yfinance,   │
│   │  Tools:         │  performs deep        │
│   │  • yfinance     │  fundamental &        │
│   │    stock tool   │  technical analysis   │
│   └────────┬────────┘                       │
│            │                                │
│            ▼                                │
│   ┌─────────────────┐                       │
│   │  Trader Agent   │  Synthesizes          │
│   │                 │  analysis into        │
│   │                 │  Buy / Hold / Sell    │
│   │                 │  recommendation       │
│   └────────┬────────┘                       │
└────────────┼────────────────────────────────┘
             │
             ▼
  ┌─────────────────────┐
  │  Streamlit UI / CLI │  Final Report
  └─────────────────────┘
```
 
---
 
## ✨ Features
 
- 📊 **Live stock data** fetched in real-time using `yfinance` — no paid API needed
- 🤖 **Multi-agent collaboration** — Analyst and Trader agents work sequentially
- 💡 **AI-generated recommendations** — Buy / Hold / Sell with reasoning
- ⚡ **Groq-powered inference** — ultra-fast LLM responses via `llama-3.1-8b-instant`
- 🖥️ **Streamlit UI** — interactive web interface for non-technical users
- 💻 **CLI runner** — `main.py` for quick terminal-based execution
- 🔧 **Modular structure** — easily add new agents, tasks, or tools
 
---
 
## 🛠️ Tech Stack
 
| Component | Technology |
|---|---|
| **Agent Framework** | CrewAI |
| **LLM** | Groq (`llama-3.1-8b-instant`) via LiteLLM |
| **Stock Data** | yfinance |
| **Frontend UI** | Streamlit |
| **Language** | Python 3.11 |
 
---
 
## 📁 Project Structure
 
```
Stock-Market-AI-Agent/
├── agents/
│   └── *.py                    # Analyst and Trader agent definitions
├── tasks/
│   └── *.py                    # Task definitions for analysis and trading
├── tools/
│   └── stock_research_tool.py  # yfinance-based live stock data tool
├── crew.py                     # Wires agents and tasks into a CrewAI Crew
├── streamlit_app.py            # Streamlit web UI
├── main.py                     # CLI runner
├── test.py                     # Testing scripts
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md
```
 
---
 
## ⚙️ Setup & Installation
 
### 1. Clone the repository
```bash
git clone https://github.com/kunalvijay42/Stock-Market-AI-Agent.git
cd Stock-Market-AI-Agent
```
 
### 2. Create and activate a virtual environment
```bash
python -m venv venv
 
# Windows
venv\Scripts\activate
 
# macOS/Linux
source venv/bin/activate
```
 
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
 
### 4. Configure environment variables
 
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
 
Get your free Groq API key at [console.groq.com](https://console.groq.com)
 
> **Note:** For Groq models like `groq/llama-3.1-8b-instant`, LiteLLM is required:
> ```bash
> pip install litellm
> ```
 
---

*Powered by CrewAI · Groq · yfinance · Streamlit*