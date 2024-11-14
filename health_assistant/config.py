import os
from dotenv import load_dotenv

def set_openai_key():
    # Load environment variables from .env file if it exists
    load_dotenv()
    
    # Get the API key from environment variable or set it directly
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable "
            "or create a .env file with your API key."
        )
    
    return api_key