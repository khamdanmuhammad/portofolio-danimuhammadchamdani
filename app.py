import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Muhammad Chamdani - Portofolio",
    page_icon="👨‍💻",
    layout="wide",
)

# Custom CSS untuk tampilan lebih menarik
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        background-color: #ff4b4b;
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HEADER / PROFIL ---
st.write("#")
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # Menampilkan foto profil yang Anda unggah
    st.image(
        "image_2.png", # Menggunakan file gambar yang Anda berikan
        caption="Muhammad Chamdani",
        use_container_width=True,
    )

with col2:
    st.title("Muhammad Chamdani (Dani)")
    st.subheader(
        "Lulusan S1 Teknik Informatika | Web Developer & Digital Creator"
    )
    st.write(
        "📍 **Domisili:** Wonosobo, Jawa Tengah (Asal: Pekalongan)\n\n"
        "Halo! Saya seorang lulusan Teknik Informatika Universitas Sains Al-Qur'an (UNSIQ) Wonosobo. "
        "Memiliki kombinasi unik antara keahlian teknis di bidang pengembangan web/analisis data dan pengalaman kerja di sektor pelayanan serta ritel. "
        "Siap memberikan dedikasi tinggi untuk setiap proyek profesional."
    )
    st.markdown(
        "[🔗 Kunjungi Toko Shopee Affiliate Saya](https://collshp.com/mcproduction88)"
    )

st.markdown("---")

# --- PENGALAMAN KERJA ---
st.header("💼 Pengalaman Kerja")

col_exp1, col_exp2 = st.columns(2)

with col_exp1:
    st.markdown(
        """
    ### 🛒 Pramuniaga Karpet
    **AB Central Wonosobo**
    * Melayani pelanggan dalam pemilihan produk karpet terbaik.
    * Mengelola penataan dan inventaris barang di toko.
    * Memberikan pelayanan ramah untuk meningkatkan kepuasan pelanggan.
    """
    )

with col_exp2:
    st.markdown(
        """
    ### 🍽️ Waiters
    **Rumah Makan Lesehan Puyuh Wonosobo**
    * Bertanggung jawab atas pelayanan pesanan tamu secara cepat dan akurat.
    * Menjaga kebersihan area makan dan kenyamanan pengunjung.
    * Berkomunikasi aktif untuk memastikan pelayanan yang prima.
    """
    )

st.markdown("---")

# --- PORTOFOLIO & PROYEK ---
st.header("🚀 Proyek & Portofolio Unggulan")

col_proj1, col_proj2 = st.columns(2)

with col_proj1:
    st.markdown("### 📊 Web Analisis Sentimen Akulaku")
    st.write(
        "Aplikasi berbasis web untuk menganalisis sentimen ulasan pengguna terhadap layanan Akulaku menggunakan teknik Data Mining dan Machine Learning."
    )
    st.markdown(
        "[🔗 Buka Aplikasi Streamlit](https://muhammad-sentimen-akulaku-e9zkg4wz6wc8ygxkizekst.streamlit.app/)"
    )

with col_proj2:
    st.markdown("### 🕌 Website Pondok Pesantren")
    st.write(
        "Pengembangan platform informasi profil dan kegiatan Pondok Pesantren Al-Munir untuk memudahkan akses informasi masyarakat."
    )
    st.markdown(
        "[🔗 Kunjungi Website PP Al-Munir](https://ppalmunir.infinityfreeapp.com/)"
    )

st.markdown("---")

# --- PENDIDIKAN ---
st.header("🎓 Pendidikan")
st.markdown(
    """
### **Universitas Sains Al-Qur'an (UNSIQ) Wonosobo**
* **Jenjang:** Strata 1 (S1)
* **Program Studi:** Teknik Informatika
* **Keahlian:** Pemrograman Web, Analisis Data, Desain Grafis, & Manajemen Sistem.
"""
)

st.markdown("---")

# --- KONTAK ---
st.header("📬 Hubungi Saya")
st.write("Tertarik berkolaborasi atau ingin mengenal saya lebih lanjut? Silakan hubungi melalui:")
st.markdown(
    f"""
* 📧 **Email:** muhammadchamdani34@gmail.com
* 📱 **WhatsApp / Telepon:** 082226238706
* 🌐 **GitHub:** [github.com/khamdanmuhammad](https://github.com/khamdanmuhammad)
"""
)
