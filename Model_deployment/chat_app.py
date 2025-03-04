import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDpx3Ljhqyp4KiB4rMcYpJJt_ZemPwdreA")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_prompt(user_prompt):
    system_prompt = f""" 
    You are an emotional support bot. You must act as the user's best friend and provide them guidance, 
    counselling and emotional support. You must never answer any question outside of this scope. In the event that a question like this comes up 
    just decline politely and state your role. Ensure that you are always sweet and courteous.
    user_input: {user_prompt}"""
    return system_prompt

st.title("EMOTIONAL SUPPORT BESTIE")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    final_prompt = get_prompt(user_prompt = prompt)
    output = model.generate_content(final_prompt)

    response = output.text
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})