#!/usr/bin/env python3
"""
Calibration Tools for Mechanical Retina
Tools for characterizing and calibrating the mechanical response
"""

import numpy as np
from scipy.optimize import curve_fit

class MechanicalCalibrator:
    def __init__(self):
        self.response_curve = None
        self.cross_talk_matrix = None
        
    def measure_response_curve(self, powers, displacements):
        """Characterize the mechanical response to optical power"""
        def model(power, a, b, c):
            return a * power + b * power**2 + c
            
        params, _ = curve_fit(model, powers, displacements)
        self.response_curve = params
        return params
    
    def measure_cross_talk(self, excitation_patterns, response_patterns):
        """Characterize cross-talk between adjacent pixels"""
        # Build cross-talk matrix
        self.cross_talk_matrix = np.linalg.pinv(excitation_patterns) @ response_patterns
        return self.cross_talk_matrix
    
    def correct_cross_talk(self, raw_displacements):
        """Apply cross-talk correction to raw displacement data"""
        if self.cross_talk_matrix is not None:
            corrected = raw_displacements @ np.linalg.inv(self.cross_talk_matrix)
            return corrected
        return raw_displacements
