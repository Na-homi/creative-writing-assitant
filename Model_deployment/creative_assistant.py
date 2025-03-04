from PIL import Image
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("API_KEY")

# Configure the API key
genai.configure(api_key = api_key)

# Select the model for the creative writing assistant
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

# Streamlit app layout
st.set_page_config(page_title="Creative Writing Assistant", page_icon=":writing_hand:", layout="wide")

# CSS Styling for a modern look
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 3rem;
            color: #2c3e50;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 1.2rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 20px;
        }
        .button {
            background-color: #3498db;
            color: white;
            padding: 12px 20px;
            border-radius: 5px;
            font-size: 1.1rem;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #2980b9;
        }
        .info-box {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: #e74c3c;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Add an image to the top of the page
image_path = "C:/Users/acer/Downloads/pexels-pixabay-372748.jpg"  # Update to the correct path
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Let your creativity flow!", width=600)

# Sidebar with navigation and genre selection
st.sidebar.title("Creative Writing Assistant")
st.sidebar.image(image, caption="Get inspired to write!", width=200)
st.sidebar.markdown("### Quick Navigation:")
st.sidebar.markdown("- *Enter Your Writing*: Add your text in the main section.")
st.sidebar.markdown("- *Generate Suggestions*: Receive tailored advice and tips.")
st.sidebar.markdown("### Genres of Writing:")
writing_genres = ["Poetry", "Short Story", "Essay", "Script", "Blog Post", "Other"]
selected_genre = st.sidebar.selectbox("Select Genre", writing_genres)

# Main page header and introduction
st.markdown('<div class="title">Creative Writing Assistant</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="subheader">
        Welcome to your personal writing partner! Whether you're crafting a poem, story, script, or essay, we’ll help you transform your ideas into polished, compelling pieces. Let’s elevate your creativity and refine your craft.
    </div>
""", unsafe_allow_html=True)

# Layout for input and suggestions
col1, col2 = st.columns([3, 2])

# Left column: Input text area
with col1:
    user_input = st.text_area(
        "Enter your writing here:",
        height=300,
        placeholder="Type or paste your draft here...",
    )

# Right column: Information box
with col2:
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("<h3>Quick Instructions:</h3>", unsafe_allow_html=True)
    st.markdown("1. Select a genre from the sidebar.")
    st.markdown("2. Enter your writing in the text box.")
    st.markdown("3. Click the *Generate Suggestions* button.")
    st.markdown("</div>", unsafe_allow_html=True)

# Button to generate suggestions
if st.button("Generate Suggestions", help="Click to refine your writing"):
    if user_input.strip():  # Ensure user entered text
        st.subheader("✨ Suggested Improvements:")
        suggestions = creative_writing_assistant(user_input, selected_genre)
        st.write(suggestions)
    else:
        st.markdown('<div class="error">Please enter some text to refine.</div>', unsafe_allow_html=True)