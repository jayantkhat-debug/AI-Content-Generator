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

business = st.text_input("Enter Business Type")

if st.button("Generate Content"):

    st.success("Content Generated Successfully!")

    st.write("### Business")
    st.write(business)

    st.write("### Platform")
    st.write(platform)

    st.write("### Tone")
    st.write(tone)

    if platform == "Instagram":

        st.write("## Instagram Captions")

        st.write(f"🔥 Welcome to the best {business} experience!")
        st.write(f"✨ Discover why customers love our {business}.")
        st.write(f"🚀 Take your {business} journey to the next level.")

        st.write("## Hashtags")

        st.write("#instagram #business #marketing #growth #success")

        st.write("## Reel Ideas")

        st.write("1. Behind the scenes")
        st.write("2. Customer testimonials")
        st.write("3. Day in the life")

    elif platform == "LinkedIn":

        st.write("## LinkedIn Post")

        st.write(
            f"We are excited to share how our {business} business is creating value for customers through innovation and dedication."
        )

    elif platform == "TikTok":

        st.write("## TikTok Ideas")

        st.write("1. Before vs After")
        st.write("2. Trending challenge")
        st.write("3. Customer reactions")