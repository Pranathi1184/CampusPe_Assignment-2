# AI API Integration Project

## Project Overview

This project demonstrates integration with multiple Generative AI APIs using Python. Each API is implemented in a separate script that accepts user input, sends it to the respective AI service, and displays the response.

The project covers the following AI providers:

* Groq
* Ollama (local)
* Hugging Face
* Google Gemini
* Cohere
* Edyx API

---

## Objectives

* Learn how to work with multiple AI APIs
* Understand API authentication using environment variables
* Implement standardized API query structures
* Handle errors gracefully in API communication

---

## Project Structure

```
ai-api-integration/
│
├── groq_example.py         # Groq API (LLaMA models)
├── ollama_example.py       # Ollama local model (REST API)
├── huggingface_example.py  # Hugging Face Inference API
├── gemini_example.py       # Google Gemini API
├── cohere_example.py       # Cohere API
├── edyx_example.py        # Edyx API integration (OpenAI replacement)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env                    # API keys (not committed)
├── .env.example            # Sample environment variables
└── screenshots/            # Output screenshots
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <your-repo-link>
cd ai-api-integration
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Setup Environment Variables

Create a `.env` file using the provided `.env.example`:

```bash
cp .env.example .env
```

Add your API keys:

```
GROQ_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key
GOOGLE_API_KEY=your_key
COHERE_API_KEY=your_key
EDYX_API_KEY=your_key

---

## API Key Setup

| API           | Link                                     |
| ------------- | ---------------------------------------- |
| Groq          | https://console.groq.com/                |
| Hugging Face  | https://huggingface.co/settings/tokens   |
| Google Gemini | https://makersuite.google.com/app/apikey |
| Cohere        | https://dashboard.cohere.com/            |
| Ollama        | https://ollama.ai/ (local installation)  |
| Edyx          | https://www.edyx.in/                        |

---

## Running the Programs

Run each script individually:

```bash
python groq_example.py
python ollama_example.py
python huggingface_example.py
python gemini_example.py
python cohere_example.py
python edyx_example.py
```

Each program will:

1. Ask for user input
2. Send request to API
3. Display response
4. Handle errors gracefully

---

## Ollama Setup (Local Model)

Install Ollama from:
https://ollama.ai/

Run model locally:

```bash
ollama run llama3
```

Keep it running while executing `ollama_example.py`.

---

## API Implementation Details

### Groq

* Uses LLaMA-based models
* Fast inference API

### Ollama

* Runs locally (no API key required)
* Uses REST endpoint: `http://localhost:11434`

### Hugging Face

* Uses Inference API
* Requires Bearer token

### Gemini

* Uses Google Generative AI SDK
* Supports conversational responses

### Cohere

* Uses `generate()` API
* Supports text generation tasks

### Edyx (OpenAI Replacement)

* Uses REST API with Bearer Token
* Model: `situation-aware`
* Demonstrates real-time contextual AI processing

---

## Screenshots

All outputs are stored in the `screenshots/` folder:

* groq_output.png
* ollama_output.png
* huggingface_output.png
* gemini_output.png
* cohere_output.png
* edyx_output.png

---

## Important Notes

* API keys are stored using environment variables
* No API keys are hardcoded
* Error handling is implemented in all scripts
* Each script follows a consistent structure:

  * API Configuration
  * Query Function
  * Main Execution

---

## Conclusion

This project demonstrates how to integrate and work with multiple AI APIs in a structured and secure manner. It highlights differences between cloud APIs and local models while maintaining a consistent interface for querying AI systems.

---

## Acknowledgements

* CampusPe – Generative AI Course
* Official API documentation of respective providers
