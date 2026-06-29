import streamlit as st

st.title("Website Pertamaku")

nama = st.text_input("Masukkan nama")

if st.button("Kirim"):
    if nama.lower() == "fikri":
        st.success("Halo Fikri! Selamat datang.")
    else:
        st.write(f"Halo {nama}! Senang bertemu denganmu.")
