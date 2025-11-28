# Mechanical Retina Project

A revolutionary photon detection system using mechanical principles instead of semiconductor photodiodes.

## The Vision
Create a biologically-inspired retina that detects photons through physical displacement, radiation pressure, or photomechanical effects rather than electronic conversion.

## Current Status
🚧 **Theoretical Research Phase** - Proving feasibility through simulation

## Quick Start
```bash
# Run basic radiation pressure simulation
cd simulations/radiation_pressure
python single_photon_force.py

Approach
Phase 1: Theoretical feasibility & simulation

Phase 2: MEMS design & material selection

Phase 3: Prototype fabrication

Phase 4: System integration & testing

Contributing
We welcome physicists, MEMS engineers, optical engineers, and computational researchers.


## 2. docs/CONCEPT.md
```markdown
# Mechanical Retina: Core Concept

## Overview
The Mechanical Retina project aims to develop a novel photon detection system that uses mechanical displacement rather than electronic photocurrent to capture visual information.

## Detection Principles

### 1. Radiation Pressure Direct Detection
- Uses photon momentum transfer: p = h/λ
- Reflective surfaces experience force: F = 2P/c
- Primary challenge: Overcoming thermal noise at room temperature

### 2. Photothermal Mechanical Transduction  
- Photon energy → Thermal expansion → Mechanical displacement
- More feasible approach for room temperature operation
- Trade-off: Lower temporal resolution for higher sensitivity

### 3. Photomechanical Material Response
- Materials that undergo conformational changes under photon absorption
- Examples: Azobenzene polymers, diarylethene crystals
- Direct photon-to-mechanical energy conversion

## System Architecture
- **Optical Layer**: Focusing system and wavelength selection
- **Mechanical Layer**: MEMS/NEMS sensor array
- **Readout Layer**: Displacement detection and signal processing
- **Reconstruction Layer**: Image formation algorithms

