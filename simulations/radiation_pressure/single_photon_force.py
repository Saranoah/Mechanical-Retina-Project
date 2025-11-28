#!/usr/bin/env python3
"""
Single Photon Force Simulation
Calculate whether we can detect a single photon via radiation pressure
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

class PhotonDetector:
    def __init__(self):
        self.h = constants.h
        self.c = constants.c
        self.kb = constants.k
        
    def photon_momentum(self, wavelength):
        """Calculate momentum of a single photon"""
        return self.h / wavelength
    
    def radiation_pressure_force(self, power, wavelength, reflective=True):
        """Calculate force from photon stream"""
        factor = 2 if reflective else 1  # Reflection doubles momentum transfer
        return factor * power / self.c
    
    def thermal_noise_force(self, temperature, bandwidth, mechanical_frequency, Q_factor=1000):
        """Calculate thermal noise force using fluctuation-dissipation theorem"""
        return np.sqrt(4 * self.kb * temperature * mechanical_frequency / (Q_factor * bandwidth))
    
    def minimum_detectable_power(self, temperature=300, wavelength=550e-9):
        """Calculate minimum detectable optical power"""
        photon_energy = self.h * self.c / wavelength
        thermal_energy = self.kb * temperature
        
        print(f"Photon energy (550nm): {photon_energy:.2e} J")
        print(f"Thermal energy (room temp): {thermal_energy:.2e} J")
        print(f"Ratio (thermal/photon): {thermal_energy/photon_energy:.2e}")
        
        return thermal_energy / photon_energy

def main():
    detector = PhotonDetector()
    
    # Single photon properties
    wavelength = 550e-9  # Green light
    p_photon = detector.photon_momentum(wavelength)
    print(f"Single photon momentum: {p_photon:.2e} kg·m/s")
    
    # Force from reasonable light power
    power = 1e-12  # 1 picoWatt
    force = detector.radiation_pressure_force(power, wavelength)
    print(f"Force from {power:.0e} W: {force:.2e} N")
    
    # Thermal noise comparison
    thermal_force = detector.thermal_noise_force(300, 1000, 10000)
    print(f"Thermal noise force: {thermal_force:.2e} N")
    print(f"Signal-to-Noise ratio: {force/thermal_force:.2f}")
    
    # Minimum detectable power
    min_power = detector.minimum_detectable_power()
    print(f"\nTheoretical minimum: {min_power:.2e} photons/sec needed to overcome thermal noise")

if __name__ == "__main__":
    main()
