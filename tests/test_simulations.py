#!/usr/bin/env python3
"""
Test Suite for Mechanical Retina Simulations
Validate simulation accuracy and performance
"""

import unittest
import numpy as np
from simulations.radiation_pressure.single_photon_force import PhotonDetector
from simulations.signal_processing.image_reconstruction import MechanicalImageReconstructor

class TestMechanicalRetina(unittest.TestCase):
    
    def setUp(self):
        self.detector = PhotonDetector()
        self.reconstructor = MechanicalImageReconstructor()
    
    def test_photon_momentum_calculation(self):
        """Test photon momentum calculation for various wavelengths"""
        wavelengths = [400e-9, 550e-9, 700e-9]  # UV, Green, IR
        
        for wavelength in wavelengths:
            momentum = self.detector.photon_momentum(wavelength)
            self.assertGreater(momentum, 0)
            self.assertLess(momentum, 1e-26)  # Should be very small
    
    def test_radiation_pressure_force(self):
        """Test radiation pressure force calculation"""
        power = 1e-9  # 1 nW
        wavelength = 550e-9
        force = self.detector.radiation_pressure_force(power, wavelength)
        
        # Force should be positive and very small
        self.assertGreater(force, 0)
        self.assertLess(force, 1e-15)
    
    def test_image_reconstruction_shape(self):
        """Test that reconstruction maintains correct shape"""
        test_input = np.random.random((100, 100)) * 1e-12
        output = self.reconstructor.reconstruct_from_displacements(test_input)
        
        self.assertEqual(output.shape, (100, 100))
    
    def test_thermal_noise_consistency(self):
        """Test thermal noise calculation for various temperatures"""
        temperatures = [4, 77, 300]  # Cryogenic, LN2, Room temp
        
        for temp in temperatures:
            noise = self.detector.thermal_noise_force(temp, 1000, 10000)
            self.assertGreater(noise, 0)
            # Noise should increase with temperature
            if temp > 4:
                self.assertGreater(noise, 1e-20)

def run_tests():
    """Run all tests"""
    unittest.main(verbosity=2)

if __name__ == "__main__":
    run_tests()
