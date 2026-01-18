# JHU Agentic AI Project 1

## Overview

This project is an **Agentic AI application** developed as part of the Johns Hopkins University (JHU) Agentic AI curriculum. It leverages **LangChain** and **OpenAI** to perform advanced data analysis and automation tasks, focusing on financial markets and corporate AI initiatives.

The core of the project is a Jupyter Notebook that integrates financial data retrieval (via `yfinance`) with Large Language Model (LLM) capabilities to generate insights and visualizations.

## Features

-   **Financial Analysis**: Retrieval and analysis of stock market data using `yfinance`.
-   **AI-Powered Insights**: Utilization of OpenAI's LLMs via `LangChain` for intelligent data processing.
-   **Data Visualization**: Generation of trend charts and visual analytics using `matplotlib`.
-   **Corporate Strategy Analysis**: Processing of company data (from `Companies-AI-Initiatives.zip`) to understand AI adoption trends.

## Prerequisites

-   Python 3.8 or higher
-   An OpenAI API Key (or compatible LLM provider key)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Venu212/AIAgents_JHU.git
cd AIAgents_JHU
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configuration

This project requires API credentials to access LLM services.

1.  Locate the `config.json` file in the root directory.
2.  Ensure it contains your valid API key. **Note:** Do not commit your actual API key to version control.

Example `config.json` structure:
```json
{
 "API_KEY": "your-api-key-here",
 "OPENAI_API_BASE": "https://api.openai.com/v1" 
}
```
*(Note: If using a custom gateway like Great Learning, ensure the Base URL is correct as provided in your course materials.)*

## Usage

1.  Start the Jupyter Notebook server:
    ```bash
    jupyter notebook
    ```
2.  Open `JHU_AgenticAI_Project-1_Learners_Notebook.ipynb` in your browser.
3.  Run the cells sequentially to execute the agentic workflow.

## Project Structure

-   `JHU_AgenticAI_Project-1_Learners_Notebook.ipynb`: Main project notebook.
-   `data/`: Directory containing datasets (e.g., `Companies-AI-Initiatives.zip`).
-   `config.json`: Configuration file for API keys.
-   `requirements.txt`: List of Python dependencies.
-   `Stock_Price_Trends_3Y.png`: Generated output example.

## License

This project is for educational purposes as part of the JHU Agentic AI program.
