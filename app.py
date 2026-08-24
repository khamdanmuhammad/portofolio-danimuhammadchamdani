import streamlit as st
import os

# Konfigurasi Halaman
st.set_page_config(
    page_title="Muhammad Chamdani - Web Engineer Portofolio",
    page_icon="⚡",
    layout="wide",
)

# Custom CSS untuk tampilan Web Engineer Dark Mode yang Estetik & Modern
st.markdown(
    """
    <style>
    /* Styling Latar Belakang Utama (Dark Theme Engineer Style) */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Styling Judul Utama */
    h1.main-title {
        color: #38bdf8;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
        letter-spacing: -0.025em;
    }
    
    /* Styling Sub-Judul */
    h3.sub-title {
        color: #818cf8;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        font-family: monospace;
    }

    /* Styling Tombol */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #38bdf8; /* Aksen Cyan Engineer */
        color: #0b0f19;
        font-weight: 700;
        padding: 0.75rem 1rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0ea5e9;
        color: white;
    }

    /* Styling Kartu Konten (Card Dark Mode ala Terminal/Editor) */
    .card {
        padding: 24px;
        border-radius: 12px;
        background-color: #1e293b;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
        border: 1px solid #334155;
        color: #e2e8f0;
    }
    
    .card h3, .card p, .card li {
        color: #e2e8f0 !important;
    }

    /* Typography Header Bagian */
    .section-header {
        color: #38bdf8;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #1e293b;
        padding-bottom: 0.5rem;
        font-family: monospace;
    }

    /* Link styling */
    a {
        color: #38bdf8 !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    
    /* Code badge style */
    .code-badge {
        background-color: #0f172a;
        color: #38bdf8;
        padding: 2px 8px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 0.9em;
        border: 1px solid #334155;
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
st.sidebar.markdown("## ⚡ SYSTEM_NAV")
selected_menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Dashboard", "👨‍💻 About Me", "🚀 Portofolio & Pengalaman", "📄 Curriculum Vitae", "📬 Kontak"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Engineer Note:** Gunakan panel navigasi di atas untuk mengakses modul portofolio Muhammad Chamdani.")


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
                caption="Muhammad Chamdani S.Kom",
                use_container_width=True,
            )

    with prof_col2:
        st.markdown('<h1 class="main-title">Muhammad Chamdani (Dani)</h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="sub-title">> S1 Teknik Informatika | Web Engineer & Digital Creator</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            📍 **Domisili:** Wonosobo, Jawa Tengah <span class="code-badge">Asal: Pekalongan</span>  
            
            Halo! Selamat datang di portofolio sistem digital saya. Dirancang dengan arsitektur bersih ala *web engineering*, platform ini merangkum kapabilitas teknis, rekam jejak profesional, serta deployment proyek riil. Silakan jelajahi modul melalui navigasi sidebar.
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            "[🔗 Kunjungi Toko Shopee Affiliate Saya](https://collshp.com/mcproduction88)"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">// SYSTEM_OVERVIEW</h2>', unsafe_allow_html=True)
    
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
elif selected_menu == "👨‍💻 About Me":
    st.markdown('<h2 class="section-header">// ABOUT_DEVELOPER</h2>', unsafe_allow_html=True)
    
    about_col1, about_col2 = st.columns([1.5, 1], gap="large")
    with about_col1:
        st.markdown(
            """
            <div class="card">
            <p>Halo! Saya seorang lulusan <strong>Teknik Informatika Universitas Sains Al-Qur'an (UNSIQ) Wonosobo</strong>. 
            Saya memiliki kombinasi unik antara keahlian teknis mendalam di bidang pengembangan web, analitik data, sistem IoT, dan pengalaman nyata di sektor profesional.</p>
            <p>Sebagai seorang engineer, saya terbiasa menulis kode yang bersih, berpikir analitis dalam memecahkan masalah, serta memiliki komunikasi yang adaptif untuk berkolaborasi dalam tim maupun pelayanan klien.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with about_col2:
        try:
            st.image("file_0000000009247208b1c50a03e0175858.png", caption="Muhammad Chamdani S.Kom", use_container_width=True)
        except:
            pass

    st.markdown('<h2 class="section-header">// ACADEMIC_BACKGROUND</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        <h3><strong>Universitas Sains Al-Qur'an (UNSIQ) Wonosobo</strong></h3>
        <p><strong>Jenjang:</strong> Strata 1 (S1)</p>
        <p><strong>Program Studi:</strong> Teknik Informatika</p>
        <p><strong>Core Stack / Keahlian:</strong> Web Development, PHP, Java, Data Analysis, UI Design, IoT (ESP32), Microsoft Office, & Problem Solving.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# 3. MENU PORTOFOLIO & PENGALAMAN
# ==========================================
elif selected_menu == "🚀 Portofolio & Pengalaman":
    st.markdown('<h2 class="section-header">// FEATURED_PROJECTS</h2>', unsafe_allow_html=True)

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
            <p>Pengembangan platform informasi profil dan kegiatan Pondok Pesantren Al-Munir untuk memudahkan akses informasi masyarakat secara digital.</p>
            <p><a href="https://ppalmunir.infinityfreeapp.com/" target="_blank">[🔗 Kunjungi Website PP Al-Munir]</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<h2 class="section-header">// PROFESSIONAL_EXPERIENCE</h2>', unsafe_allow_html=True)

    col_exp1, col_exp2 = st.columns(2, gap="medium")

    with col_exp1:
        st.markdown(
            """
            <div class="card">
            <h3>🛒 Pramuniaga Karpet Permadani</h3>
            <p><strong>CV. Arta Berkah Pitulungan (Wonosobo)</strong></p>
            <ul>
                <li>Melayani pelanggan dalam memilih produk karpet sesuai kebutuhan.</li>
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
            <h3>🍽️ Pramusaji / Waiters</h3>
            <p><strong>Rumah Makan Lesehan Puyuh Wonosobo</strong></p>
            <ul>
                <li>Memberikan pelayanan kepada pelanggan dan membantu operasional pelayanan restoran.</li>
                <li>Menjaga kebersihan area makan dan kenyamanan pengunjung.</li>
                <li>Berkomunikasi aktif untuk memastikan pelayanan yang prima.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# 4. MENU CURRICULUM VITAE (CV)
# ==========================================
elif selected_menu == "📄 Curriculum Vitae":
    st.markdown('<h2 class="section-header">// CURRICULUM_VITAE</h2>', unsafe_allow_html=True)
    st.write("Berikut adalah dokumen Curriculum Vitae (CV) profesional saya. Anda dapat melihat pratinjau langsung di bawah atau mengunduhnya melalui tombol yang tersedia.")

    cv_file_path = "CV_ATS_Muhammad_Chamdani.pdf"

    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        col_cv1, col_cv2 = st.columns([1, 1], gap="medium")
        
        with col_cv1:
            st.download_button(
                label="📥 Unduh CV (PDF)",
                data=PDFbyte,
                file_name="CV_ATS_Muhammad_Chamdani.pdf",
                mime="application/octet-stream"
            )
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Pratinjau PDF menggunakan iframe HTML
        import base64
        base64_pdf = base64.b64encode(PDFbyte).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" type="application/pdf" style="border-radius: 12px; border: 1px solid #334155;"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ File PDF CV (`CV_ATS_Muhammad_Chamdani.pdf`) belum ditemukan pada direktori sistem. Pastikan file sudah diletakkan di folder yang sama dengan skrip aplikasi.")


# ==========================================
# 5. MENU KONTAK
# ==========================================
elif selected_menu == "📬 Kontak":
    st.markdown('<h2 class="section-header">// CONTACT_CHANNELS</h2>', unsafe_allow_html=True)
    st.write("Tertarik berkolaborasi, mendiskusikan proyek teknologi, atau merekrut saya? Silakan hubungi melalui kanal di bawah ini:")
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
