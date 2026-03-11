# ✈️ AI Travel Planner

An **AI-powered travel planning assistant** that generates complete trip plans including **flights, hotels, budgets, and travel itineraries** using Large Language Models.

The system combines **FastAPI, LangChain, OpenAI, and Streamlit** to create an interactive travel planning experience.

It uses **LLM-powered extractors and web scraping** to gather travel information and generate structured trip plans.

Users can either:

- Generate trips using a structured planner
- Plan trips using natural language via an AI chat assistant

# 🛠 Tech Stack
### Backend 
- Python
- FastAPI
- LangChain
- OpenAI API

### Frontend

- Streamlit

### AI / Data Processing

- Large Language Models (OpenAI)
- Prompt Engineering
- Web Scraping
- Information Extraction
- LLM-based Data Extractors

---

# 🚀 Features

### ✈️ AI Trip Planning

Users can generate a complete trip plan by providing:

- Origin city
- Destination
- Number of travelers
- Trip duration

The system automatically generates:

- Flight information
- Hotel suggestions
- Budget estimation
- Travel itinerary

---

## 💬 AI Travel Chat Assistant

Users can plan trips using natural language.

Example:

```
Plan a 5 day trip from Berlin to Rome for 2 people
```

The AI automatically extracts:

- Origin
- Destination
- Number of travelers
- Trip duration

using an **LLM-based query parser** and generates the full travel plan.

---

## ✈️ Flight Information Extraction

The system gathers travel information through **web scraping** and processes it using an **LLM extractor** to obtain:

- Average flight price
- Airlines operating the route
- Estimated flight duration
- Important travel notes

---

## 🏨 Hotel Suggestions

The system extracts hotel information from scraped data using an **LLM-based hotel extractor**.

Users can directly search hotels using booking platforms such as:

- Booking.com
- Expedia
- KAYAK

---

## 💰 Budget Estimation

The system calculates an estimated trip cost including:

- Flights
- Hotels
- Local transport
- Activities

This gives users a **quick financial overview before booking the trip.**

---

## 🗺️ Travel Itinerary Generation

The AI generates a **day-by-day itinerary** based on:

- destination
- trip duration
- common attractions
- realistic travel pacing

The itinerary is generated using an **LLM-powered itinerary generator.**

---

# 🏗 System Architecture

```
User (Streamlit UI)
        │
        ▼
FastAPI Backend
        │
        ▼
Travel Service
        │
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
Flight Extractor  Hotel Extractor  Budget Calculator
 │               │               │
 ▼               ▼               ▼
Web Scraping → LLM Processing → Structured Travel Plan
```

---



# 📂 Project Structure

```
ai-travel-agent
│
├── backend
│   ├── agents
│   │   ├── flight_extractor.py
│   │   ├── hotel_extractor.py
│   │   └── query_parser.py
│   │
│   ├── services
│   │   └── travel_service.py
│   │
│   ├── extractors
│   │
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```
git clone https://github.com/karanexc/ai-travel-agent.git
cd ai-travel-agent
```

---

## Create Virtual Environment

```
python -m venv venv
```

Activate environment

Mac / Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Run Backend

```
uvicorn backend.main:app --reload
```

API will run on:

```
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```
streamlit run streamlit_app.py
```

---

# 📌 Example Usage

### Trip Planner Input

```
Origin: London
Destination: Rome
Travelers: 2
Days: 5
```

### Output

- Flight information
- Hotel suggestions
- Budget breakdown
- Travel itinerary

---

### AI Chat Example

```
Plan a 4 day trip from Mumbai to New York
```

The AI automatically extracts travel parameters and generates the trip.

---

# 📈 Future Improvements

Planned enhancements include:

- Real-time flight APIs
- Live hotel pricing integration
- Interactive travel maps
- Multi-agent orchestration
- RAG-based travel knowledge

---

# 👨‍💻 Author

**Karan Mhaswadkar**

MSc Computer Science (Artificial Intelligence)  
University of Kent

GitHub  
https://github.com/karanexc

---

# 📄 License

MIT License
