
# 🔬 Mechanical Retina: Photon Detection Through Mechanical Transduction

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research](https://img.shields.io/badge/status-research-orange.svg)]()

> **A novel approach to photon detection using MEMS-based mechanical transducers instead of traditional semiconductor photodiodes.**

Instead of converting photons to electrons (like conventional image sensors), this project explores detecting light through **mechanical displacement** caused by radiation pressure, thermal expansion, or photomechanical materials.

---

## 🎯 Project Vision

Create a **100×100 pixel "mechanical retina"** that:
- Detects photons through **physical cantilever deflection**
- Achieves **sub-picowatt sensitivity** (0.5-1 pW per pixel)
- Operates at **room temperature** with MEMS-compatible fabrication
- Provides **radiation-hard imaging** for extreme environments

**Why This Matters:**
- 🛰️ **Radiation-hard sensors** for space applications
- 🔬 **Fundamental physics research** in quantum optomechanics
- 🎓 **Educational demonstration** of mechanical transduction principles
- 🔋 **Ultra-low-power** potential in specialized applications

---

## 📊 Current Status

**🚧 Phase 1: Theoretical Research & Simulation** (Current)

| Component | Status | Progress |
|-----------|--------|----------|
| Radiation pressure simulation | ✅ Complete | 100% |
| Thermal bolometer design | ✅ Complete | 100% |
| MEMS fabrication process | ✅ Documented | 100% |
| Signal processing pipeline | ✅ Designed | 100% |
| Hardware prototype | ⏳ Pending | 0% |
| Experimental validation | ⏳ Pending | 0% |

**Key Findings:**
- Single-photon detection impossible at room temperature (thermal noise dominates)
- ~10⁶ photons needed for SNR=1 with optimized cantilever design
- Bimetallic microbolometer approach most promising for practical implementation

---

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8+ with scientific stack
pip install numpy scipy matplotlib

# Optional: For advanced image processing
pip install opencv-python pillow
```

### Run Basic Simulations

**1. Nano-cantilever photon detector:**
```bash
cd simulations/radiation_pressure
python single_photon_force.py
```

**Expected output:**
- Cantilever displacement vs time plot
- Thermal noise analysis
- Minimum detectable power calculation
- Phase space trajectory

**Results preview:**
```
SINGLE PHOTON IMPACT:
  Peak displacement (vacuum, Q=10000): 0.0023 fm
  SNR vs thermal: 2.31e-08
  Photons needed for SNR=1: 1.87e+15 photons
```

**2. MEMS bolometer array simulation:**
```bash
cd simulations/bolometer_array
python thermal_response.py
```

---

## 📁 Repository Structure

```
mechanical-retina/
├── docs/
│   ├── theory/
│   │   ├── radiation_pressure.md      # Photon momentum transfer calculations
│   │   ├── thermal_detection.md       # Bolometric detection principles
│   │   └── quantum_limits.md          # Fundamental sensitivity limits
│   ├── design/
│   │   ├── mems_specification.md      # Complete MEMS device specs
│   │   ├── system_architecture.md     # Full system design
│   │   └── fabrication_process.md     # 14-mask MEMS process flow
│   └── images/
│       ├── cantilever_response.png
│       ├── system_block_diagram.png
│       └── pixel_cross_section.png
├── simulations/
│   ├── radiation_pressure/
│   │   ├── single_photon_force.py     # Cantilever dynamics simulation
│   │   └── thermal_noise_analysis.py  # Noise budget calculator
│   ├── bolometer_array/
│   │   ├── thermal_response.py        # Bolometer pixel simulation
│   │   └── array_imaging.py           # Image formation demo
│   └── signal_processing/
│       ├── image_reconstruction.py    # Full processing pipeline
│       └── calibration_tools.py       # NUC and FPN correction
├── hardware/
│   ├── mems_layout/                   # GDS files (future)
│   ├── pcb_designs/                   # KiCAD schematics (future)
│   └── optical_design/                # Lens specifications
├── tests/
│   └── unit_tests/
└── README.md
```

---

## 🔬 Technical Approach

### Five Detection Mechanisms Explored:

| Approach | Sensitivity | Speed | Temp | Status |
|----------|-------------|-------|------|--------|
| **1. Radiation Pressure Cantilever** | 10¹⁵ photons | Fast (μs) | Cryogenic | Simulated |
| **2. Bimetallic Microbolometer** | 10⁶ photons | Medium (ms) | Room temp | ✅ **Selected** |
| **3. Azobenzene Photomechanical** | 10⁹ photons | Slow (s) | Room temp | Explored |
| **4. Quantum Optomechanical** | 1 photon | Fast (μs) | Cryogenic | Theory only |
| **5. Bio-inspired Vesicles** | 10⁷ photons | Slow (s) | Room temp | Concept |

**Selected Design: Bimetallic Microbolometer Array**
- **Pixel pitch:** 10 μm (100×100 array in 1 mm²)
- **Sensitivity:** 0.5-1 pW per pixel
- **Response time:** 0.35 ms thermal constant, 100 ms with averaging
- **Readout:** Capacitive displacement sensing
- **Fabrication:** Standard MEMS process (14 masks)

  ---

## 📸 Visualizations

### System Overview

![Mechanical Retina System](docs/images/system_overview_macro.png)
*100×100 pixel mechanical sensor array with bimetallic cantilevers and capacitive readout*

### Single Pixel Detail

![Single Pixel Closeup](docs/images/single_pixel_closeup.png)
*Nano-scale view of a single pixel showing photon impact and mechanical deflection*

> **Note:** Images generated using AI tools. See [`docs/visualization/IMAGE_GENERATION_PROMPTS.md`](docs/visualization/IMAGE_GENERATION_PROMPTS.md) for prompts and generation instructions.

---

### Key Performance Metrics:
```
✅ Sensitivity:        0.5 pW (meets <1 pW target)
✅ Array size:         100×100 pixels
✅ Pixel pitch:        10 μm
✅ Response time:      <100 ms (with integration)
✅ Dynamic range:      80 dB
✅ Operating temp:     20°C ± 0.01°C (with TEC)
⚠️  Single photon:     Not achievable at room temp
```

---

## 📈 Results & Visualizations

### Simulation Results

**Cantilever Response to Single Photon:**

![Cantilever Response](docs/images/cantilever_response.png)
*Displacement vs time showing thermal noise dominance*

**Key Insight:** Thermal noise (Brownian motion) at room temperature is ~10⁸× larger than single-photon momentum transfer. Cryogenic operation required for single-photon sensitivity.

**Thermal Bolometer Array Performance:**

| Metric | Value |
|--------|-------|
| Thermal time constant | 0.35 ms |
| Temperature rise per pW | 6.3 mK |
| Capacitance change per pW | 0.86 aF |
| Noise equivalent power | 0.5 pW/√Hz |

---

## 🛠️ Development Roadmap

### ✅ Phase 1: Theoretical Feasibility (Complete)
- [x] Literature review of mechanical photodetection
- [x] Python simulations of 5 different approaches
- [x] MEMS device specification (100×100 array)
- [x] Complete system architecture design
- [x] Noise budget analysis
- [x] Fabrication process documentation

### 🚧 Phase 2: Detailed Design (In Progress - 60%)
- [x] Optical system design (lens, filters)
- [x] Readout electronics schematic
- [x] Signal processing algorithms
- [ ] GDS layout for MEMS fabrication
- [ ] PCB design for electronics
- [ ] Firmware development (FPGA)

### ⏳ Phase 3: Prototype Fabrication (Not Started)
- [ ] MEMS fabrication (foundry or university cleanroom)
- [ ] PCB assembly and testing
- [ ] Optical system assembly
- [ ] System integration

### ⏳ Phase 4: Experimental Validation (Not Started)
- [ ] Dark noise characterization
- [ ] Sensitivity measurements
- [ ] Image quality assessment
- [ ] Publication of results

**Estimated Timeline:** 18-24 months from funding to first prototype

---

## 🖥️ Interactive PCB Design Viewer

Explore the complete hardware design with our interactive viewer:

**[🚀 Launch Interactive Viewer](https://Saranoah.github.io/Mechanical-Retina-Project/interactive/)**

[![PCB Design Viewer](docs/images/viewer_preview.png)](https://Saranoah.github.io/Mechanical-Retina-Project/interactive/))

Features:
- 📋 Complete Bill of Materials (BOM)
- ⚡ Power budget analysis
- 🔧 Design considerations
- 💻 Firmware module documentation
- 📊 Cost breakdown


---

## 🤝 Contributing

We welcome contributions from:
- 🔬 **Physicists**: Quantum optomechanics, thermal physics
- ⚙️ **MEMS Engineers**: Device design, fabrication expertise
- 🔭 **Optical Engineers**: Lens design, calibration methods
- 💻 **Software Developers**: Signal processing, image reconstruction
- 📊 **Data Scientists**: Machine learning for image enhancement

### How to Contribute:
1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/amazing-improvement`)
3. **Commit** your changes (`git commit -m 'Add quantum noise analysis'`)
4. **Push** to the branch (`git push origin feature/amazing-improvement`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📚 Key References

1. **Radiation Pressure Detection:**
   - Aspelmeyer et al., "Cavity optomechanics," *Rev. Mod. Phys.* 86, 1391 (2014)

2. **MEMS Bolometers:**
   - Rogalski et al., "Uncooled infrared detectors," *Opto-Electronics Review* 20(3), 279-308 (2012)

3. **Quantum Limits:**
   - Clerk et al., "Introduction to quantum noise, measurement, and amplification," *Rev. Mod. Phys.* 82, 1155 (2010)

4. **MEMS Fabrication:**
   - Madou, M., *Fundamentals of Microfabrication* (CRC Press, 2002)

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

**Academic Use:** Please cite this repository if used in academic work:
```bibtex
@misc{mechanical_retina_2024,
  author = {[Israa Ali]},
  title = {Mechanical Retina: Photon Detection Through Mechanical Transduction},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/Mechanical-Retina-Project}
}
```

---

## 🙏 Acknowledgments

- Inspired by biological photoreceptors and quantum optomechanics research
- Simulation framework adapted from open-source scientific Python tools

---

## 📧 Contact

**Project Lead:** Israa Ali 
**Email:** israaali2019@domain.com  
**LinkedIn:**  https://www.linkedin.com/in/israaalipharmacist/ 

**Questions?** Open an issue or start a discussion!

---

## ⭐ Star History

If you find this project interesting, please consider starring it! ⭐

## Acknowledgments
Concept development assisted by AI collaboration, exploring the boundaries of mechanical photon detection.

---

**Note:** This is a research project exploring fundamental limits of mechanical photodetection. It is not intended to compete with commercial CMOS/CCD sensors but rather to demonstrate novel transduction principles and potential applications in extreme environments.

