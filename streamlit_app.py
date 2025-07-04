<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chemistry Experiment Lab</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .tabs {
            display: flex;
            justify-content: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .tab {
            background: rgba(255,255,255,0.9);
            border: none;
            padding: 12px 24px;
            margin: 5px;
            cursor: pointer;
            border-radius: 25px;
            font-weight: bold;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .tab.active, .tab:hover {
            background: #4CAF50;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        .tab-content {
            display: none;
            background: rgba(255,255,255,0.95);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
        }

        .tab-content.active {
            display: block;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .experiment-section {
            margin-bottom: 30px;
        }

        .experiment-controls {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 20px;
        }

        .control-group {
            display: flex;
            flex-direction: column;
            min-width: 150px;
        }

        .control-group label {
            font-weight: bold;
            margin-bottom: 5px;
            color: #555;
        }

        .control-group select,
        .control-group input {
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s ease;
        }

        .control-group select:focus,
        .control-group input:focus {
            outline: none;
            border-color: #4CAF50;
        }

        .btn {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }

        .result-container {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            min-height: 100px;
            border-left: 5px solid #4CAF50;
        }

        .periodic-table {
            display: grid;
            grid-template-columns: repeat(18, 1fr);
            gap: 2px;
            max-width: 100%;
            margin: 20px 0;
        }

        .element {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 4px;
            text-align: center;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 12px;
            min-height: 60px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .element:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            z-index: 10;
        }

        .element-symbol {
            font-weight: bold;
            font-size: 16px;
        }

        .element-name {
            font-size: 10px;
            opacity: 0.8;
        }

        .element-number {
            font-size: 10px;
            opacity: 0.6;
        }

        .calculator-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .calculator-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .calculator-card h3 {
            margin-bottom: 15px;
            text-align: center;
        }

        .formula-display {
            background: rgba(255,255,255,0.2);
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            font-family: monospace;
            font-size: 18px;
            text-align: center;
            backdrop-filter: blur(5px);
        }

        .reaction-animation {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
            font-size: 24px;
        }

        .molecule {
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            color: white;
            padding: 15px;
            border-radius: 50%;
            animation: bounce 2s infinite;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }

        .arrow {
            font-size: 30px;
            color: #4CAF50;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        .info-panel {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }

        .info-panel h3 {
            margin-bottom: 15px;
            color: #FFD700;
        }

        @media (max-width: 768px) {
            .periodic-table {
                grid-template-columns: repeat(10, 1fr);
            }
            
            .experiment-controls {
                flex-direction: column;
            }
            
            .control-group {
                min-width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧪 Chemistry Experiment Lab</h1>
            <p>Jelajahi dunia kimia dengan simulasi interaktif</p>
        </div>

        <div class="tabs">
            <button class="tab active" onclick="showTab('reactions')">Reaksi Kimia</button>
            <button class="tab" onclick="showTab('periodic')">Tabel Periodik</button>
            <button class="tab" onclick="showTab('calculator')">Kalkulator Kimia</button>
            <button class="tab" onclick="showTab('experiments')">Eksperimen</button>
        </div>

        <div id="reactions" class="tab-content active">
            <h2>🔬 Simulasi Reaksi Kimia</h2>
            <div class="experiment-section">
                <div class="experiment-controls">
                    <div class="control-group">
                        <label>Reaktan 1:</label>
                        <select id="reactant1">
                            <option value="H2">H₂ (Hidrogen)</option>
                            <option value="O2">O₂ (Oksigen)</option>
                            <option value="Na">Na (Natrium)</option>
                            <option value="Cl2">Cl₂ (Klorin)</option>
                            <option value="HCl">HCl (Asam Klorida)</option>
                            <option value="NaOH">NaOH (Natrium Hidroksida)</option>
                        </select>
                    </div>
                    <div class="control-group">
                        <label>Reaktan 2:</label>
                        <select id="reactant2">
                            <option value="O2">O₂ (Oksigen)</option>
                            <option value="H2">H₂ (Hidrogen)</option>
                            <option value="Cl2">Cl₂ (Klorin)</option>
                            <option value="Na">Na (Natrium)</option>
                            <option value="NaOH">NaOH (Natrium Hidroksida)</option>
                            <option value="HCl">HCl (Asam Klorida)</option>
                        </select>
                    </div>
                    <div class="control-group">
                        <label>Suhu (°C):</label>
                        <input type="number" id="temperature" value="25" min="0" max="1000">
                    </div>
                    <div class="control-group">
                        <label>Tekanan (atm):</label>
                        <input type="number" id="pressure" value="1" min="0.1" max="10" step="0.1">
                    </div>
                </div>
                <button class="btn" onclick="simulateReaction()">🚀 Mulai Reaksi</button>
                
                <div class="result-container" id="reactionResult">
                    <div class="reaction-animation" id="reactionAnimation" style="display: none;">
                        <div class="molecule" id="mol1">H₂</div>
                        <div class="arrow">→</div>
                        <div class="molecule" id="mol2">O₂</div>
                        <div class="arrow">→</div>
                        <div class="molecule" id="product">H₂O</div>
                    </div>
                    <div id="reactionDetails">
                        <p>Pilih reaktan dan klik "Mulai Reaksi" untuk melihat simulasi!</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="periodic" class="tab-content">
            <h2>⚛️ Tabel Periodik Interaktif</h2>
            <div class="periodic-table" id="periodicTable"></div>
            <div class="info-panel" id="elementInfo">
                <h3>Informasi Unsur</h3>
                <p>Klik pada unsur untuk melihat detail informasi</p>
            </div>
        </div>

        <div id="calculator" class="tab-content">
            <h2>🧮 Kalkulator Kimia</h2>
            <div class="calculator-grid">
                <div class="calculator-card">
                    <h3>Massa Molar</h3>
                    <div class="control-group">
                        <label>Rumus Kimia:</label>
                        <input type="text" id="molecularFormula" placeholder="contoh: H2SO4">
                    </div>
                    <button class="btn" onclick="calculateMolarMass()">Hitung</button>
                    <div class="formula-display" id="molarMassResult">Masukkan rumus kimia</div>
                </div>
                
                <div class="calculator-card">
                    <h3>Konsentrasi</h3>
                    <div class="control-group">
                        <label>Mol zat terlarut:</label>
                        <input type="number" id="moles" placeholder="mol" step="0.001">
                    </div>
                    <div class="control-group">
                        <label>Volume larutan (L):</label>
                        <input type="number" id="volume" placeholder="L" step="0.001">
                    </div>
                    <button class="btn" onclick="calculateConcentration()">Hitung</button>
                    <div class="formula-display" id="concentrationResult">M = n/V</div>
                </div>
                
                <div class="calculator-card">
                    <h3>Persamaan Gas Ideal</h3>
                    <div class="control-group">
                        <label>Tekanan (atm):</label>
                        <input type="number" id="gasP" placeholder="atm" step="0.1">
                    </div>
                    <div class="control-group">
                        <label>Volume (L):</label>
                        <input type="number" id="gasV" placeholder="L" step="0.1">
                    </div>
                    <div class="control-group">
                        <label>Suhu (K):</label>
                        <input type="number" id="gasT" placeholder="K" step="0.1">
                    </div>
                    <button class="btn" onclick="calculateIdealGas()">Hitung n</button>
                    <div class="formula-display" id="idealGasResult">PV = nRT</div>
                </div>
            </div>
        </div>

        <div id="experiments" class="tab-content">
            <h2>🔬 Eksperimen Virtual</h2>
            <div class="experiment-section">
                <h3>Eksperimen Titrasi Asam-Basa</h3>
                <div class="experiment-controls">
                    <div class="control-group">
                        <label>Asam:</label>
                        <select id="acid">
                            <option value="HCl">HCl (Asam Kuat)</option>
                            <option value="CH3COOH">CH₃COOH (Asam Lemah)</option>
                            <option value="H2SO4">H₂SO₄ (Asam Kuat)</option>
                        </select>
                    </div>
                    <div class="control-group">
                        <label>Konsentrasi Asam (M):</label>
                        <input type="number" id="acidConc" value="0.1" step="0.01" min="0.01">
                    </div>
                    <div class="control-group">
                        <label>Volume Asam (mL):</label>
                        <input type="number" id="acidVol" value="25" step="1" min="1">
                    </div>
                    <div class="control-group">
                        <label>Basa (NaOH):</label>
                        <input type="number" id="baseConc" value="0.1" step="0.01" min="0.01">
                        <small>Konsentrasi (M)</small>
                    </div>
                </div>
                <button class="btn" onclick="performTitration()">🧪 Lakukan Titrasi</button>
                
                <div class="result-container" id="titrationResult">
                    <p>Siapkan untuk melakukan titrasi!</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Data unsur untuk tabel periodik
        const elements = [
            {symbol: 'H', name: 'Hidrogen', number: 1, mass: 1.008},
            {symbol: 'He', name: 'Helium', number: 2, mass: 4.003},
            {symbol: 'Li', name: 'Lithium', number: 3, mass: 6.941},
            {symbol: 'Be', name: 'Berilium', number: 4, mass: 9.012},
            {symbol: 'B', name: 'Boron', number: 5, mass: 10.811},
            {symbol: 'C', name: 'Karbon', number: 6, mass: 12.011},
            {symbol: 'N', name: 'Nitrogen', number: 7, mass: 14.007},
            {symbol: 'O', name: 'Oksigen', number: 8, mass: 15.999},
            {symbol: 'F', name: 'Fluorin', number: 9, mass: 18.998},
            {symbol: 'Ne', name: 'Neon', number: 10, mass: 20.180},
            {symbol: 'Na', name: 'Natrium', number: 11, mass: 22.990},
            {symbol: 'Mg', name: 'Magnesium', number: 12, mass: 24.305},
            {symbol: 'Al', name: 'Aluminium', number: 13, mass: 26.982},
            {symbol: 'Si', name: 'Silikon', number: 14, mass: 28.086},
            {symbol: 'P', name: 'Fosfor', number: 15, mass: 30.974},
            {symbol: 'S', name: 'Sulfur', number: 16, mass: 32.065},
            {symbol: 'Cl', name: 'Klorin', number: 17, mass: 35.453},
            {symbol: 'Ar', name: 'Argon', number: 18, mass: 39.948}
        ];

        // Massa atom untuk kalkulator
        const atomicMasses = {
            'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
            'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
            'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.086, 'P': 30.974,
            'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078
        };

        // Reaksi kimia database
        const reactions = {
            'H2+O2': {
                equation: '2H₂ + O₂ → 2H₂O',
                product: 'H₂O (Air)',
                type: 'Sintesis',
                energy: 'Eksotermik',
                description: 'Pembentukan air dari hidrogen dan oksigen'
            },
            'Na+Cl2': {
                equation: '2Na + Cl₂ → 2NaCl',
                product: 'NaCl (Garam)',
                type: 'Sintesis',
                energy: 'Eksotermik',
                description: 'Pembentukan garam dari natrium dan klorin'
            },
            'HCl+NaOH': {
                equation: 'HCl + NaOH → NaCl + H₂O',
                product: 'NaCl + H₂O',
                type: 'Netralisasi',
                energy: 'Eksotermik',
                description: 'Reaksi netralisasi asam-basa'
            }
        };

        function showTab(tabName) {
            // Hide all tab contents
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => content.classList.remove('active'));

            // Remove active class from all tabs
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => tab.classList.remove('active'));

            // Show selected tab content
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');

            // Initialize periodic table if periodic tab is selected
            if (tabName === 'periodic') {
                initPeriodicTable();
            }
        }

        function simulateReaction() {
            const reactant1 = document.getElementById('reactant1').value;
            const reactant2 = document.getElementById('reactant2').value;
            const temperature = document.getElementById('temperature').value;
            const pressure = document.getElementById('pressure').value;

            const reactionKey = `${reactant1}+${reactant2}`;
            const reverseKey = `${reactant2}+${reactant1}`;
            
            const reaction = reactions[reactionKey] || reactions[reverseKey];

            const animationDiv = document.getElementById('reactionAnimation');
            const resultDiv = document.getElementById('reactionDetails');

            if (reaction) {
                // Show animation
                animationDiv.style.display = 'flex';
                document.getElementById('mol1').textContent = reactant1;
                document.getElementById('mol2').textContent = reactant2;
                document.getElementById('product').textContent = reaction.product.split(' ')[0];

                // Show reaction details
                resultDiv.innerHTML = `
                    <h3>🎯 Hasil Reaksi</h3>
                    <div class="formula-display">${reaction.equation}</div>
                    <p><strong>Produk:</strong> ${reaction.product}</p>
                    <p><strong>Jenis Reaksi:</strong> ${reaction.type}</p>
                    <p><strong>Energi:</strong> ${reaction.energy}</p>
                    <p><strong>Kondisi:</strong> T = ${temperature}°C, P = ${pressure} atm</p>
                    <p><strong>Deskripsi:</strong> ${reaction.description}</p>
                `;
            } else {
                animationDiv.style.display = 'none';
                resultDiv.innerHTML = `
                    <h3>⚠️ Reaksi Tidak Tersedia</h3>
                    <p>Reaksi antara ${reactant1} dan ${reactant2} belum tersedia dalam database.</p>
                    <p>Coba kombinasi reaktan yang lain!</p>
                `;
            }
        }

        function initPeriodicTable() {
            const table = document.getElementById('periodicTable');
            table.innerHTML = '';

            elements.forEach(element => {
                const elementDiv = document.createElement('div');
                elementDiv.className = 'element';
                elementDiv.innerHTML = `
                    <div class="element-number">${element.number}</div>
                    <div class="element-symbol">${element.symbol}</div>
                    <div class="element-name">${element.name}</div>
                `;
                elementDiv.onclick = () => showElementInfo(element);
                table.appendChild(elementDiv);
            });
        }

        function showElementInfo(element) {
            const infoPanel = document.getElementById('elementInfo');
            infoPanel.innerHTML = `
                <h3>⚛️ ${element.name} (${element.symbol})</h3>
                <p><strong>Nomor Atom:</strong> ${element.number}</p>
                <p><strong>Massa Atom:</strong> ${element.mass} u</p>
                <p><strong>Simbol:</strong> ${element.symbol}</p>
                <p><strong>Konfigurasi Elektron:</strong> ${getElectronConfig(element.number)}</p>
                <p><strong>Golongan:</strong> ${getGroup(element.number)}</p>
            `;
        }

        function getElectronConfig(atomicNumber) {
            const configs = {
                1: '1s¹', 2: '1s²', 3: '[He] 2s¹', 4: '[He] 2s²', 5: '[He] 2s² 2p¹',
                6: '[He] 2s² 2p²', 7: '[He] 2s² 2p³', 8: '[He] 2s² 2p⁴', 9: '[He] 2s² 2p⁵',
                10: '[He] 2s² 2p⁶', 11: '[Ne] 3s¹', 12: '[Ne] 3s²', 13: '[Ne] 3s² 3p¹',
                14: '[Ne] 3s² 3p²', 15: '[Ne] 3s² 3p³', 16: '[Ne] 3s² 3p⁴', 17: '[Ne] 3s² 3p⁵',
                18: '[Ne] 3s² 3p⁶'
            };
            return configs[atomicNumber] || 'Tidak tersedia';
        }

        function getGroup(atomicNumber) {
            const groups = {
                1: 'Alkali', 2: 'Gas Mulia', 3: 'Alkali', 4: 'Alkali Tanah',
                5: 'Boron', 6: 'Karbon', 7: 'Nitrogen', 8: 'Oksigen',
                9: 'Halogen', 10: 'Gas Mulia', 11: 'Alkali', 12: 'Alkali Tanah',
                13: 'Boron', 14: 'Karbon', 15: 'Nitrogen', 16: 'Oksigen',
                17: 'Halogen', 18: 'Gas Mulia'
            };
            return groups[atomicNumber] || 'Tidak tersedia';
        }

        function calculateMolarMass() {
            const formula = document.getElementById('molecularFormula').value.toUpperCase();
            const result = document.getElementById('molarMassResult');
            
            if (!formula) {
                result.textContent = 'Masukkan rumus kimia';
                return;
            }

            try {
                let totalMass = 0;
                let i = 0;
                
                while (i < formula.length) {
                    let element = '';
                    let count = '';
                    
                    // Get element symbol
                    element += formula[i];
                    i++;
                    
                    // Check for second character (lowercase)
                    if (i < formula.length && formula[i] >= 'a' && formula[i] <= 'z') {
                        element += formula[i].toLowerCase();
                        i++;
                    }
                    
                    // Get count
                    while (i < formula.length && formula[i] >= '0' && formula[i] <= '9') {
                        count += formula[i];
                        i++;
                    }
                    
                    const atomCount = count === '' ? 1 : parseInt(count);
                    
                    if (atomicMasses[element]) {
                        totalMass += atomicMasses[element] * atomCount;
                    } else {
                        result.textContent = `Unsur ${element} tidak ditemukan`;
                        return;
                    }
                }
                
                result.textContent = `Massa Molar: ${totalMass.toFixed(3)} g/mol`;
            } catch (error) {
                result.textContent = 'Format rumus tidak valid';
            }
        }

        function calculateConcentration() {
            const moles = parseFloat(document.getElementById('moles').value);
            const volume = parseFloat(document.getElementById('volume').value);
            const result = document.getElementById('concentrationResult');
            
            if (moles && volume) {
                const concentration = moles / volume;
                result.textContent = `Konsentrasi: ${concentration.toFixed(4)} M`;
            } else {
                result.textContent = 'Masukkan nilai mol dan volume';
            }
        }

        function calculateIdealGas() {
            const P = parseFloat(document.getElementById('gasP').value);
            const V = parseFloat(document.getElementById('gasV').value);
            const T = parseFloat(document.getElementById('gasT').value);
            const result = document.getElementById('idealGasResult');
            const R = 0.08206; // L·atm/(mol·K)
            
            if (P && V && T) {
                const n = (P * V) / (R * T);
                result.textContent = `Jumlah mol: ${n.toFixed(4)} mol`;
            } else {
                result.textContent = 'Masukkan nilai P, V, dan T';
            }
        }

        function performTitration() {
            const acid = document.getElementById('acid').value;
            const acidConc = parseFloat(document.getElementById('acidConc').value);
            const acidVol = parseFloat(document.getElementById('acidVol').value);
            const baseConc = parseFloat(document.getElementById('baseConc').value);
            const result = document.getElementById('titrationResult');
            
            if (acidConc && acidVol && baseConc) {
                const acidMoles = acidConc * (acidVol / 1000); // Convert mL to L
                const baseVolNeeded = (acidMoles / baseConc) * 1000; // Convert L to mL
                
                result.innerHTML = `
                    <h3>📊
