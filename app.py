import streamlit as st
from PIL import Image
import base64
import os

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Portfolio | Reydiko Fakhran Haidi", page_icon="💼", layout="wide")

# --- Gaya CSS Kustom ---
st.markdown("""
    <style>
        .big-font {
            font-size:50px !important;
            color: #1ABC9C;
        }
        .small-font {
            font-size:18px !important;
            color: #1F618D;
        }
        .skill-bar {
            background-color: #D6EAF8;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1,3])
with col1:
    img = Image.open("foto_profil.jpg")
    st.image(img, width=200)
with col2:
    st.markdown('<p class="big-font">Reydiko Fakhran Haidi</p>', unsafe_allow_html=True)
    st.markdown("**AI Engineer | Machine Learning Engineer | Data Analyst**")
    st.write("""
Fresh Graduate jurusan Sains Data Terapan di Politeknik Elektronika Negeri Surabaya (PENS) | AI/ML/CV Engineer dan Data Analyst Enthusiast.
""")

st.write("---")

# --- About Me ---
st.header("👨‍💻 Tentang Saya")
st.write("""
Halo Semuanya! Nama saya Reydiko Fakhran Haidi, Fresh Graduate jurusan Sains Data Terapan di Politeknik Elektronika Negeri Surabaya (PENS).
Saya memiliki satu tahun pengalaman kerja sebagai Machine Learning Engineer Intern di PDAM Surya Sembada Surabaya selama 6 bulan dan Telkom Indonesia selama 6 bulan.
Minat saya terletak pada Machine Learning, Artificial Intelligence, Computer Vision, dan Analisis Data.

Sepanjang perjalanan akademis dan profesional saya, saya telah mengembangkan dan menerapkan berbagai model pembelajaran mesin (ML) termasuk sistem NLP,
segmentasi gambar, klasifikasi, dan deteksi objek. Saya memiliki spesialisasi dalam membangun solusi menyeluruh dan mengintegrasikan model ML ke dalam aplikasi
dunia nyata menggunakan layanan API.
""")

st.write("---")

# --- Konfigurasi Halaman ---
st.header("🛠 Skills")

# --- Data Skill Terstruktur ---
skills_grouped = {
    "Database": [
        ("skills/mysql.png", "MySQL", "85%"),
        ("skills/postgresql.png", "PostgreSQL", "80%"),
        ("skills/chromadb.png", "ChromaDB", "90%")
    ],
    "Bahasa Pemrograman": [
        ("skills/python.png", "Python", "95%"),
        ("skills/sql.png", "SQL", "75%"),
        ("skills/javascript.png", "JavaScript", "50%"),
    ],
    "Web Development": {
        "BackEnd Frameworks": [
            ("skills/flask.png", "Flask", "85%"),
            ("skills/fastapi.png", "FastAPI", "85%"),
            ("skills/django.png", "Django", "80%"),
        ],
        "FrontEnd Frameworks": [
            ("skills/html.png", "HTML", "70%"),
            ("skills/css.png", "CSS", "70%"),
            ("skills/streamlit.png", "Streamlit", "85%"),
            ("skills/reactjs.png", "ReactJS", "70%"),
        ]
    },
    "Data Science / Machine Learning": [
        ("skills/pandas.png", "Pandas", "95%"),
        ("skills/numpy.png", "NumPy", "95%"),
        ("skills/scikitlearn.png", "Scikit-Learn", "95%"),
        ("skills/opencv.png", "OpenCV", "90%"),
        ("skills/tensorflow.png", "TensorFlow", "95%"),
        ("skills/pytorch.png", "PyTorch", "95%"),
    ],
    "Tools": {
        "Analytics Tools": [
            ("skills/excel.png", "Excel", "80%"),
            ("skills/powerbi.png", "PowerBI", "95%"),
            ("skills/looker.png", "Looker Studio", "90%"),
            ("skills/tableau.png", "Tableau", "80%"),
        ],
        "Annotation Tools": [
            ("skills/labelstudio.png", "Label Studio", "95%"),
            ("skills/cvat.png", "CVAT", "95%"),
            ("skills/roboflow.png", "Roboflow", "95%"),
        ],
        "NLP/LLM Development Tools": [
            ("skills/huggingface.png", "HuggingFace", "95%"),
            ("skills/langchain.png", "LangChain", "95%"),
            ("skills/w&b.png", "Weights & Biases", "95%"),
            ("skills/openai.png", "Open AI API", "95%"),
        ]
    }
}

st.markdown("""
<style>
/* Default: Desktop / layar lebar */
.row-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 100px;  /* 🔹 jarak horizontal antar kategori lebih besar */
    flex-wrap: wrap;
    margin-bottom: 80px; /* 🔹 jarak antar baris kategori */
}
.category-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    margin-bottom: 40px; /* 🔹 tambahkan jarak bawah antar kategori */
}

/* Grid logo */
.skills-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px; /* 🔹 jarak antar lingkaran */
    margin-bottom: 0px;
}
.skill-item {
    position: relative;
    width: 110px;
    height: 110px;
    border: 2px solid #1ABC9C;
    border-radius: 50%;
    overflow: hidden;
    transition: transform 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
}
.skill-item img {
    width: 70%;
    height: 70%;
    object-fit: contain;
}
.skill-item:hover { transform: scale(1.1); }

/* Overlay teks */
.skill-overlay {
    position: absolute;
    inset: 0;
    background-color: rgba(0,0,0,0.7);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8px;
    font-size: clamp(10px, 1.8vw, 14px);
    font-weight: bold;
    opacity: 0;
    transition: opacity 0.3s ease;
    border-radius: 50%;
    line-height: 1.3;
    word-break: break-word;
}
.skill-overlay span:first-child {
    font-size: clamp(13px, 2vw, 17px);
    margin-bottom: 5px;
}
.skill-item:hover .skill-overlay { opacity: 1; }

.category-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;  /* 🔹 ganti dari margin-top ke margin-bottom */
    color: var(--text-color);
}
.subcategory-title {
    font-size: 16px;
    font-weight: 600;
    margin-top: 10px;
    margin-bottom: 15px;
    color: var(--text-color);
}
.separator-row {
    border-top: 2px solid #eee;
    margin: 60px 0;
}

/* 🔹 Mobile Responsive (max 768px) */
@media (max-width: 768px) {
    .row-container {
        flex-direction: column;
        align-items: center;
        gap: 40px;
        margin-bottom: 60px;
    }
    .category-box {
        margin-bottom: 40px; /* 🔹 spacing lebih lega di HP */
    }
    .skills-grid {
        justify-content: center;
        gap: 20px;
    }
    .skill-item {
        width: 85px;
        height: 85px;
    }
    .skill-overlay {
        font-size: clamp(9px, 3vw, 12px);
        padding: 5px;
    }
    .category-title {
        font-size: 20px;
    }
    .subcategory-title {
        font-size: 15px;
    }
}
</style>
""", unsafe_allow_html=True)


# --- Fungsi Render Skill Grid ---
def render_skills(skills):
    html = '<div class="skills-grid">'
    for logo, name, percent in skills:
        try:
            with open(logo, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
            html += f"""
<div class="skill-item">
    <img src="data:image/png;base64,{encoded}" alt="{name}">
    <div class="skill-overlay">
        <span>{name}</span>
        <span>{percent}</span>
    </div>
</div>
"""
        except FileNotFoundError:
            st.error(f"File gambar '{logo}' tidak ditemukan.")
    html += "</div>"
    return html


# --- Render Horizontal Layout ---
html = '<div class="categories-container">'
for idx, (category, data) in enumerate(skills_grouped.items()):
    html += '<div class="category-box">'
    
    # 🟢 Judul kategori dipindah ke atas
    if isinstance(data, dict):  # Web Development dengan subkategori
        html += f"<div class='category-title'>{category}</div>"
        for subcat, skills in data.items():
            html += render_skills(skills)
            html += f"<div class='subcategory-title'>{subcat}</div>"
    else:  # Database, Bahasa Pemrograman, dll
        html += f"<div class='category-title'>{category}</div>"
        html += render_skills(data)
    
    html += '</div>'
    
    if idx < len(skills_grouped) - 1:
        html += '<div class="separator-vertical"></div>'
html += '</div>'

st.markdown(html, unsafe_allow_html=True)

st.write("---")

# --- Pengalaman ---
st.header("📂 Pengalaman")

def pengalaman_card(title, subtitle, items):
    with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: var(--secondary-background-color);
                border: 1px solid rgba(255,255,255,0.1);
                padding:15px; 
                border-radius:15px; 
                margin-bottom:15px; 
                box-shadow: 0px 2px 6px rgba(0,0,0,0.15);
            ">
                <h4 style="margin-bottom:5px; color: var(--text-color);">{title}</h4>
                <p style="color: var(--secondary-text-color); margin-top:0; margin-bottom:10px;">{subtitle}</p>
                <ul style="margin:0; padding-left:20px; color: var(--text-color);">
                    {''.join([f"<li>{item}</li>" for item in items])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# Telkom
pengalaman_card(
    "Machine Learning Engineer Intern — Telkom Indonesia",
    "Juli 2024 – Desember 2024",
    [
        "Membuat Chatbot Layanan Pelanggan di WhatsApp",
        "Membuat Dashboard Monitoring Transaksi Produk di Telkom Indonesia"
    ]
)

# PDAM
pengalaman_card(
    "Machine Learning Engineer Intern — PDAM Surya Sembada Surabaya",
    "Januari 2024 – Juli 2024",
    [
        "Membuat Generative AI berdasarkan database perusahaan untuk meningkatkan efisiensi dan efektivitas operasional"
    ]
)

# YDSF
pengalaman_card(
    "Data Analyst — Yayasan Dana Sosial Al-Falah Surabaya",
    "Juli 2023 – September 2023",
    [
        "Membaca dan menganalisis insight dari data (Dana Terhimpun dan Dana Tersalur)",
        "Membuat clustering data",
        "Membuat forecasting data",
        "Membuat dashboard analitik untuk dibagikan ke Yayasan Dana Sosial Al-Falah Surabaya"
    ]
)

st.write("---")

# --- Projects ---
st.header("🚀 Proyek")

# Fungsi kartu project
def project_card(
    title, subtitle, desc, items, 
    img_path="project_placeholder.png", 
    github_url="#", demo_url="#", 
    video_url=None, extra_img_path=None, 
    skills=None
):
    # CSS
    st.markdown(
        """
        <style>
        .skill-circle {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
            margin-right: 10px;
            cursor: pointer;
        }
        .skill-circle img {
            max-width: 35px;
            max-height: 35px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        col1, col2 = st.columns([1,2])
        with col1:
            if video_url:  
                if video_url.endswith(".mp4") and os.path.exists(video_url):
                    with open(video_url, "rb") as f:
                        video_bytes = f.read()
                    st.video(video_bytes)
                else:
                    st.video(video_url)
            else:  
                try:
                    img = Image.open(img_path)
                    st.image(img, use_column_width=True)
                except:
                    st.write("📷 [Tambahkan gambar di sini]")

        with col2:
            st.subheader(title)
            st.caption(subtitle)

            # 🔹 Skill icons in circle + hover tooltip
            if skills:
                skill_html = ""
                for skill in skills:
                    # Bisa tuple ("path", "nama") atau string biasa
                    if isinstance(skill, tuple):
                        icon, label = skill
                    else:
                        icon, label = skill, os.path.splitext(os.path.basename(skill))[0]

                    try:
                        with open(icon, "rb") as f:
                            data = f.read()
                        b64 = base64.b64encode(data).decode()
                        skill_html += f'<div class="skill-circle" title="{label}"><img src="data:image/png;base64,{b64}"></div>'
                    except:
                        skill_html += f'<div class="skill-circle" title="{label}">❓</div>'
                st.markdown(f"<div style='display:flex; gap:10px; margin-bottom:10px'>{skill_html}</div>", unsafe_allow_html=True)

            st.write(desc)
            st.markdown("**Kontribusi Utama:**")
            st.markdown("".join([f"- {item}\n" for item in items]))
            if demo_url != "#":
                st.markdown(f"[🚀 Demo Aplikasi]({demo_url})")

            if extra_img_path and os.path.exists(extra_img_path):
                st.image(extra_img_path, caption="Desain Sistem", use_column_width=True)
            
            if github_url != "#":
                st.markdown(f"[🔗 GitHub Repo]({github_url})")

    st.write("---")

# =========================
# 🔹 AI Engineer Projects
# =========================
st.subheader("🤖 Proyek AI/ML Engineer")

project_card(
    "Generative AI Berdasarkan API Basis Data PDAM Surya Sembada Kota Surabaya",
    "Desember 2024 – April 2025",
    "Chatbot Generatif AI berbasis Text-to-Text Generation yang aman, cerdas, dan terhubung dengan API database internal PDAM untuk menghasilkan jawaban naratif kontekstual.",
    [
        "Fine-tuning model RoBERTa untuk intent classification, BERT untuk NER, dan Cendol-mT5 untuk text generation dengan perbandingan model sebelumnya dan dipilih model terbaik dari masing-masing pendekatan.",
        "Implementasi normalisasi pertanyaan (slang, typo) untuk Bahasa Indonesia.",
        "Membangun API gateway untuk akses database PDAM secara aman.",
        "Mendesain frontend berbasis ReactJs."
    ],
    img_path="project/ai/generative_ai.png",
    github_url="https://github.com/username/generative-ai-chatbot",
    video_url="https://youtu.be/Mrv-jpRoClg",
    extra_img_path="project/ai/ds_generative_ai.png",
    skills=[
        ("skills/reactjs.png", "ReactJS"),
        ("skills/flask.png", "Flask"),
        ("skills/huggingface.png", "HuggingFace"),
        ("skills/python.png", "Python"),
        ("skills/postgresql.png", "PostgreSQL"),
        ("skills/pytorch.png", "PyTorch")
    ]
)

project_card(
    "Deteksi Penyakit Gigi pada Radiograf Panoramik",
    "Januari 2025 – April 2025",
    "API berbasis Machine Learning untuk mendeteksi penyakit gigi Karies, Impaksi, Lesi Periapikal, dan Resorpsi pada radiograf panoramik menggunakan teknik segmentasi gambar dengan perbandingan model UNet dan UNet-ResNet50 Backbone.",
    [
        "Anotasi gambar radiografik panoramik yang terdeteksi adanya penyakit gigi menggunakan CVAT.",
        "Membangun dan melatih model deep learning untuk segmentasi semantik dengan PyTorch.",
        "Evaluasi performa model pada dataset multiclass imbalanced dengan preprocessing & augmentasi.",
        "Deploy model terbaik sebagai RESTful API menggunakan Flask."
    ],
    img_path="project/ai/gigi.png",
    github_url="https://github.com/username/tooth-disease-detection",
    extra_img_path="project/ai/ds_gigi.png",
    skills=[
        ("skills/numpy.png", "NumPy"),
        ("skills/flask.png", "Flask"),
        ("skills/cvat.png", "CVAT"),
        ("skills/python.png", "Python"),
        ("skills/opencv.png", "OpenCV"),
        ("skills/tensorflow.png", "TensorFlow")
    ]
)

project_card(
    "Chatbot Layanan Pelanggan Telkom Witel Suramadu di Platform WhatsApp",
    "Juli 2024 – Desember 2024",
    "Sistem chatbot berbasis klasifikasi teks untuk menjawab pertanyaan pelanggan Telkom "
    "dan terintegrasi dengan WhatsApp menggunakan pendekatan LLM dan logika rule-based.",
    [
        "Membangun pipeline klasifikasi teks untuk pertanyaan pelanggan.",
        "Melakukan fine-tuning model dengan dataset QnA Customer Service Telkom.",
        "Menerapkan hyperparameter tuning dan evaluasi model (accuracy, confusion matrix).",
        "Mengintegrasikan model ke WhatsApp API melalui server backend.",
        "Menambahkan logika if-else untuk jawaban class agar sesuai dengan kebutuhan user."
    ],
    img_path="project/ai/telkom.png",
    github_url="https://github.com/username/chatbot-telkom-witel-suramadu",
    extra_img_path="project/ai/ds_telkom.png",
    skills=[
        ("skills/pandas.png", "Pandas"),
        ("skills/scikitlearn.png", "Scikit-Learn"),
        ("skills/huggingface.png", "HuggingFace"),
        ("skills/pytorch.png", "PyTorch"),
        ("skills/python.png", "Python"),
        ("skills/nodejs.png", "NodeJS")
    ]
)

project_card(
    "Sistem Rekomendasi Karir di Bidang IT",
    "April 2025",
    "Sistem pakar berbasis machine learning berisi 50 pertanyaan pilihan ganda (Sangat Tidak Setuju - Sangat Setuju) untuk merekomendasikan jalur karir di bidang IT, yaitu Backend Developer, Data Scientist, Frontend Developer, Product Manager, dan UI/UX Designer menggunakan klasifikasi data tabular.",
    [
        "Training Random Forest, XGBoost, dan MLPClassifier pada data karir untuk menentukan model terbaik.",
        "Preprocessing: encoding label, evaluasi dengan accuracy & classification report.",
        "Deploy model terbaik via Flask API."
    ],
    img_path="project/ai/karir.png",
    github_url="https://github.com/username/career-recommendation",
    extra_img_path="project/ai/ds_karir.png",
    skills=[
        ("skills/pandas.png", "Pandas"),
        ("skills/scikitlearn.png", "Scikit-Learn"),
        ("skills/numpy.png", "NumPy"),
        ("skills/flask.png", "Flask"),
        ("skills/python.png", "Python"),
        ("skills/streamlit.png", "Streamlit")
    ]
)

# =========================
# 🔹 Data Analytics Projects
# =========================
st.subheader("📊 Proyek Data Analyst")

project_card(
    "Dashboard Rekomendasi Program Penurunan Stunting di NTT Tahun 2018-2022",
    "September 2023 – Desember 2023",
    "Dashboard analitik untuk memantau faktor-faktor yang mempengaruhi prevalensi stunting di NTT, dilengkapi sistem rekomendasi program kerja berbasis faktor dominan.",
    [
        "Membangun dashboard interaktif dengan Power BI.",
        "Menggunakan K-Means untuk clustering.",
        "Analisis faktor dengan Python (FactorAnalysis)."
    ],
    img_path="stunting_dashboard.png",
    video_url="https://youtu.be/mQQpIzt-GQU",
    skills=[
        ("skills/pandas.png", "Pandas"),
        ("skills/scikitlearn.png", "Scikit-Learn"),
        ("skills/numpy.png", "NumPy"),
        ("skills/python.png", "Python"),
        ("skills/powerbi.png", "Power BI")
    ]
)

project_card(
    "Dashboard Analitik Yayasan Dana Sosial Al-Falah Surabaya",
    "Juli 2023 – September 2023",
    "Dashboard analitik untuk memantau dana terhimpun dan dana tersalur, dilengkapi dengan fitur clustering serta forecasting untuk mendukung pengambilan keputusan yayasan.",
    [
        "Membaca dan menganalisis insight dari data (Dana Terhimpun & Dana Tersalur).",
        "Membuat clustering data dengan metode K-Means.",
        "Membangun forecasting dana dengan Python (ARIMA/Prophet).",
        "Membuat dashboard interaktif dengan Power BI."
    ],
    img_path="ydsf_dashboard.png",
    video_url="https://youtu.be/Emc6MmD3IEM",
    skills=[
        ("skills/pandas.png", "Pandas"),
        ("skills/scikitlearn.png", "Scikit-Learn"),
        ("skills/numpy.png", "NumPy"),
        ("skills/python.png", "Python"),
        ("skills/powerbi.png", "Power BI")
    ]
)

# --- Contact ---
st.header("📫 Kontak")

col1, col2, col3 = st.columns(3)

card_style = """
    <style>
    .contact-card {
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 5px; /* space bawah kecil */
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        background-color: var(--background-color); /* ikut theme streamlit */
        color: var(--text-color);
        border: 1px solid var(--secondary-background-color);
    }
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    .contact-card a {
        color: var(--text-color) !important;
        text-decoration: none;
    }

    /* Atur padding bawah global biar ga kosong */
    .block-container {
        padding-bottom: 20px !important;
    }
    </style>
"""

st.markdown(card_style, unsafe_allow_html=True)

def contact_card(icon, link, label):
    return f"""
        <div class="contact-card">
            <p style="font-size:28px; margin:0;">{icon}</p>
            <a href="{link}" target="_blank" style="font-size:16px;">
                {label}
            </a>
        </div>
    """

with col1:
    st.markdown(contact_card("📩", "https://mail.google.com/mail/?view=cm&fs=1&to=reydikofakhran@gmail.com", "Email"), unsafe_allow_html=True)

with col2:
    st.markdown(contact_card("🔗", "https://www.linkedin.com/in/reydikofakhranhaidi/", "LinkedIn"), unsafe_allow_html=True)

with col3:
    st.markdown(contact_card("☏", "http://wa.me/6282213185236", "WhatsApp"), unsafe_allow_html=True)

# st.write("💻 [GitHub](https://github.com/username)")