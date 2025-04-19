import streamlit as st
import string

sifre = st.text_input("şifrenizi giriniz")

if len(sifre)<3:
    st.stop()

# 8karakter
# büyük küçük h. sembol ve rakam
bh = string.ascii_uppercase
kh = string.ascii_lowercase
sy = string.punctuation
dg = string.digits

bhsay = 0
khsay = 0
sysay = 0
dgsay = 0
for harf in sifre:
    i = bh.count(harf)
    bhsay = bhsay + i

    y = kh.count(harf)
    khsay = khsay + y

    z = sy.count(harf)
    sysay = sysay + z

    t = dg.count(harf)
    dgsay = dgsay + t

#print("küçükharf:", khsay, "büyükharf:", bhsay, "sembolsay:", sysay, "rakam", dgsay)

sonuc = khsay * bhsay * dgsay * sysay

if len(sifre) < 8:
    sonuc = 0

if sonuc != 0:
    st.success("şifre güvenilir")
else:
    st.error("şifre güvenilir değil")