import streamlit as st
import random

# ===== CSS CUSTOM =====
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
    /* BACKGROUND GRADIENT */
    .stApp {
        background: linear-gradient(135deg, #a8c0ff 0%, #9fa4c4 100%) !important;
        min-height: 100vh;
    }
    
    /* SEMUA TEKS PUTIH */
    .stNumberInput label, .stButton button, 
    .game-title, .attempts, .result,
    .stNumberInput input, .stNumberInput input::placeholder {
        color: white !important;
    }
    
    /* INPUT BOX STYLING */
    .stNumberInput input {
        background: rgba(255,255,255,0.2) !important;
        border: 2px solid white !important;
    }
    
    /* TOMBOL GRADIENT */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #9fa4c4 100%) !important;
        border: none !important;
        width: 100%;
    }
    
    /* HOVER EFFECT */
    .stButton>button:hover {
        transform: scale(1.02) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== GAME LOGIC =====
st.markdown('<h1 class="game-title">🎯 GUESS NUMBER MENG</h1>', unsafe_allow_html=True)

if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input(
    "Masukkin angka bro (1-100):",
    min_value=1,
    max_value=100,
    key="guess_input"
)

if st.button("TEBAK!", key="submit_btn"):
    st.session_state.attempts += 1
    
    if guess < st.session_state.target:
        st.error("📉 TERLALU RENDAH KOCAK!")
    elif guess > st.session_state.target:
        st.error("📈 TERLALU TINGGIIII!")
    else:
        st.success(f"🎉 ANJAY! kamoe nebak dalam {st.session_state.attempts} percobaan!")
        if st.button("MAIN LAGIII", key="play_again"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0
            st.rerun()

st.markdown(f'<p class="attempts">🔢 Percobaan: {st.session_state.attempts}</p>', unsafe_allow_html=True)
