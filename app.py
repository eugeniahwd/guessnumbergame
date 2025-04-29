import streamlit as st
import random

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Game Container */
    .game-container {
        max-width: 500px;
        margin: 50px auto;
        padding: 30px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    
    /* Title */
    .title {
        color: #764ba2;
        font-size: 2.5rem;
        margin-bottom: 20px;
        font-weight: 700;
    }
    
    /* Input Box */
    .stNumberInput input {
        border: 2px solid #764ba2 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    /* Button */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        transition: transform 0.3s !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.05) !important;
    }
    
    /* Result Text */
    .result {
        font-size: 1.2rem;
        margin: 20px 0;
        font-weight: bold;
    }
    
    /* Attempts Counter */
    .attempts {
        color: #764ba2;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======== GAME LOGIC ======== #
st.markdown('<div class="game-container">', unsafe_allow_html=True)
st.markdown('<div class="title">🎯 GUESS NUMBER MENG</div>', unsafe_allow_html=True)

# Initialize game state
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input(
    "Masukkin angka bro (1-100):",
    min_value=1,
    max_value=100,
    key="guess_input"
)

# Submit button
if st.button("TEBAK!", key="submit_btn"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.target:
        st.markdown(
            '<p class="result" style="color: #ff6b6b;">📉 TERLALU RENDAH KOCAK!</p>',
            unsafe_allow_html=True
        )
    elif guess > st.session_state.target:
        st.markdown(
            '<p class="result" style="color: #ff6b6b;">📈 TERLALU TINGGIIII!</p>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<p class="result" style="color: #4CAF50;">🎉 ANJAY! kamoe nebak dalam {st.session_state.attempts} percobaan!</p>',
            unsafe_allow_html=True
        )
        if st.button("MAIN LAGIII", key="play_again"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()

st.markdown(
    f'<div class="attempts">🔢 Percobaan: {st.session_state.attempts}</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)