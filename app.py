import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Muhammad Chamdani - Portofolio Digital",
    page_icon="👨‍💻",
    layout="wide",
)

# Custom CSS untuk tampilan Dark Mode yang Estetik & Modern
st.markdown(
    """
    <style>
    /* Styling Latar Belakang Utama (Dark Theme) */
    .stApp {
        background-color: #0e1117;
        color: #f3f4f6;
    }

    /* Styling Judul Utama */
    h1.main-title {
        color: #60a5fa;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
    }
    
    /* Styling Sub-Judul */
    h3.sub-title {
        color: #93c5fd;
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }

    /* Styling Tombol */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #f59e0b; /* Aksen Gold/Oranye */
        color: #0e1117;
        font-weight: 700;
        padding: 0.75rem 1rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #d97706;
        color: white;
    }

    /* Styling Kartu Konten (Card Dark Mode) */
    .card {
        padding: 25px;
        border-radius: 15px;
        background-color: #1f2937;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        border: 1px solid #374151;
        color: #f3f4f6;
    }
    
    .card h3, .card p, .card li {
        color: #f3f4f6 !important;
    }

    /* Typography Header Bagian */
    .section-header {
        color: #60a5fa;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #374151;
        padding-bottom: 0.5rem;
    }

    /* Link styling */
    a {
        color: #60a5fa !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    
    /* Responsivitas untuk Mobile */
    @media (max-width: 768px) {
        h1.main-title { font-size: 2rem; }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MENU NAVIGASI SIDEBAR ---
st.sidebar.markdown("## 🧭 Navigasi Menu")
selected_menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Dashboard", "👤 About Me", "🚀 Portofolio & Pengalaman", "📬 Kontak"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tips:** Gunakan menu di atas untuk menjelajahi portofolio Muhammad Chamdani.")


# ==========================================
# 1. MENU DASHBOARD (HALAMAN UTAMA)
# ==========================================
if selected_menu == "🏠 Dashboard":
    prof_col1, prof_col2 = st.columns([1, 1.5], gap="large")

    with prof_col1:
        try:
            st.image("file_0000000009247208b1c50a03e0175858.png", caption="Muhammad Chamdani", use_container_width=True)
        except Exception as e:
            st.warning("Foto profil gagal dimuat. Menggunakan gambar placeholder.")
            st.image(
                "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400",
                caption="Muhammad Chamdani",
                use_container_width=True,
            )

    with prof_col2:
        st.markdown('<h1 class="main-title">Muhammad Chamdani (Dani)</h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="sub-title">Lulusan S1 Teknik Informatika | Web Developer & Digital Creator</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            📍 **Domisili:** Wonosobo, Jawa Tengah (Asal: Pekalongan)  
            
            Halo! Selamat datang di portofolio digital saya. Platform ini merangkum perjalanan profesional, keahlian teknis, serta proyek-proyek unggulan yang telah saya kembangkan. Silakan gunakan menu navigasi di sebelah kiri untuk melihat detail informasi lainnya.
            """
        )
        st.markdown(
            "[🔗 Kunjungi Toko Shopee Affiliate Saya](https://collshp.com/mcproduction88)"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">✨ Sekilas Ringkasan</h2>', unsafe_allow_html=True)
    
    dash_col1, dash_col2, dash_col3 = st.columns(3)
    with dash_col1:
        st.markdown('<div class="card"><h3>🎓 Pendidikan</h3><p>S1 Teknik Informatika<br>UNSIQ Wonosobo</p></div>', unsafe_allow_html=True)
    with dash_col2:
        st.markdown('<div class="card"><h3>🚀 Proyek</h3><p>Web Analisis Sentimen & Website Pesantren</p></div>', unsafe_allow_html=True)
    with dash_col3:
        st.markdown('<div class="card"><h3>💼 Pengalaman</h3><p>Ritel, Pelayanan, & Pengembangan Web</p></div>', unsafe_allow_html=True)


# ==========================================
# 2. MENU ABOUT (TENTANG SAYA & PENDIDIKAN)
# ==========================================
elif selected_menu == "👤 About Me":
    st.markdown('<h2 class="section-header">👤 Tentang Saya</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns([1.5, 1], gap="large")
    with about_col1:
        st.markdown(
            """
            <div class="card">
            <p>Halo! Saya seorang lulusan <strong>Teknik Informatika Universitas Sains Al-Qur'an (UNSIQ) Wonosobo</strong>. 
            Saya memiliki kombinasi unik antara keahlian teknis di bidang pengembangan web/analisis data dan pengalaman kerja di sektor pelayanan serta ritel.</p>
            <p>Dengan latar belakang tersebut, saya terbiasa bekerja secara teliti, komunikatif, dan memiliki dedikasi tinggi untuk memberikan solusi terbaik dalam setiap proyek profesional yang saya jalankan.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with about_col2:
        try:
            st.image("file_0000000009247208b1c50a03e0175858.png", caption="Muhammad Chamdani", use_container_width=True)
        except:
            pass

    st.markdown('<h2 class="section-header">🎓 Pendidikan</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        <h3><strong>Universitas Sains Al-Qur'an (UNSIQ) Wonosobo</strong></h3>
        <p><strong>Jenjang:</strong> Strata 1 (S1)</p>
        <p><strong>Program Studi:</strong> Teknik Informatika</p>
        <p><strong>Keahlian:</strong> Pemrograman Web, Analisis Data, Desain Grafis, & Manajemen Sistem.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# 3. MENU PORTOFOLIO & PENGALAMAN
# ==========================================
elif selected_menu == "🚀 Portofolio & Pengalaman":
    st.markdown('<h2 class="section-header">🚀 Proyek & Portofolio Unggulan</h2>', unsafe_allow_html=True)

    col_proj1, col_proj2 = st.columns(2, gap="medium")

    with col_proj1:
        st.markdown(
            """
            <div class="card">
            <h3>📊 Web Analisis Sentimen Akulaku</h3>
            <p>Aplikasi berbasis web untuk menganalisis sentimen ulasan pengguna terhadap layanan Akulaku menggunakan teknik Data Mining dan Machine Learning.</p>
            <p><a href="https://muhammad-sentimen-akulaku-e9zkg4wz6wc8ygxkizekst.streamlit.app/" target="_blank">[🔗 Buka Aplikasi Streamlit]</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_proj2:
        st.markdown(
            """
            <div class="card">
            <h3>🕌 Website Pondok Pesantren</h3>
            <p>Pengembangan platform informasi profil dan kegiatan Pondok Pesantren Al-Munir untuk memudahkan akses informasi masyarakat.</p>
            <p><a href="https://ppalmunir.infinityfreeapp.com/" target="_blank">[🔗 Kunjungi Website PP Al-Munir]</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<h2 class="section-header">💼 Pengalaman Kerja</h2>', unsafe_allow_html=True)

    col_exp1, col_exp2 = st.columns(2, gap="medium")

    with col_exp1:
        st.markdown(
            """
            <div class="card">
            <h3>🛒 Pramuniaga Karpet</h3>
            <p><strong>AB Central Wonosobo</strong></p>
            <ul>
                <li>Melayani pelanggan dalam pemilihan produk karpet terbaik.</li>
                <li>Mengelola penataan dan inventaris barang di toko.</li>
                <li>Memberikan pelayanan ramah untuk meningkatkan kepuasan pelanggan.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_exp2:
        st.markdown(
            """
            <div class="card">
            <h3>🍽️ Waiters</h3>
            <p><strong>Rumah Makan Lesehan Puyuh Wonosobo</strong></p>
            <ul>
                <li>Bertanggung jawab atas pelayanan pesanan tamu secara cepat dan akurat.</li>
                <li>Menjaga kebersihan area makan dan kenyamanan pengunjung.</li>
                <li>Berkomunikasi aktif untuk memastikan pelayanan yang prima.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# 4. MENU KONTAK
# ==========================================
elif selected_menu == "📬 Kontak":
    st.markdown('<h2 class="section-header">📬 Hubungi Saya</h2>', unsafe_allow_html=True)
    st.write("Tertarik berkolaborasi atau ingin mengenal saya lebih lanjut? Silakan hubungi melalui:")
    st.markdown(
        """
        <div class="card">
        <p>📧 <strong>Email:</strong> muhammadchamdani34@gmail.com</p>
        <p>📱 <strong>WhatsApp / Telepon:</strong> 082226238706</p>
        <p>🌐 <strong>GitHub:</strong> <a href="https://github.com/khamdanmuhammad" target="_blank">github.com/khamdanmuhammad</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
