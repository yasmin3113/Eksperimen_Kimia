function performTitration() {
    const acid = document.getElementById('acid').value;import streamlit as st
import numpy as np
from molmass import Formula

st.set_page_config(page_title="Laboratorium Kimia Virtual", layout="wide")

st.title("🧪 Laboratorium Kimia Virtual")

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
        mol_asam = kons_asam * (vol_asam / 1000)
        vol_basa_ml = (mol_asam / kons_basa) * 1000
        st.success(f"📈 Volume basa yang diperlukan untuk netralisasi: **{vol_basa_ml:.2f} mL**")

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

    
    const acidConc = parseFloat(document.getElementById('acidConc').value);
    const acidVol = parseFloat(document.getElementById('acidVol').value);
    const baseConc = parseFloat(document.getElementById('baseConc').value);
    const result = document.getElementById('titrationResult');

    if (acidConc && acidVol && baseConc) {
        // Menghitung mol asam: M x V (dalam liter)
        const acidMoles = acidConc * (acidVol / 1000); // mL ke L

        // Menghitung volume basa (dalam mL) yang dibutuhkan untuk netralisasi
        const baseVolNeeded = (acidMoles / baseConc) * 1000; // L ke mL

        result.innerHTML = `
            <h3>📊 Hasil Titrasi</h3>
            <p><strong>Asam:</strong> ${acid}</p>
            <p><strong>Konsentrasi Asam:</strong> ${acidConc} M</p>
            <p><strong>Volume Asam:</strong> ${acidVol} mL</p>
            <p><strong>Konsentrasi Basa (NaOH):</strong> ${baseConc} M</p>
            <p><strong>Volume Basa yang Diperlukan untuk Netralisasi:</strong> ${baseVolNeeded.toFixed(2)} mL</p>
        `;
    } else {
        result.innerHTML = `
            <h3>⚠️ Input Tidak Lengkap</h3>
            <p>Harap isi semua nilai konsentrasi dan volume dengan benar.</p>
        `;
    }
}
