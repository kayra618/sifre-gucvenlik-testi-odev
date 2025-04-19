import streamlit as st
import random
import string
from datetime import datetime

istimestamp = st.sidebar.checkbox("TimeStamp Kullanılsın")
ts = ""
if istimestamp:
    ts = str(int(datetime.timestamp(datetime.now())))

adet = st.sidebar.slider("Şifre Karakter Sayısı",8,40,12)

kh = string.ascii_lowercase  # küçükharfleri
bh = string.ascii_uppercase  # büyükharfler
sy = string.punctuation  # noktalama işaretler
dg = string.digits  # rakamlar

iskh = st.sidebar.checkbox("Küçük Harf",value=True)
isbh = st.sidebar.checkbox("Büyük Harf",value=True)
issy = st.sidebar.checkbox("Sembol",value=True)
isdg =st.sidebar.checkbox("Rakam",value=True)



k1 = 0
k2 = 0
k3 = 0
k4 = 0
toplam = 0
artiksec = []

if iskh:
    k1 = 1
    toplam = toplam + 1
    artiksec = artiksec + list(kh)
if isbh:
    k2 = 1
    toplam = toplam + 1
    artiksec = artiksec + list(bh)
if issy:
    k3 = 1
    toplam = toplam + 1
    artiksec = artiksec + list(sy)
if isdg:
    k4 = 1
    toplam = toplam + 1
    artiksec = artiksec + list(dg)

if istimestamp and adet > 20:
    kartik = adet - toplam - len(ts)

else:
    kartik = adet - toplam

if toplam==0:
    st.warning("En az 1 karakter tipi seçmelisiniz")
    st.stop()

khsec = random.choices(kh, k=k1)
bhsec = random.choices(bh, k=k2)
sysec = random.choices(sy, k=k3)
dgsec = random.choices(dg, k=k4)

artik = random.choices(artiksec, k=kartik)

sifre = khsec + bhsec + sysec + dgsec + artik

random.shuffle(sifre)

sifre = "".join(sifre)

if istimestamp and adet > 20:
    sifre = sifre + ts

if istimestamp and adet<=20:
    st.warning("Timestamp kullanabilmek için 20den fazla karakter seçmelisiniz")

st.title(sifre)