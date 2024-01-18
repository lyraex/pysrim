"""Binding energies for target atoms.

This file contains a dictionary of element-specific binding energies (in eV)
for use in TRIM calculations. Included are SRIM's suggested (i.e., default)
values for each element's:
- Displacement energy (the energy that a recoil needs to overcome the
  lattice forces and move more than one atomic spacing away from its original
  site).
- Lattice binding energy (the energy that every recoiling atoms loses
  when it leaves its lattice site and recoils into the target).
- Surface binding energy (the energy that target atoms must overcome to
  leave the surface of the target).

A more complete description of these quantities can be found in the TRIM Help
window.
"""

# displacement, lattice, & surface binding energies (in eV) for each element
binding_energy = {
    "H": {
        "Displacement (eV)": 10.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "He": {
        "Displacement (eV)": 5.0,
        "Lattice (eV)": 1.0,
        "Surface (eV)": 2.0,
    },
    "Li": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.67,
    },
    "Be": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.38,
    },
    "B": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.73,
    },
    "C": {
        "Displacement (eV)": 28.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 7.41,
    },
    "N": {
        "Displacement (eV)": 28.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "O": {
        "Displacement (eV)": 28.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "F": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Ne": {
        "Displacement (eV)": 5.0,
        "Lattice (eV)": 1.0,
        "Surface (eV)": 2.0,
    },
    "Na": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.12,
    },
    "Mg": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.54,
    },
    "Al": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.36,
    },
    "Si": {
        "Displacement (eV)": 15.0,
        "Lattice (eV)": 2.0,
        "Surface (eV)": 4.7,
    },
    "P": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.27,
    },
    "S": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.88,
    },
    "Cl": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Ar": {
        "Displacement (eV)": 5.0,
        "Lattice (eV)": 1.0,
        "Surface (eV)": 2.0,
    },
    "K": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 0.93,
    },
    "Ca": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.83,
    },
    "Sc": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.49,
    },
    "Ti": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.89,
    },
    "V": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.33,
    },
    "Cr": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.12,
    },
    "Mn": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.98,
    },
    "Fe": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.34,
    },
    "Co": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.43,
    },
    "Ni": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.46,
    },
    "Cu": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.52,
    },
    "Zn": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.35,
    },
    "Ga": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.82,
    },
    "Ge": {
        "Displacement (eV)": 15.0,
        "Lattice (eV)": 2.0,
        "Surface (eV)": 3.88,
    },
    "As": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.26,
    },
    "Se": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.14,
    },
    "Br": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Kr": {
        "Displacement (eV)": 5.0,
        "Lattice (eV)": 1.0,
        "Surface (eV)": 2.0,
    },
    "Rb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 0.86,
    },
    "Sr": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.7,
    },
    "Y": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.24,
    },
    "Zr": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 6.33,
    },
    "Nb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 7.59,
    },
    "Mo": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 6.83,
    },
    "Tc": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Ru": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 6.69,
    },
    "Rh": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.78,
    },
    "Pd": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.91,
    },
    "Ag": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.97,
    },
    "Cd": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.16,
    },
    "In": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.49,
    },
    "Sn": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.12,
    },
    "Sb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.72,
    },
    "Te": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.02,
    },
    "I": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Cs": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 0.81,
    },
    "Ba": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.84,
    },
    "La": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.42,
    },
    "Ce": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.23,
    },
    "Pr": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.71,
    },
    "Nd": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.28,
    },
    "Pm": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Sm": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.16,
    },
    "Eu": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.85,
    },
    "Gd": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.57,
    },
    "Tb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.81,
    },
    "Dy": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.89,
    },
    "Ho": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.05,
    },
    "Er": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.05,
    },
    "Tm": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.52,
    },
    "Yb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.74,
    },
    "Lu": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 4.29,
    },
    "Hf": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 6.31,
    },
    "Ta": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 8.1,
    },
    "W": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 8.68,
    },
    "Re": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 8.09,
    },
    "Os": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 8.13,
    },
    "Ir": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 6.9,
    },
    "Pt": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.86,
    },
    "Au": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 3.8,
    },
    "Hg": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 0.64,
    },
    "Tl": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.88,
    },
    "Pb": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.03,
    },
    "Bi": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.17,
    },
    "Po": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 1.5,
    },
    "At": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Rn": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Fr": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Ra": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Ac": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "Th": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.93,
    },
    "Pa": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 2.0,
    },
    "U": {
        "Displacement (eV)": 25.0,
        "Lattice (eV)": 3.0,
        "Surface (eV)": 5.42,
    },
}
