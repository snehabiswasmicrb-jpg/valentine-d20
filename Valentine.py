import streamlit as st
import time
import random

st.set_page_config(page_title="Valentine D20 Roll 💖", page_icon="🎲")

st.title("🧙‍♂️ A Valentine Quest Appears!")
st.subheader("💌 Will you be my Valentine Paul?")

st.write("Roll the D20 to determine your fate…")

if st.button("🎲 Roll the D20"):
    roll_placeholder = st.empty()

    # Suspense rolls
    for _ in range(8):
        roll_placeholder.markdown(
            f"## 🎲 Rolling… **{random.randint(1, 20)}**"
        )
        time.sleep(0.3)

    # The only real roll 😉
    roll = 20
    roll_placeholder.markdown("## 🎉 **NATURAL 20!!!** 🎉")

    st.success("❤️ SUCCESS! ❤️")
    st.markdown(
        """
        ### ✨ Critical Success!
        **Of course I want to be your Valentine 💍💕**

        You rolled a Natural 20 — destiny has spoken.
        """
    )