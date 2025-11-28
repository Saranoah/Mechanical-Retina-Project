#!/usr/bin/env python3
"""
Test Signal Processing Algorithms
Validate image reconstruction and noise filtering
"""

import unittest
import numpy as np
from data_analysis.noise_filtering.kalman_filter import MechanicalKalmanFilter

class TestSignalProcessing(unittest.TestCase):
    
    def test_kalman_filter_convergence(self):
        """Test that Kalman filter reduces noise"""
        # Create noisy signal
        t = np.linspace(0, 10, 1000)
        true_signal = np.sin(2 * np.pi * t) * 1e-12
        noise = np.random.normal(0, 1e-12, len(t))
        measurements = true_signal + noise
        
        # Apply filter
        filter = MechanicalKalmanFilter()
        filtered = filter.filter_signal(measurements)
        
        # Filter should reduce variance
        original_variance = np.var(measurements - true_signal)
        filtered_variance = np.var(filtered - true_signal)
        
        self.assertLess(filtered_variance, original_variance)
    
    def test_pattern_recognition_consistency(self):
        """Test that pattern recognition produces consistent results"""
        from data_analysis.image_reconstruction.pattern_recognition import MechanicalPatternRecognizer
        
        recognizer = MechanicalPatternRecognizer()
        test_data = np.random.randn(100, 100) * 1e-12
        
        labels1, centers1 = recognizer.recognize_patterns(test_data, n_patterns=3)
        labels2, centers2 = recognizer.recognize_patterns(test_data, n_patterns=3)
        
        # Should produce same number of patterns
        self.assertEqual(len(centers1), len(centers2))

if __name__ == "__main__":
    unittest.main()
