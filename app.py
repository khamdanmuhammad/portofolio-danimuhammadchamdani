import streamlit as st
import os
import base64

# Konfigurasi Halaman
st.set_page_config(
    page_title="Muhammad Chamdani - Web Engineer Portofolio",
    page_icon="⚡",
    layout="wide",
)

# Custom CSS untuk Navigasi Estetik & Tampilan Web Engineer Dark Mode
st.markdown(
    """
    <style>
    /* Global Background & Font */
    .stApp {
        background-color: #0c1017;
        color: #cbd5e1;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ==========================================================
       STYLING SIDEBAR & MENU NAVIGASI YANG ESTETIK & BERWARNA
       ========================================================== */
    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }

    /* Sembunyikan radio button bawaan streamlit agar bisa di-styling via label */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 8px;
    }

    [data-testid="stSidebar"] .stRadio label {
        background-color: #162032;
        border: 1px solid #1f2937;
        border-radius: 10px;
        padding: 10px 14px;
        color: #94a3b8 !important;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background-color: #1e293b;
        color: #22d3ee !important;
        border-color: #06b6d4;
        transform: translateX(4px);
    }

    /* Header Navigasi di Sidebar */
    .sidebar-header {
        background: linear-gradient(135deg, #0891b2 0%, #06b6d4 100%);
        color: #0c1017;
        padding: 12px 16px;
        border-radius: 10px;
        font-weight: 800;
        font-family: monospace;
        letter-spacing: 1px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
    }

    /* Typography Judul Utama */
    h1.main-title {
        color: #ffffff;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
        letter-spacing: -0.025em;
    }
    
    /* Typography Sub-Judul */
    h3.sub-title {
        color: #22d3ee;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 1rem;
        font-family: monospace;
    }

    /* Styling Tombol Utama */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #06b6d4;
        color: #0c1017;
        font-weight: 700;
        padding: 0.75rem 1rem;
        border: none;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #22d3ee;
        color: #0c1017;
        box-shadow: 0 0 25px rgba(34, 211, 238, 0.6);
    }

    /* Styling Kartu Konten */
    .card {
        padding: 24px;
        border-radius: 14px;
        background-color: #131b2e;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        border: 1px solid #1e293b;
        color: #cbd5e1;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .card:hover {
        border-color: #06b6d4;
    }
    
    .card h3, .card p, .card li {
        color: #cbd5e1 !important;
    }
    .card h3 {
        color: #f8fafc !important;
    }

    /* Typography Header Bagian */
    .section-header {
        color: #22d3ee;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #1e293b;
        padding-bottom: 0.5rem;
        font-family: monospace;
        letter-spacing: 1px;
    }

    /* Link styling */
    a {
        color: #22d3ee !important;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    
    /* Code badge style */
    .code-badge {
        background-color: #0f172a;
        color: #22d3ee;
        padding: 2px 8px;
        border-radius: 4px;
        font-family: monospace;
        font-size: 0.9em;
        border: 1px solid #1e293b;
    }

    /* Responsivitas Mobile */
    @media (max-width: 768px) {
        h1.main-title { font-size: 2rem; }
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- MENU NAVIGASI SIDEBAR YANG ESTETIK ---
st.sidebar.markdown('<div class="sidebar-header">⚡ SYSTEM_NAVIGATOR</div>', unsafe_allow_html=True)

selected_menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Dashboard", "👨‍💻 About Me", "🚀 Portofolio & Pengalaman", "📄 Curriculum Vitae", "📬 Kontak"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Engineer UI:** Navigasi aktif dengan sistem tema warna gelap terintegrasi.")


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
        st.markdown('<h1 class="main-title">Hello, It\'s Me<br><span style="color: #22d3ee;">Muhammad Chamdani</span></h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="sub-title">And I\'m a Web Engineer & Digital Creator</h3>', unsafe_allow_html=True)
        st.markdown(
            """
            📍 **Domisili:** Wonosobo, Jawa Tengah <span class="code-badge">Asal: Pekalongan</span>  
            
            Selamat datang di portofolio digital berbasis arsitektur *cyber-dark UI*. Platform ini mendokumentasikan kapabilitas teknis, rekam jejak pengembangan sistem, serta proyek-proyek inovatif yang telah saya selesaikan.
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
            <h3>About Me</h3>
            <p>Halo! Saya seorang lulusan <strong>Teknik Informatika Universitas Sains Al-Qur'an (UNSIQ) Wonosobo</strong>. 
            Saya memiliki spesialisasi dalam merancang aplikasi web yang responsif, analitik data, implementasi sistem IoT, serta memiliki dedikasi tinggi pada standar kualitas kode yang bersih.</p>
            <p>Berbekal pengalaman lintas industri baik di bidang teknologi maupun pelayanan profesional, saya terbiasa menghadirkan solusi fungsional yang berorientasi pada kepuasan pengguna akhir.</p>
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
    st.write("Berikut adalah dokumen Curriculum Vitae (CV) profesional saya. Anda dapat melihat pratinjau langsung di bawah atau mengunduhnya melalui tombol aksi.")

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
        
        # Pratinjau PDF interaktif
        base64_pdf = base64.b64encode(PDFbyte).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" type="application/pdf" style="border-radius: 12px; border: 1px solid #1e293b;"></iframe>'
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
        <h3>Contact Me!</h3>
        <p>📧 <strong>Email:</strong> muhammadchamdani34@gmail.com</p>
        <p>📱 <strong>WhatsApp / Telepon:</strong> 082226238706</p>
        <p>🌐 <strong>GitHub:</strong> <a href="https://github.com/khamdanmuhammad" target="_blank">github.com/khamdanmuhammad</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )
