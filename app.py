import streamlit as st

st.title("AI Social Media Content Generator")

platform = st.selectbox(
    "Choose Platform",
    ["Instagram", "LinkedIn", "TikTok"]
)

tone = st.selectbox(
    "Choose Tone",
    ["Professional", "Funny", "Luxury", "Motivational"]
)

business = st.text_input("Business Type")

if st.button("Generate Content"):

    st.write(f"Platform: {platform}")
    st.write(f"Tone: {tone}")

    st.subheader("Content Ideas")

    st.write(
        f"Create a {tone.lower()} {platform} campaign for a {business} business."
    )