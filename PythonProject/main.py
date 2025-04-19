import streamlit as st

st.title("🔐 Basit Şifre Güvenlik Testi")

sifre = st.text_input("Şifrenizi girin:", type="password")

if sifre:
    uzun = len(sifre) >= 8
    kucuk = any(c.islower() for c in sifre)
    buyuk = any(c.isupper() for c in sifre)
    rakam = any(c.isdigit() for c in sifre)
    sembol = any(c in "!@#$%^&*()_-+=<>?/|{}[]~" for c in sifre)

    puan = sum([uzun, kucuk, buyuk, rakam, sembol])

    if puan == 5:
        st.success("Şifre Güçlü 💪")
    elif puan >= 3:
        st.warning("Şifre Orta ⚠️")
    else:
        st.error("Şifre Zayıf ❌")

    if not uzun:
        st.write("- En az 8 karakter olmalı")
    if not kucuk:
        st.write("- Küçük harf içermeli")
    if not buyuk:
        st.write("- Büyük harf içermeli")
    if not rakam:
        st.write("- Rakam içermeli")
    if not sembol:
        st.write("- Sembol içermeli (örn. ! @ # $)")
