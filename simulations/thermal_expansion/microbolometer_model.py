#!/usr/bin/env python3
"""
Microbolometer-based Mechanical Detection Model
Simulate photon detection via thermal expansion
"""

import numpy as np
import matplotlib.pyplot as plt

class MicrobolometerModel:
    def __init__(self):
        self.thermal_expansion_coeff = 2.6e-6  # Silicon α (1/K)
        self.youngs_modulus = 170e9  # Pa
        
    def thermal_displacement(self, power, absorption=0.8, thermal_resistance=1e6):
        """Calculate displacement from absorbed optical power"""
        # Power → Temperature → Expansion → Displacement
        delta_temp = power * absorption * thermal_resistance
        displacement = self.thermal_expansion_coeff * delta_temp  # Strain
        return displacement
    
    def simulate_response(self):
        """Simulate response to various power levels"""
        powers = np.logspace(-15, -6, 50)  # 1fW to 1μW
        displacements = [self.thermal_displacement(p) for p in powers]
        
        plt.figure(figsize=(10, 6))
        plt.loglog(powers, displacements)
        plt.xlabel('Incident Power (W)')
        plt.ylabel('Thermal Displacement (m)')
        plt.title('Microbolometer Mechanical Response')
        plt.grid(True)
        plt.savefig('microbolometer_response.png')
        plt.show()

if __name__ == "__main__":
    model = MicrobolometerModel()
    model.simulate_response()
