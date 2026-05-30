import streamlit as st

st.title("AI Social Media Content Generator")

business = st.text_input("Business Type")

if st.button("Generate Content"):

    st.subheader("Instagram Captions")

    captions = [
        f"🔥 Discover why our {business} stands out from the crowd!",
        f"✨ Experience the best {business} experience today.",
        f"🚀 Taking {business} services to the next level."
    ]

    for caption in captions:
        st.write(caption)

    st.subheader("Hashtags")

    st.write("#marketing #business #growth #success #socialmedia")

    st.subheader("Reel Ideas")

    st.write("1. Behind the scenes")
    st.write("2. Customer testimonials")
    st.write("3. Day in the life")