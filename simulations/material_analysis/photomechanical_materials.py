#!/usr/bin/env python3
"""
Photomechanical Materials Analysis
Analyze materials that change shape under photon absorption
"""

class PhotomechanicalMaterial:
    def __init__(self, name, strain_per_photon, response_time, wavelength_sensitivity):
        self.name = name
        self.strain_per_photon = strain_per_photon  # m/photon
        self.response_time = response_time  # seconds
        self.wavelength_sensitivity = wavelength_sensitivity  # meters
        
    def calculate_response(self, photon_flux):
        """Calculate mechanical response to photon flux"""
        return photon_flux * self.strain_per_photon

# Common photomechanical materials
materials = {
    'azobenzene': PhotomechanicalMaterial('Azobenzene Polymer', 1e-12, 1e-3, 450e-9),
    'diarylethene': PhotomechanicalMaterial('Diarylethene Crystal', 1e-13, 1e-6, 550e-9),
    'graphene_oxide': PhotomechanicalMaterial('Graphene Oxide', 1e-14, 1e-9, 'Broadband')
}

def analyze_materials():
    """Compare different photomechanical materials"""
    print("Photomechanical Materials Analysis")
    print("=" * 50)
    for name, material in materials.items():
        response = material.calculate_response(1e15)  # 10^15 photons/s
        print(f"{material.name}:")
        print(f"  Strain per photon: {material.strain_per_photon:.1e} m/photon")
        print(f"  Response to 1mW @550nm: {response:.1e} m")
        print(f"  Response time: {material.response_time:.1e} s")
        print()

if __name__ == "__main__":
    analyze_materials()
