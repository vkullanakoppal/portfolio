import openai
import streamlit as st
import json

with open("openai_api_key.json", "r") as file:
    keys = json.load(file)

api_key = keys["OPENAI_API_KEY"].strip()

from openai import OpenAI
client = OpenAI(api_key=api_key)

# Streamlit Interface
st.title("Resume Bullet Point Generator")

role = st.text_input("Enter the role (e.g., Data Analyst, Software Engineer):")
experience = st.text_area("Enter your experience (e.g., Python, SQL, data analysis):")

if st.button("Generate Resume Bullet Point"):
    if role and experience:
        messages = [
            {"role": "system", "content": "You are a resume bullet point generator."},
            {"role": "user", "content": f"Generate a resume bullet point for a {role} role involving {experience}."}
        ]

        # Call the chat completions endpoint
        completion = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0125:personal::BuAH1C34",  
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )

        # Display the generated resume bullet point
        st.subheader("Generated Resume Bullet Point:")
        st.write(completion.choices[0].message.content)
    else:
        st.error("Please provide both the role and experience.")
