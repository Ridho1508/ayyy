import base64
import datetime
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Untuk bb 🧸", page_icon="🧸", layout="centered")

# ---------- GANTI BAGIAN INI ----------
NAMA_DIA = "Ressy Awalina Agustian"
PANGGILAN = "ayyy 🧸"
NAMA_KAMU = "idoooo" 
TANGGAL_JADIAN = datetime.date(2026, 8, 9)          # <- ganti dengan namamu             
# --------------------------------------

IMG = Path(__file__).parent / "images"


@st.cache_data
def data_uri(nama_file: str) -> str:
    b64 = base64.b64encode((IMG / nama_file).read_bytes()).decode()
    return f"data:image/jpeg;base64,{b64}"


# ---------- STYLE (background foto + overlay pink) ----------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:
            linear-gradient(rgba(255,235,242,0.86), rgba(255,244,248,0.88)),
            url("{data_uri('background_kolase.jpg')}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{ background: transparent; }}
    h1, h2, h3 {{ color: #b03a62 !important; text-align: center; }}
    .kartu {{
        background: rgba(255,255,255,0.90);
        border-radius: 20px;
        padding: 1.6rem 1.8rem;
        box-shadow: 0 6px 20px rgba(176,58,98,0.15);
        line-height: 1.85;
        font-size: 1.05rem;
        color: #4a2b36;
        margin-bottom: 1rem;
    }}
    .besar {{ font-size: 3.5rem; text-align: center; }}
    .ttd {{ text-align: right; font-style: italic; color: #b03a62; }}
    [data-testid="stImage"] img {{ border-radius: 16px; box-shadow: 0 4px 14px rgba(0,0,0,0.25); }}
    </style>
    """,
    unsafe_allow_html=True,
)


def kartu(teks: str):
    st.markdown(f'<div class="kartu">{teks}</div>', unsafe_allow_html=True)


# ---------- GERBANG MASUK ----------
if "masuk" not in st.session_state:
    st.session_state.masuk = False

if not st.session_state.masuk:
    st.markdown('<div class="besar">🧸💌</div>', unsafe_allow_html=True)
    st.title(f"alooo ayyy")
    st.image(str(IMG / "foto_b2.jpg"), use_container_width=True)
    kartu("Ada sesuatu yang aku buat khusus buat kamu. Baca yaa 🤍")
    if st.button("Buka dong ✨", use_container_width=True):
        st.session_state.masuk = True
        st.balloons()
        st.rerun()
    st.stop()

# ---------- NAVIGASI ----------
st.sidebar.title("🧸 Untuk bb")
halaman = st.sidebar.radio(
    "Pilih halaman",
    ["💌 Terima kasih", "🥺Maaf ayy", "🤍 Janji aku", "📸 Kenangan", "🌙 Selamanya"],
)

if TANGGAL_JADIAN:
    hari = (datetime.date.today() - TANGGAL_JADIAN).days
    st.sidebar.metric("Hari bersama kamu", f"{hari} hari")

# ---------- HALAMAN ----------
if halaman == "💌 Terima kasih":
    st.markdown('<div class="besar">💌</div>', unsafe_allow_html=True)
    st.title("Terima kasih, bb")
    kartu(
        "Terima kasih karena sudah jadi kamu.<br><br>"
        "Pas sama kamu, ada hal hal baru yang aku rasain "
        "Salah satu contohnya, mirip krong ."
    )
    st.image(str(IMG / "foto_a1.jpg"), use_container_width=True)
    kartu(
        "Aku tahu kamu sering marah-marah, tapi aku juga tahu di balik itu kamu "
        "gengsi buat nunjukin kalau kamu sayang. Dan kamu sebenarnya cuma pengen dimanja, kan? 🥺<br><br>"
        "Tenang, aku ngerti kok. Justru itu yang bikin kamu lucu dan bikin aku makin sayang."
    )
    if st.button("Klik kalau kamu senyum 😊"):
        st.toast("Yes, berhasil bikin bb senyum! 🧸", icon="🤍")
        st.balloons()

elif halaman == "🥺Maaf ayy":
    st.markdown('<div class="besar">🥺</div>', unsafe_allow_html=True)
    st.title("Aku mau minta maaf")
    kartu(
        "Maaf ya, ayy.<br><br>"
        "Maaf kalau aku belum bisa kasih kamu hal-hal baru dan kesan baru seperti yang "
        "kamu rasain ke aku. Aku sadar, mungkin aku belum sehebat itu."
    )
    st.image(str(IMG / "foto_a2.jpg"), use_container_width=True)
    kartu(
        "Tapi satu hal yang aku tahu: aku akan terus berusaha jadi yang terbaik buat kamu "
        "di segala aspek. Mungkin bukan dengan hal yang selalu baru, tapi ini caraku "
        "mencintai kamu, dan mencintai hubungan kita."
    )

elif halaman == "🤍 Janji aku":
    st.markdown('<div class="besar">🤍</div>', unsafe_allow_html=True)
    st.title("Janji kecil dari aku")
    janji = [
        "Aku bakal sabar waktu kamu lagi marah-marah 😌",
        "Aku bakal terus berusaha jadi lebih baik, buat kamu",
    ]
    isi = "".join(f" {j}<br>" for j in janji)
    kartu(isi)
    st.image(str(IMG / "foto_b3.jpg"), use_container_width=True)
    kartu("Janji ini mungkin sederhana, tapi semuanya datang dari hati yang tulus. 🤍")

elif halaman == "📸 Kenangan":
    st.markdown('<div class="besar">📸</div>', unsafe_allow_html=True)
    st.title("Kenangan kita")
    kartu("Beberapa momen yang bikin aku senyum tiap kali lihat ulang. 🧸")
    daftar = [
        ("foto_a1.jpg", "Awal yang manis"),
        ("foto_b1.jpg", "Kamu yang paling cantik"),
        ("foto_a2.jpg", "Pipi kamu yang gemesin"),
        ("foto_b2.jpg", "Dipeluk dan dimanja"),
        ("foto_a3.jpg", "Ekspresi ngambek kamu"),
        ("foto_b3.jpg", "Favorit aku"),
        ("foto_a4.jpg", "Gaya kita berdua"),
        ("foto_b4.jpg", "Kita yang paling konyol"),
    ]
    kolom = st.columns(2)
    for i, (file, teks) in enumerate(daftar):
        with kolom[i % 2]:
            st.image(str(IMG / file), caption=teks, use_container_width=True)

elif halaman == "🌙 Selamanya":
    st.markdown('<div class="besar">🌙</div>', unsafe_allow_html=True)
    st.title("Aku bersyukur punya kamu")
    st.image(str(IMG / "foto_b4.jpg"), use_container_width=True)
    kartu(
        f"{PANGGILAN}, aku bersyukur banget punya kamu di hidupku sekarang.<br><br>"
        "Dan yang paling aku pengen: <b>selamanya</b>. Bukan cuma sementara. "
        "Aku pengen terus jalan bareng kamu, dalam susah dan senang, dalam marah dan manja 🧸"
        f'<p class="ttd">Dari yang sayang kamu,<br>{NAMA_KAMU} 🤍</p>'
    )
    st.subheader("Satu pertanyaan terakhir...")
    pilihan = st.radio(
        "Mau jalan bareng aku selamanya?",
        ["Pilih dulu...", "Mau 🥰", "Mau banget 🧸"],
        index=0,
    )
    if pilihan != "Pilih dulu...":
        st.success("Yeay! Aku sayang kamu, bb 🤍")
        st.snow()
