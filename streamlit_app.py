import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from streamlit_option_menu import option_menu
from molmass import Formula


# Judul
st.set_page_config(page_title="Kalkulator Kimia", layout="centered")


# CSS
st.markdown(
    """
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #9AA6B2;
            color: white;
            padding: 5px;
            widht: 400px;
        }

        .sidebar{
        width: 500px;
        }
        
        /* Teks styling */
        h2{
            text-align: center;
        }
    </syle>
    """,
    unsafe_allow_html=True
)


# Navbar
with st.sidebar:
     selected = option_menu("Kalkulator Kimia", 
                         ["Titrasi",
                          "Kurva Kalibrasi",
                          "Reaksi Kimia"],
                         icons= ["calculator", "bar-chart", "shuffle"],
                         default_index=0,
                         styles={"container": {"background-color": "#FDFBFB"},
                                 "icon": {"color": "red", "font-size": "15px"},
                                 "nav-link": {"font-size": "13px", "text-align": "left"},
                                 "nav-link-selected": {"background-color": "#1237EF", "font-weight": "bold", "color": "white"}})


# Fitur Titrasi
if selected == "Titrasi":
    st.header("Kalkulator Konsentrasi Sampel (Titrasi)")

    

    # Input user
    M1 = st.number_input("Molaritas Titran (M₁) dalam mol/L", min_value=0.0, format="%.5f")
    V1 = st.number_input("Volume Titran (V₁) dalam mL", min_value=0.0, format="%.2f")
    V2 = st.number_input("Volume Sampel (V₂) dalam mL", min_value=0.0, format="%.2f")
    n1 = st.number_input("Koefisien Reaksi Titran (n₁)", min_value=1, max_value=20, value=1, step=1, format="%d")
    n2 = st.number_input("Koefisien Reaksi Sampel (n₂)", min_value=1, max_value=20, value=1, step=1, format="%d")
    # Tombol hitung
    if st.button("Hitung Konsentrasi Sampel"):
        try:
            M2 = (M1 * V1 * n2) / (V2 * n1)
            st.success(f"Konsentrasi Sampel (M₂) = {M2:.5f} mol/L")
        except ZeroDivisionError:
            st.error("Volume sampel atau koefisien tidak boleh nol.")


# Fitur Kurva Kalibrasi
elif selected == "Kurva Kalibrasi":
    st.header("📊 Kalkulator Kurva Kalibrasi Spektrofotometri")

    st.markdown("""
    Aplikasi ini membantu menghitung *persamaan regresi linear* dari data standar, dan menghitung *konsentrasi sampel* dari absorbansi yang diukur.
    """)

    # INPUT DATA STANDAR
    st.subheader("1. Input Data Standar (Konsentrasi vs Absorbansi)")

    with st.form("input_form"):
        data_input = st.text_area(
            "Masukkan data (format: konsentrasi,absorbansi — pisahkan dengan koma dan baris baru)", 
            value=st.session_state.get("data_input", "10,0.15\n20,0.30\n30,0.45"), 
            height=150
        )
        submitted = st.form_submit_button("Hitung Regresi")

    if submitted:
        try:
            # Simpan input ke session state
            st.session_state["data_input"] = data_input

            # Parsing data
            lines = data_input.strip().split("\n")
            data = [list(map(float, line.split(','))) for line in lines]
            df = pd.DataFrame(data, columns=["Konsentrasi", "Absorbansi"])

            # Model regresi linear
            X = df["Konsentrasi"].values.reshape(-1, 1)
            y = df["Absorbansi"].values
            model = LinearRegression()
            model.fit(X, y)

            a = model.coef_[0]
            b = model.intercept_

            # Simpan model ke session_state
            st.session_state["regresi_a"] = a
            st.session_state["regresi_b"] = b
            st.session_state["df"] = df

            st.success(f"Persamaan Regresi: y = {a:.4f}x + {b:.4f}")

        except Exception as e:
            st.error("❌ Format data salah. Contoh: 10,0.15 (tanpa spasi)")

    # BAGIAN 2: ABSORBANSI SAMPEL
    st.subheader("2. Hitung Konsentrasi dari Absorbansi Sampel")

    if "regresi_a" in st.session_state and "regresi_b" in st.session_state:
        a = st.session_state["regresi_a"]
        b = st.session_state["regresi_b"]
        df = st.session_state["df"]

        # Tampilkan grafik kurva kalibrasi
        fig, ax = plt.subplots()
        ax.scatter(df["Konsentrasi"], df["Absorbansi"], color="blue", label="Data Standar")
        ax.plot(df["Konsentrasi"], a * df["Konsentrasi"] + b, color="red", label="Garis Regresi")
        ax.set_xlabel("Konsentrasi (mg/L)")
        ax.set_ylabel("Absorbansi")
        ax.set_title("Kurva Kalibrasi")
        ax.legend()
        st.pyplot(fig)

        # Input absorbansi sampel
        y_sample = st.number_input("Masukkan Absorbansi Sampel", min_value=0.0, format="%.4f", key="abs_sample")

        if y_sample > 0:
            x_sample = (y_sample - b) / a
            st.success(f"🎯 Konsentrasi Sampel = {x_sample:.4f} mg/L")

    else:
        st.info("⚠ Silakan isi dan hitung data regresi terlebih dahulu di bagian atas.")
        
        
#Fitur Reaksi Kimia
elif selected == "Reaksi Kimia":
    st.header("Reaksi Kimia")
    st.title("🧪 Laboratorium Kimia Virtual")

# Sidebar untuk memilih eksperimen
sidebar = st.sidebar.selectbox(
    "Pilih Eksperimen", 
    ("Simulasi Reaksi Kimia", "Titrasi Asam-Basa", "Kalkulator Kimia")
)

# === 1. Simulasi Reaksi Kimia ===
if sidebar == "Simulasi Reaksi Kimia":
    st.header("🔬 Simulasi Reaksi Sederhana")
    reaktan1 = st.selectbox("Reaktan 1", ["H₂", "Na", "HCl"])
    reaktan2 = st.selectbox("Reaktan 2", ["O₂", "Cl₂", "NaOH"])
    suhu = st.slider("Suhu (°C)", 0, 500, 25)
    tekanan = st.slider("Tekanan (atm)", 1, 10, 1)

    reaksi_db = {
        ("H₂", "O₂"): "2H₂ + O₂ → 2H₂O",
        ("Na", "Cl₂"): "2Na + Cl₂ → 2NaCl",
        ("HCl", "NaOH"): "HCl + NaOH → NaCl + H₂O"
    }

    if st.button("🚀 Mulai Reaksi"):
        key = (reaktan1, reaktan2)
        alt_key = (reaktan2, reaktan1)
        hasil = reaksi_db.get(key) or reaksi_db.get(alt_key)
        if hasil:
            st.success(f"💥 Reaksi terjadi:\n\n`{hasil}`\n\n📊 Suhu: {suhu}°C | Tekanan: {tekanan} atm")
        else:
            st.warning("⚠ Reaksi belum tersedia dalam database.")

# === 2. Titrasi Asam-Basa ===
elif sidebar == "Titrasi Asam-Basa":
    st.header("🧪 Simulasi Titrasi Asam-Basa")
    asam = st.selectbox("Jenis Asam", ["HCl", "CH₃COOH"])
    kons_asam = st.number_input("Konsentrasi Asam (M)", value=0.1, step=0.01)
    vol_asam = st.number_input("Volume Asam (mL)", value=25)
    kons_basa = st.number_input("Konsentrasi Basa (NaOH) (M)", value=0.1, step=0.01)

    if st.button("Hitung Volume Basa yang Dibutuhkan"):
        if kons_basa > 0:
            mol_asam = kons_asam * (vol_asam / 1000)
            vol_basa_ml = (mol_asam / kons_basa) * 1000
            st.success(f"📈 Volume basa yang diperlukan untuk netralisasi: *{vol_basa_ml:.2f} mL*")
        else:
            st.error("Konsentrasi basa tidak boleh nol")

# === 3. Kalkulator Kimia ===
elif sidebar == "Kalkulator Kimia":
    st.header("🧮 Kalkulator Kimia")
    tab1, tab2, tab3 = st.tabs(["Massa Molar", "Konsentrasi", "Gas Ideal"])

    with tab1:
        rumus = st.text_input("Masukkan Rumus Kimia", "H2SO4")
        if st.button("Hitung Massa Molar"):
            try:
                massa = Formula(rumus).mass
                st.success(f"Massa molar {rumus} adalah *{massa:.3f} g/mol*")
            except Exception as e:
                st.error(f"Format salah: {e}")

    with tab2:
        mol = st.number_input("Jumlah mol zat (mol)", step=0.001)
        vol = st.number_input("Volume larutan (L)", step=0.001)
        if st.button("Hitung Konsentrasi"):
            if vol > 0:
                kons = mol / vol
                st.success(f"Konsentrasi larutan: *{kons:.3f} M*")
            else:
                st.warning("Volume harus > 0")

    with tab3:
        P = st.number_input("Tekanan (atm)")
        V = st.number_input("Volume (L)")
        T = st.number_input("Suhu (K)")
        R = 0.0821
        if st.button("Hitung mol (n)"):
            try:
                n = (P * V) / (R * T)
                st.success(f"Jumlah mol gas: *{n:.3f} mol*")
            except:
                st.error("Masukkan nilai valid untuk P, V, dan T")import streamlit as st
import numpy as np
from molmass import Formula

st.set_page_config(page_title="Laboratorium Kimia Virtual", layout="wide")
st.title("🧪 Laboratorium Kimia Virtual")

# Sidebar untuk memilih eksperimen
sidebar = st.sidebar.selectbox(
    "Pilih Eksperimen", 
    ("Simulasi Reaksi Kimia", "Titrasi Asam-Basa", "Kalkulator Kimia")
)

# === 1. Simulasi Reaksi Kimia ===
if sidebar == "Simulasi Reaksi Kimia":
    st.header("🔬 Simulasi Reaksi Sederhana")
    reaktan1 = st.selectbox("Reaktan 1", ["H₂", "Na", "HCl"])
    reaktan2 = st.selectbox("Reaktan 2", ["O₂", "Cl₂", "NaOH"])
    suhu = st.slider("Suhu (°C)", 0, 500, 25)
    tekanan = st.slider("Tekanan (atm)", 1, 10, 1)

    reaksi_db = {
        ("H₂", "O₂"): "2H₂ + O₂ → 2H₂O",
        ("Na", "Cl₂"): "2Na + Cl₂ → 2NaCl",
        ("HCl", "NaOH"): "HCl + NaOH → NaCl + H₂O"
    }

    if st.button("🚀 Mulai Reaksi"):
        key = (reaktan1, reaktan2)
        alt_key = (reaktan2, reaktan1)
        hasil = reaksi_db.get(key) or reaksi_db.get(alt_key)
        if hasil:
            st.success(f"💥 Reaksi terjadi:\n\n`{hasil}`\n\n📊 Suhu: {suhu}°C | Tekanan: {tekanan} atm")
        else:
            st.warning("⚠️ Reaksi belum tersedia dalam database.")

# === 2. Titrasi Asam-Basa ===
elif sidebar == "Titrasi Asam-Basa":
    st.header("🧪 Simulasi Titrasi Asam-Basa")
    asam = st.selectbox("Jenis Asam", ["HCl", "CH₃COOH"])
    kons_asam = st.number_input("Konsentrasi Asam (M)", value=0.1, step=0.01)
    vol_asam = st.number_input("Volume Asam (mL)", value=25)
    kons_basa = st.number_input("Konsentrasi Basa (NaOH) (M)", value=0.1, step=0.01)

    if st.button("Hitung Volume Basa yang Dibutuhkan"):
        if kons_basa > 0:
            mol_asam = kons_asam * (vol_asam / 1000)
            vol_basa_ml = (mol_asam / kons_basa) * 1000
            st.success(f"📈 Volume basa yang diperlukan untuk netralisasi: **{vol_basa_ml:.2f} mL**")
        else:
            st.error("Konsentrasi basa tidak boleh nol")

# === 3. Kalkulator Kimia ===
elif sidebar == "Kalkulator Kimia":
    st.header("🧮 Kalkulator Kimia")
    tab1, tab2, tab3 = st.tabs(["Massa Molar", "Konsentrasi", "Gas Ideal"])

    with tab1:
        rumus = st.text_input("Masukkan Rumus Kimia", "H2SO4")
        if st.button("Hitung Massa Molar"):
            try:
                massa = Formula(rumus).mass
                st.success(f"Massa molar {rumus} adalah **{massa:.3f} g/mol**")
            except Exception as e:
                st.error(f"Format salah: {e}")

    with tab2:
        mol = st.number_input("Jumlah mol zat (mol)", step=0.001)
        vol = st.number_input("Volume larutan (L)", step=0.001)
        if st.button("Hitung Konsentrasi"):
            if vol > 0:
                kons = mol / vol
                st.success(f"Konsentrasi larutan: **{kons:.3f} M**")
            else:
                st.warning("Volume harus > 0")

    with tab3:
        P = st.number_input("Tekanan (atm)")
        V = st.number_input("Volume (L)")
        T = st.number_input("Suhu (K)")
        R = 0.0821
        if st.button("Hitung mol (n)"):
            try:
                n = (P * V) / (R * T)
                st.success(f"Jumlah mol gas: **{n:.3f} mol**")
            except:
                st.error("Masukkan nilai valid untuk P, V, dan T")
