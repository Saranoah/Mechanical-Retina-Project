#!/usr/bin/env python3
"""
Thermal Noise Analysis for Mechanical Retina
Analyze the impact of thermal noise on detection sensitivity
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

class ThermalNoiseAnalyzer:
    def __init__(self):
        self.kb = constants.k
        self.h = constants.h
        
    def thermal_displacement(self, temp, spring_constant, frequency, Q=1000):
        """Calculate RMS displacement from thermal noise"""
        return np.sqrt(self.kb * temp / (spring_constant * (1 + (frequency * Q)**2)))
    
    def plot_temperature_sensitivity(self):
        """Plot how temperature affects minimum detectable force"""
        temps = np.linspace(0.1, 300, 100)  # From cryogenic to room temp
        k = 1e-3  # Spring constant N/m
        
        thermal_forces = np.sqrt(4 * self.kb * temps * k)
        
        plt.figure(figsize=(10, 6))
        plt.semilogy(temps, thermal_forces)
        plt.xlabel('Temperature (K)')
        plt.ylabel('Thermal Noise Force (N/√Hz)')
        plt.title('Thermal Noise vs Temperature')
        plt.grid(True)
        plt.savefig('thermal_noise_vs_temperature.png')
        plt.show()

if __name__ == "__main__":
    analyzer = ThermalNoiseAnalyzer()
    analyzer.plot_temperature_sensitivity()
