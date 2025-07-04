function performTitration() {
    const acid = document.getElementById('acid').value;
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
