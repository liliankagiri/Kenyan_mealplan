## Setup Instructions

### 1. Activate Virtual Environment

Before installing dependencies, it's a good practice to create and activate a virtual environment. Use the following commands:

#### For Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

First, you need to install the required Python packages. Use the following command to install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Setup the API Key

To use the Gemini AI, you need an API key. Set the `GEMINI_API_KEY` as an environment variable by following these steps:

#### For Linux/MacOS:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

#### For Windows (Command Prompt):
```cmd
set GEMINI_API_KEY="your_api_key_here"
```

Make sure to replace `"your_api_key_here"` with your actual Gemini API key. Get your API key [here](https://aistudio.google.com/app/apikey).

### 4. Run the Program

Once everything is set up, you can run the program using:

```bash
python main.py
```


