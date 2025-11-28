#!/usr/bin/env python3
"""
Kalman Filter for Mechanical Retina Noise Reduction
Advanced filtering to extract signal from noisy mechanical measurements
"""

import numpy as np
from pykalman import KalmanFilter

class MechanicalKalmanFilter:
    def __init__(self, process_noise=1e-15, measurement_noise=1e-12):
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        self.kf = None
        
    def setup_filter(self, initial_state=0.0):
        """Set up Kalman filter parameters"""
        self.kf = KalmanFilter(
            transition_matrices=[1],
            observation_matrices=[1],
            initial_state_mean=initial_state,
            initial_state_covariance=1,
            transition_covariance=self.process_noise,
            observation_covariance=self.measurement_noise
        )
        
    def filter_signal(self, measurements):
        """Apply Kalman filter to noisy mechanical measurements"""
        if self.kf is None:
            self.setup_filter()
            
        state_means, state_covariances = self.kf.filter(measurements)
        return state_means.flatten()

def test_kalman_filter():
    """Test Kalman filter on simulated noisy data"""
    filter = MechanicalKalmanFilter()
    
    # Generate simulated signal with noise
    t = np.linspace(0, 10, 1000)
    true_signal = np.sin(2 * np.pi * t) * 1e-12  # True mechanical displacement
    noise = np.random.normal(0, 1e-12, len(t))   # Measurement noise
    measurements = true_signal + noise
    
    # Apply Kalman filter
    filtered_signal = filter.filter_signal(measurements)
    
    print(f"Original signal std: {np.std(measurements):.2e}")
    print(f"Filtered signal std: {np.std(filtered_signal):.2e}")
    
    return true_signal, measurements, filtered_signal

if __name__ == "__main__":
    test_kalman_filter()
