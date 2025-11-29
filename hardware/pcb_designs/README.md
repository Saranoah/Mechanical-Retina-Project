# PCB Designs for Mechanical Retina

## Overview

The Mechanical Retina system consists of four interconnected PCBs that handle signal acquisition, processing, power distribution, and system control.

**System Architecture:**
```
┌─────────────┐
│   Sensor    │ (Mechanical detector die)
│   Array     │
└──────┬──────┘
       │
┌──────▼──────────────────────────────────────┐
│  READOUT ELECTRONICS BOARD                  │
│  • 100 charge amplifiers                    │
│  • Capacitive displacement sensing          │
│  • 12-bit ADC conversion                    │
│  • USB 3.0 data output                      │
└──────┬──────────────────────────────────────┘
       │
┌──────▼──────────────────────────────────────┐
│  FPGA PROCESSING BOARD                      │
│  • Real-time signal processing              │
│  • Frame buffering (100 frames)             │
│  • FPN/NUC correction                       │
│  • Temporal averaging                       │
└──────┬──────────────────────────────────────┘
       │
┌──────▼──────────────────────────────────────┐
│  SYSTEM CONTROL BOARD                       │
│  • Temperature stabilization (±10mK)        │
│  • Environmental monitoring                 │
│  • User interface (OLED + buttons)          │
│  • System diagnostics                       │
└─────────────────────────────────────────────┘
       │
┌──────▼──────────────────────────────────────┐
│  POWER SUPPLY BOARD                         │
│  • ±3.3V analog (ultralow noise)            │
│  • 3.3V/1.8V digital                        │
│  • Active filtering                         │
│  • Over-current protection                  │
└─────────────────────────────────────────────┘
```

---

## 📊 Complete System Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Total Board Count** | 4 boards | Plus sensor die |
| **Total Power** | 1.25W | Typical operation |
| **Peak Power** | 2.5W | With TEC cooling |
| **Supply Voltage** | 12V DC | 2A max |
| **Data Rate** | 120 Mbps | 10 fps @ 12-bit |
| **Enclosure Size** | 150×120×80 mm | Aluminum with EMI shielding |
| **Operating Temp** | 10-40°C | Ambient |
| **Prototype Cost** | ~$5,800 | Single unit BOM |

---

## 🔧 Board Details

### 1. Readout Electronics Board

**Purpose:** Interface with 100×100 mechanical sensor array and digitize analog signals

**Key Specifications:**
- **Size:** 100mm × 80mm, 6-layer FR4
- **Analog Frontend:** 100 low-noise charge amplifiers (AD8429)
- **ADC:** 12-bit SAR, 1 MSPS (AD7476)
- **Voltage Reference:** 3.3V ±0.05%, 3ppm/°C (ADR435)
- **Interfaces:** 
  - 100-pin sensor connector (0.5mm pitch)
  - USB 3.0 Type-C output
  - 20-pin expansion header

**Critical Design Features:**
- Guard rings around analog traces (crosstalk <-80 dB)
- Star grounding topology
- Kelvin sensing for voltage reference
- Thermal vias under power devices

**BOM Cost:** ~$850 per board

**Schematic Status:** ⏳ In progress
**Layout Status:** ⏳ Not started

---

### 2. FPGA Processing Board

**Purpose:** Real-time signal processing, frame buffering, and USB communication

**Key Specifications:**
- **Size:** 120mm × 90mm, 8-layer FR4
- **FPGA:** Xilinx Spartan-7 XC7S25 (23K logic cells)
- **Memory:** 4Gbit DDR3 SDRAM @ 1600 MT/s
- **Interface:** USB 3.0 via FT600Q bridge
- **Clock:** 100MHz TCXO (±1ppm stability)

**Firmware Modules:**
1. **Timing Generator** - Pixel clock, CDS phases, frame sync
2. **Frame Buffer** - Circular buffer for 100 frames (15MB)
3. **FPN Correction** - Dark frame subtraction, gain map
4. **Temporal Averaging** - Running average of 100 frames
5. **Bad Pixel Replace** - Median filter for defective pixels
6. **USB Interface** - Bulk transfer protocol, 400 MB/s

**Critical Design Features:**
- Length-matched DDR3 traces (±5mil tolerance)
- 100Ω differential pairs for USB 3.0
- Via stitching around high-speed signals
- Dedicated power planes for FPGA core

**BOM Cost:** ~$95 per board

**Schematic Status:** ⏳ In progress
**Layout Status:** ⏳ Not started
**Firmware Status:** ⏳ Architecture defined

---

### 3. System Control Board

**Purpose:** Temperature control, system monitoring, and auxiliary functions

**Key Specifications:**
- **Size:** 70mm × 50mm, 4-layer FR4
- **MCU:** STM32F407 (168MHz ARM Cortex-M4)
- **Temperature Control:** TEC driver (LTC3633), ±10mK stability
- **Sensors:** Thermistor, humidity, pressure, accelerometer
- **Interface:** OLED display (128×64), pushbuttons, LEDs

**PID Control Loop:**
- **Update Rate:** 10 Hz
- **Parameters:** Kp=100, Ki=10, Kd=1
- **Target Stability:** ±10 mK
- **Temperature Range:** 10-40°C ambient

**Critical Design Features:**
- PID loop runs in real-time OS task
- Non-volatile storage of calibration
- Watchdog timer for fault recovery
- EMI shielding around TEC driver

**BOM Cost:** ~$95 per board

**Schematic Status:** ⏳ In progress
**Layout Status:** ⏳ Not started
**Firmware Status:** ⏳ PID algorithm defined

---

### 4. Power Supply & Distribution Board

**Purpose:** Provide ultra-clean, low-noise power to sensitive analog circuits

**Key Specifications:**
- **Size:** 80mm × 60mm, 4-layer FR4 (2oz copper)
- **Input:** 12V DC, 2A max
- **Analog Rails:** ±3.3V @ 300mA (LT3045/LT3094)
- **Digital Rails:** 3.3V @ 800mA, 1.8V @ 500mA
- **Noise:** <1µV RMS (analog rails)
- **Efficiency:** 85% overall

**Power Budget:**
| Rail | Voltage | Current | Power | Load |
|------|---------|---------|-------|------|
| Analog+ | +3.3V | 200mA | 0.66W | Charge amps |
| Analog- | -3.3V | 100mA | 0.33W | Op-amp rails |
| Digital | 3.3V | 800mA | 2.64W | FPGA, MCU, ADC |
| Sensor | 3.3V | 50mA | 0.17W | Bias current |
| **Total** | | | **3.8W** | |

**Critical Design Features:**
- Separate analog/digital ground planes (star connection)
- Post-regulator RC filtering on analog supplies
- Heavy copper traces (2oz) for power
- Thermal heatsinks on linear regulators

**BOM Cost:** ~$65 per board

**Schematic Status:** ⏳ In progress
**Layout Status:** ⏳ Not started

---

## 🔌 System Interconnections

### Cable Specifications

| Connection | Type | Length | Specification |
|------------|------|--------|---------------|
| Sensor → Readout | High-density flex | 50mm | 100 signal + 20 ground, 0.5mm pitch |
| Readout → FPGA | USB 3.0 | Internal | SuperSpeed, shielded |
| FPGA → Control | I²C + GPIO | 100mm | Twisted pair, 400 kHz |
| Power → All boards | Multi-conductor | Various | 18 AWG, star topology |

### Grounding Strategy
```
Power Board Ground (Star Point)
        │
    ┌───┼───┬───────┐
    │   │   │       │
Analog Digital FPGA Control
Ground Ground Ground Ground
```

---

## 🛠️ Fabrication Requirements

### PCB Manufacturing Specs

**Vendor Recommendations:** PCBWay, JLCPCB, OSH Park

| Board | Layers | Impedance | Copper | Min Via | Min Trace/Space |
|-------|--------|-----------|--------|---------|-----------------|
| Readout | 6 | 50Ω | 1oz | 0.3mm | 0.1mm/0.1mm |
| FPGA | 8 | 50Ω/100Ω | 1oz | 0.25mm | 0.1mm/0.1mm |
| Control | 4 | No | 1oz | 0.3mm | 0.15mm/0.15mm |
| Power | 4 | No | 2oz | 0.4mm | 0.2mm/0.2mm |

**Surface Finish:** ENIG (Electroless Nickel Immersion Gold) for reliability

**Solder Mask:** LPI (Liquid Photo Imageable), green or blue

**Silkscreen:** White, both sides, component references

---

## 📦 Assembly Notes

### Component Sourcing

- **Preferred Distributors:** Digi-Key, Mouser, Arrow
- **Lead Time:** 2-4 weeks for standard components
- **Critical Parts:** Pre-order FPGAs, precision references, TEC modules

### Assembly Process

1. **Solder Paste Stenciling** - Use laser-cut stencil
2. **Pick-and-Place** - Can be done by hand for prototype
3. **Reflow** - Standard lead-free profile (SAC305)
4. **Inspection** - Visual + AOI for critical boards
5. **Hand Soldering** - Through-hole connectors
6. **Testing** - Board-level bring-up before integration

---

## 🧪 Testing Procedure

### Board-Level Tests

**1. Power Board Test (30 minutes)**
- Verify all output voltages ±1%
- Measure ripple noise (<10mV RMS)
- Check efficiency
- Test over-current protection

**2. Control Board Test (45 minutes)**
- Flash firmware via JTAG
- Test temperature sensor readout
- Verify TEC driver (open-loop)
- Check OLED display
- Test all peripherals

**3. FPGA Board Test (60 minutes)**
- Program FPGA bitstream
- Test DDR3 memory (walking 1s/0s)
- Verify USB 3.0 enumeration
- Check clock signals
- Run loopback tests

**4. Readout Board Test (90 minutes)**
- Power up analog circuits
- Verify voltage reference stability
- Test charge amplifier response (sine wave input)
- Check ADC linearity
- Measure crosstalk between channels

### System Integration Test (4 hours)

1. Connect all boards via cables
2. Power up in sequence: Power → Control → FPGA → Readout
3. Load sensor dummy (capacitor array)
4. Capture dark frames
5. Apply test patterns
6. Verify image reconstruction
7. Long-term stability test (overnight)

---

## 📊 Cost Breakdown

### Prototype (Single Unit)

| Item | Cost | Notes |
|------|------|-------|
| **Sensor Die** | $5,000 | MEMS foundry fabrication |
| Readout Board | $850 | BOM + assembly |
| FPGA Board | $95 | BOM + assembly |
| Control Board | $95 | BOM + assembly |
| Power Board | $65 | BOM + assembly |
| PCB Fabrication | $400 | 4 boards, prototyping |
| Assembly | $200 | Hand assembly labor |
| Enclosure | $150 | CNC aluminum |
| Cables & Misc | $100 | Connectors, hardware |
| **Total** | **$6,955** | Single prototype unit |

### Small Production (10 units)

- **Per Unit Cost:** ~$3,200 (sensor amortized)
- **Economies of Scale:** PCBA assembly, bulk component pricing

---

## 🗺️ Development Timeline

### Phase 1: Schematic Capture (Weeks 1-4)
- [ ] Readout board schematic
- [ ] FPGA board schematic
- [ ] Control board schematic
- [ ] Power board schematic
- [ ] Design review

### Phase 2: PCB Layout (Weeks 5-10)
- [ ] Readout board layout
- [ ] FPGA board layout (DDR3 routing critical)
- [ ] Control board layout
- [ ] Power board layout
- [ ] DRC/ERC checks

### Phase 3: Fabrication & Assembly (Weeks 11-14)
- [ ] Submit Gerbers to fab house
- [ ] Order components (BOM)
- [ ] Receive PCBs
- [ ] Assembly & soldering
- [ ] Initial power-on tests

### Phase 4: Firmware Development (Weeks 8-16, parallel)
- [ ] FPGA RTL development
- [ ] MCU firmware (PID control)
- [ ] USB driver software
- [ ] Host PC application

### Phase 5: Integration & Testing (Weeks 15-20)
- [ ] System integration
- [ ] Characterization
- [ ] Optimization
- [ ] Documentation

**Total Timeline:** ~5 months from schematic to working prototype

---

## 📚 Design Files

### File Organization
```
hardware/pcb_designs/
├── readout_board/
│   ├── schematic.pdf
│   ├── layout.kicad_pcb
│   ├── gerbers/
│   └── bom.csv
├── fpga_board/
│   ├── schematic.pdf
│   ├── layout.kicad_pcb
│   ├── gerbers/
│   └── bom.csv
├── control_board/
│   ├── schematic.pdf
│   ├── layout.kicad_pcb
│   ├── gerbers/
│   └── bom.csv
├── power_board/
│   ├── schematic.pdf
│   ├── layout.kicad_pcb
│   ├── gerbers/
│   └── bom.csv
└── system_integration/
    ├── cable_diagrams.pdf
    ├── enclosure_drawing.step
    └── assembly_instructions.pdf
```

---

## 🤝 Contributing

Interested in helping with PCB design? We need:
- [ ] KiCAD schematic capture
- [ ] High-speed PCB layout expertise
- [ ] FPGA firmware development
- [ ] Embedded systems programming
- [ ] Testing and characterization

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

---

## 📧 Contact

Questions about hardware design? Open an issue or contact the hardware team.

---

**Last Updated:** 2024-11-29  
**Status:** Design phase - Schematics in progress  
**Next Milestone:** Complete readout board schematic by 2024-12-15
