
import streamlit as st
import random
import pandas as pd


# List of Growth Mindset Challenges
challenges = [
    "Try a new skill today and reflect on what you learned.",
    "Turn a failure into a lesson – write about it.",
    "Give someone positive feedback today.",
    "Step outside your comfort zone in one small way.",
    "Practice gratitude – list 3 things you're grateful for."
]

# List of Motivational Quotes
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Your only limit is your mind.",
    "Growth happens outside your comfort zone.",
    "Believe in your ability to improve.",
    "Mistakes are proof that you are trying."
]

# Streamlit UI
st.title("🌱 Growth Mindset Challenge : Web App with Streamlit")
st.write("Build a growth mindset with daily challenges and motivation! 🌟")

# Display a random challenge
st.subheader(" 💪 Today's Challenge:")
st.write(random.choice(challenges))

# Motivational Quote
st.subheader(" ❤️️ Motivational Quote:")
st.write(random.choice(quotes))

# User Reflection
st.subheader(" ☄︎ Your Reflection: ✔️")
user_input = st.text_area(" 💫 How did you approach today's challenge? ⍣ ")
if user_input:
    st.success("Reflection saved!⭐ Keep growing, pushing forward towords your goal. 💐")
else:
    st.info("tell us about yours approach ✈")

    #achievements
    st.subheader("💐Celebrate Wins:")
    achievement = st.text_input("Share something you've recently accomplished:🌷")

    if st.button("Submit"):
        st.success(f"Amazing Your achievement.😍")
    else:
        st.info("Big or small , every achievement counts! share one now 📢")

        #footer
        st.write("_ _ _")
        st.write("🎼Keep believing in Yourself. Growth is a journey, not a destination⭐")
        st.write("***🌸Created by Tayyaba Rafiq.***")
        

