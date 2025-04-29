import streamlit as st
import random

# CSS with proper formatting
st.markdown(
    """
    <style>
    /* Game Container (ubah background jadi transparan) */
    .game-container {
        max-width: 500px;
        margin: 50px auto;
        padding: 30px;
        background: rgba(255, 255, 255, 0.2) !important;  # Transparan
        backdrop-filter: blur(10px);  # Efek blur modern
        border-radius: 20px;
        text-align: center;
        color: white !important;  # Teks putih
    }
    
    /* Input Box (teks putih) */
    .stNumberInput input {
        color: white !important;
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Judul dan teks lainnya */
    .title, .attempts, .result {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Game logic
with st.container():
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown('<div class="title">🎯 GUESS NUMBER MENG</div>', unsafe_allow_html=True)

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
