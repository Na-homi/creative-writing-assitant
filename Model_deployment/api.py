from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Define the creative writing assistant function
def creative_writing_assistant(input_text: str, genre: str) -> str:
    """
    Generates creative suggestions to improve writing based on input text and selected genre.
    """
    system_prompt = f"""
    You are a creative writing expert helping writers refine their work in the genre: {genre}.
    
    Your task is to provide the following:
    1. *Metaphors*: Suggest creative metaphors that evoke emotions and engage readers.
    2. *Imagery*: Provide sensory-rich descriptions that bring the narrative to life.
    3. *Structure & Flow Suggestions*: Recommend ways to improve pacing and flow.
    4. *Tone and Voice Guidance*: Offer advice on enhancing tone and authenticity.
    5. *Creative Writing Tips*: Share unique tips to elevate the writer's craft.
    
    Here's the text: {input_text}
    """
    result = model.generate_content(system_prompt)
    return result.text

class Input(BaseModel):
    category: str
    draft: str



app = FastAPI()


@app.post('/creative-writer/')
async def assistant(user_input: Input):
    """
    
    """
    selected_genre = user_input.category
    user_text = user_input.draft
    suggestions = creative_writing_assistant(user_input, selected_genre)

    return {"output": suggestions}



