import scipy
import math
import tkinter as tk
from tkinter import messagebox

# Completed periodic table data
periodic_table = {
    1: {'symbol': 'H', 'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'electron_configuration': '1s^1'},
    2: {'symbol': 'He', 'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.0026, 'electron_configuration': '1s^2'},
    3: {'symbol': 'Li', 'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94, 'electron_configuration': '[He] 2s^1'},
    4: {'symbol': 'Be', 'name': 'Beryllium', 'atomic_number': 4, 'atomic_mass': 9.0122, 'electron_configuration': '[He] 2s^2'},
    5: {'symbol': 'B', 'name': 'Boron', 'atomic_number': 5, 'atomic_mass': 10.81, 'electron_configuration': '[He] 2s^2 2p^1'},
    6: {'symbol': 'C', 'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'electron_configuration': '[He] 2s^2 2p^2'},
    7: {'symbol': 'N', 'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.007, 'electron_configuration': '[He] 2s^2 2p^3'},
    8: {'symbol': 'O', 'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'electron_configuration': '[He] 2s^2 2p^4'},
    9: {'symbol': 'F', 'name': 'Fluorine', 'atomic_number': 9, 'atomic_mass': 18.998, 'electron_configuration': '[He] 2s^2 2p^5'},
    10: {'symbol': 'Ne', 'name': 'Neon', 'atomic_number': 10, 'atomic_mass': 20.180, 'electron_configuration': '[He] 2s^2 2p^6'},
    11: {'symbol': 'Na', 'name': 'Sodium', 'atomic_number': 11, 'atomic_mass': 22.990, 'electron_configuration': '[Ne] 3s^1'},
    12: {'symbol': 'Mg', 'name': 'Magnesium', 'atomic_number': 12, 'atomic_mass': 24.305, 'electron_configuration': '[Ne] 3s^2'},
    13: {'symbol': 'Al', 'name': 'Aluminum', 'atomic_number': 13, 'atomic_mass': 26.982, 'electron_configuration': '[Ne] 3s^2 3p^1'},
    14: {'symbol': 'Si', 'name': 'Silicon', 'atomic_number': 14, 'atomic_mass': 28.085, 'electron_configuration': '[Ne] 3s^2 3p^2'},
    15: {'symbol': 'P', 'name': 'Phosphorus', 'atomic_number': 15, 'atomic_mass': 30.974, 'electron_configuration': '[Ne] 3s^2 3p^3'},
    16: {'symbol': 'S', 'name': 'Sulfur', 'atomic_number': 16, 'atomic_mass': 32.06, 'electron_configuration': '[Ne] 3s^2 3p^4'},
    17: {'symbol': 'Cl', 'name': 'Chlorine', 'atomic_number': 17, 'atomic_mass': 35.45, 'electron_configuration': '[Ne] 3s^2 3p^5'},
    18: {'symbol': 'Ar', 'name': 'Argon', 'atomic_number': 18, 'atomic_mass': 39.948, 'electron_configuration': '[Ne] 3s^2 3p^6'},
    19: {'symbol': 'K', 'name': 'Potassium', 'atomic_number': 19, 'atomic_mass': 39.098, 'electron_configuration': '[Ar] 4s^1'},
    20: {'symbol': 'Ca', 'name': 'Calcium', 'atomic_number': 20, 'atomic_mass': 40.078, 'electron_configuration': '[Ar] 4s^2'},
    21: {'symbol': 'Sc', 'name': 'Scandium', 'atomic_number': 21, 'atomic_mass': 44.956, 'electron_configuration': '[Ar] 3d^1 4s^2'},
    22: {'symbol': 'Ti', 'name': 'Titanium', 'atomic_number': 22, 'atomic_mass': 47.867, 'electron_configuration': '[Ar] 3d^2 4s^2'},
    23: {'symbol': 'V', 'name': 'Vanadium', 'atomic_number': 23, 'atomic_mass': 50.942, 'electron_configuration': '[Ar] 3d^3 4s^2'},
    24: {'symbol': 'Cr', 'name': 'Chromium', 'atomic_number': 24, 'atomic_mass': 51.996, 'electron_configuration': '[Ar] 3d^5 4s^1'},
    25: {'symbol': 'Mn', 'name': 'Manganese', 'atomic_number': 25, 'atomic_mass': 54.938, 'electron_configuration': '[Ar] 3d^5 4s^2'},
    26: {'symbol': 'Fe', 'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.845, 'electron_configuration': '[Ar] 3d^6 4s^2'},
    27: {'symbol': 'Co', 'name': 'Cobalt', 'atomic_number': 27, 'atomic_mass': 58.933, 'electron_configuration': '[Ar] 3d^7 4s^2'},
    28: {'symbol': 'Ni', 'name': 'Nickel', 'atomic_number': 28, 'atomic_mass': 58.693, 'electron_configuration': '[Ar] 3d^8 4s^2'},
    29: {'symbol': 'Cu', 'name': 'Copper', 'atomic_number': 29, 'atomic_mass': 63.546, 'electron_configuration': '[Ar] 3d^10 4s^1'},
    30: {'symbol': 'Zn', 'name': 'Zinc', 'atomic_number': 30, 'atomic_mass': 65.38, 'electron_configuration': '[Ar] 3d^10 4s^2'},
    31: {'symbol': 'Ga', 'name': 'Gallium', 'atomic_number': 31, 'atomic_mass': 69.723, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^1'},
    32: {'symbol': 'Ge', 'name': 'Germanium', 'atomic_number': 32, 'atomic_mass': 72.63, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^2'},
    33: {'symbol': 'As', 'name': 'Arsenic', 'atomic_number': 33, 'atomic_mass': 74.922, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^3'},
    34: {'symbol': 'Se', 'name': 'Selenium', 'atomic_number': 34, 'atomic_mass': 78.971, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^4'},
    35: {'symbol': 'Br', 'name': 'Bromine', 'atomic_number': 35, 'atomic_mass': 79.904, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^5'},
    36: {'symbol': 'Kr', 'name': 'Krypton', 'atomic_number': 36, 'atomic_mass': 83.798, 'electron_configuration': '[Ar] 3d^10 4s^2 4p^6'},
    37: {'symbol': 'Rb', 'name': 'Rubidium', 'atomic_number': 37, 'atomic_mass': 85.468, 'electron_configuration': '[Kr] 5s^1'},
    38: {'symbol': 'Sr', 'name': 'Strontium', 'atomic_number': 38, 'atomic_mass': 87.62, 'electron_configuration': '[Kr] 5s^2'},
    39: {'symbol': 'Y', 'name': 'Yttrium', 'atomic_number': 39, 'atomic_mass': 88.906, 'electron_configuration': '[Kr] 4d^1 5s^2'},
    40: {'symbol': 'Zr', 'name': 'Zirconium', 'atomic_number': 40, 'atomic_mass': 91.224, 'electron_configuration': '[Kr] 4d^2 5s^2'},
    41: {'symbol': 'Nb', 'name': 'Niobium', 'atomic_number': 41, 'atomic_mass': 92.906, 'electron_configuration': '[Kr] 4d^4 5s^1'},
    42: {'symbol': 'Mo', 'name': 'Molybdenum', 'atomic_number': 42, 'atomic_mass': 95.95, 'electron_configuration': '[Kr] 4d^5 5s^1'},
    43: {'symbol': 'Tc', 'name': 'Technetium', 'atomic_number': 43, 'atomic_mass': 98, 'electron_configuration': '[Kr] 4d^5 5s^2'},
    44: {'symbol': 'Ru', 'name': 'Ruthenium', 'atomic_number': 44, 'atomic_mass': 101.07, 'electron_configuration': '[Kr] 4d^7 5s^1'},
    45: {'symbol': 'Rh', 'name': 'Rhodium', 'atomic_number': 45, 'atomic_mass': 102.91, 'electron_configuration': '[Kr] 4d^8 5s^1'},
    46: {'symbol': 'Pd', 'name': 'Palladium', 'atomic_number': 46, 'atomic_mass': 106.42, 'electron_configuration': '[Kr] 4d^10'},
    47: {'symbol': 'Ag', 'name': 'Silver', 'atomic_number': 47, 'atomic_mass': 107.87, 'electron_configuration': '[Kr] 4d^10 5s^1'},
    48: {'symbol': 'Cd', 'name': 'Cadmium', 'atomic_number': 48, 'atomic_mass': 112.41, 'electron_configuration': '[Kr] 4d^10 5s^2'},
    49: {'symbol': 'In', 'name': 'Indium', 'atomic_number': 49, 'atomic_mass': 114.82, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^1'},
    50: {'symbol': 'Sn', 'name': 'Tin', 'atomic_number': 50, 'atomic_mass': 118.71, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^2'},
    51: {'symbol': 'Sb', 'name': 'Antimony', 'atomic_number': 51, 'atomic_mass': 121.76, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^3'},
    52: {'symbol': 'Te', 'name': 'Tellurium', 'atomic_number': 52, 'atomic_mass': 127.6, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^4'},
    53: {'symbol': 'I', 'name': 'Iodine', 'atomic_number': 53, 'atomic_mass': 126.9, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^5'},
    54: {'symbol': 'Xe', 'name': 'Xenon', 'atomic_number': 54, 'atomic_mass': 131.29, 'electron_configuration': '[Kr] 4d^10 5s^2 5p^6'},
    55: {'symbol': 'Cs', 'name': 'Cesium', 'atomic_number': 55, 'atomic_mass': 132.91, 'electron_configuration': '[Xe] 6s^1'},
    56: {'symbol': 'Ba', 'name': 'Barium', 'atomic_number': 56, 'atomic_mass': 137.33, 'electron_configuration': '[Xe] 6s^2'},
    57: {'symbol': 'La', 'name': 'Lanthanum', 'atomic_number': 57, 'atomic_mass': 138.91, 'electron_configuration': '[Xe] 5d^1 6s^2'},
    58: {'symbol': 'Ce', 'name': 'Cerium', 'atomic_number': 58, 'atomic_mass': 140.12, 'electron_configuration': '[Xe] 4f^1 5d^1 6s^2'},
    59: {'symbol': 'Pr', 'name': 'Praseodymium', 'atomic_number': 59, 'atomic_mass': 140.91, 'electron_configuration': '[Xe] 4f^3 6s^2'},
    60: {'symbol': 'Nd', 'name': 'Neodymium', 'atomic_number': 60, 'atomic_mass': 144.24, 'electron_configuration': '[Xe] 4f^4 6s^2'},
    61: {'symbol': 'Pm', 'name': 'Promethium', 'atomic_number': 61, 'atomic_mass': 145, 'electron_configuration': '[Xe] 4f^5 6s^2'},
    62: {'symbol': 'Sm', 'name': 'Samarium', 'atomic_number': 62, 'atomic_mass': 150.36, 'electron_configuration': '[Xe] 4f^6 6s^2'},
    63: {'symbol': 'Eu', 'name': 'Europium', 'atomic_number': 63, 'atomic_mass': 151.96, 'electron_configuration': '[Xe] 4f^7 6s^2'},
    64: {'symbol': 'Gd', 'name': 'Gadolinium', 'atomic_number': 64, 'atomic_mass': 157.25, 'electron_configuration': '[Xe] 4f^7 5d^1 6s^2'},
    65: {'symbol': 'Tb', 'name': 'Terbium', 'atomic_number': 65, 'atomic_mass': 158.93, 'electron_configuration': '[Xe] 4f^9 6s^2'},
    66: {'symbol': 'Dy', 'name': 'Dysprosium', 'atomic_number': 66, 'atomic_mass': 162.5, 'electron_configuration': '[Xe] 4f^10 6s^2'},
    67: {'symbol': 'Ho', 'name': 'Holmium', 'atomic_number': 67, 'atomic_mass': 164.93, 'electron_configuration': '[Xe] 4f^11 6s^2'},
    68: {'symbol': 'Er', 'name': 'Erbium', 'atomic_number': 68, 'atomic_mass': 167.26, 'electron_configuration': '[Xe] 4f^12 6s^2'},
    69: {'symbol': 'Tm', 'name': 'Thulium', 'atomic_number': 69, 'atomic_mass': 168.93, 'electron_configuration': '[Xe] 4f^13 6s^2'},
    70: {'symbol': 'Yb', 'name': 'Ytterbium', 'atomic_number': 70, 'atomic_mass': 173.05, 'electron_configuration': '[Xe] 4f^14 6s^2'},
    71: {'symbol': 'Lu', 'name': 'Lutetium', 'atomic_number': 71, 'atomic_mass': 174.97, 'electron_configuration': '[Xe] 4f^14 5d^1 6s^2'},
    72: {'symbol': 'Hf', 'name': 'Hafnium', 'atomic_number': 72, 'atomic_mass': 178.49, 'electron_configuration': '[Xe] 4f^14 5d^2 6s^2'},
    73: {'symbol': 'Ta', 'name': 'Tantalum', 'atomic_number': 73, 'atomic_mass': 180.95, 'electron_configuration': '[Xe] 4f^14 5d^3 6s^2'},
    74: {'symbol': 'W', 'name': 'Tungsten', 'atomic_number': 74, 'atomic_mass': 183.84, 'electron_configuration': '[Xe] 4f^14 5d^4 6s^2'},
    75: {'symbol': 'Re', 'name': 'Rhenium', 'atomic_number': 75, 'atomic_mass': 186.21, 'electron_configuration': '[Xe] 4f^14 5d^5 6s^2'},
    76: {'symbol': 'Os', 'name': 'Osmium', 'atomic_number': 76, 'atomic_mass': 190.23, 'electron_configuration': '[Xe] 4f^14 5d^6 6s^2'},
    77: {'symbol': 'Ir', 'name': 'Iridium', 'atomic_number': 77, 'atomic_mass': 192.22, 'electron_configuration': '[Xe] 4f^14 5d^7 6s^2'},
    78: {'symbol': 'Pt', 'name': 'Platinum', 'atomic_number': 78, 'atomic_mass': 195.08, 'electron_configuration': '[Xe] 4f^14 5d^9 6s^1'},
    79: {'symbol': 'Au', 'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 196.97, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^1'},
    80: {'symbol': 'Hg', 'name': 'Mercury', 'atomic_number': 80, 'atomic_mass': 200.59, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2'},
    81: {'symbol': 'Tl', 'name': 'Thallium', 'atomic_number': 81, 'atomic_mass': 204.38, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^1'},
    82: {'symbol': 'Pb', 'name': 'Lead', 'atomic_number': 82, 'atomic_mass': 207.2, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^2'},
    83: {'symbol': 'Bi', 'name': 'Bismuth', 'atomic_number': 83, 'atomic_mass': 208.98, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^3'},
    84: {'symbol': 'Po', 'name': 'Polonium', 'atomic_number': 84, 'atomic_mass': 209, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^4'},
    85: {'symbol': 'At', 'name': 'Astatine', 'atomic_number': 85, 'atomic_mass': 210, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^5'},
    86: {'symbol': 'Rn', 'name': 'Radon', 'atomic_number': 86, 'atomic_mass': 222, 'electron_configuration': '[Xe] 4f^14 5d^10 6s^2 6p^6'},
    87: {'symbol': 'Fr', 'name': 'Francium', 'atomic_number': 87, 'atomic_mass': 223, 'electron_configuration': '[Rn] 7s^1'},
     88: {'symbol': 'Ra', 'name': 'Radium', 'atomic_number': 88, 'atomic_mass': 226, 'electron_configuration': '[Rn] 7s^2'},
     89: {'symbol': 'Ac', 'name': 'Actinium', 'atomic_number': 89, 'atomic_mass': 227, 'electron_configuration': '[Rn] 6d^1 7s^2'},
     90: {'symbol': 'Th', 'name': 'Thorium', 'atomic_number': 90, 'atomic_mass': 232.04, 'electron_configuration': '[Rn] 6d^2 7s^2'},
     91: {'symbol': 'Pa', 'name': 'Protactinium', 'atomic_number': 91, 'atomic_mass': 231.04, 'electron_configuration': '[Rn] 5f^2 6d^1 7s^2'},
     92: {'symbol': 'U', 'name': 'Uranium', 'atomic_number': 92, 'atomic_mass': 238.03, 'electron_configuration': '[Rn] 5f^3 6d^1 7s^2'},
     93: {'symbol': 'Np', 'name': 'Neptunium', 'atomic_number': 93, 'atomic_mass': 237, 'electron_configuration': '[Rn] 5f^4 6d^1 7s^2'},
     94: {'symbol': 'Pu', 'name': 'Plutonium', 'atomic_number': 94, 'atomic_mass': 244, 'electron_configuration': '[Rn] 5f^6 7s^2'},
     95: {'symbol': 'Am', 'name': 'Americium', 'atomic_number': 95, 'atomic_mass': 243, 'electron_configuration': '[Rn] 5f^7 7s^2'},
     96: {'symbol': 'Cm', 'name': 'Curium', 'atomic_number': 96, 'atomic_mass': 247, 'electron_configuration': '[Rn] 5f^7 6d^1 7s^2'},
     97: {'symbol': 'Bk', 'name': 'Berkelium', 'atomic_number': 97, 'atomic_mass': 247, 'electron_configuration': '[Rn] 5f^9 7s^2'},
     98: {'symbol': 'Cf', 'name': 'Californium', 'atomic_number': 98, 'atomic_mass': 251, 'electron_configuration': '[Rn] 5f^10 7s^2'},
     99: {'symbol': 'Es', 'name': 'Einsteinium', 'atomic_number': 99, 'atomic_mass': 252, 'electron_configuration': '[Rn] 5f^11 7s^2'},
     100: {'symbol': 'Fm', 'name': 'Fermium', 'atomic_number': 100, 'atomic_mass': 257, 'electron_configuration': '[Rn] 5f^12 7s^2'},
     101: {'symbol': 'Md', 'name': 'Mendelevium', 'atomic_number': 101, 'atomic_mass': 258, 'electron_configuration': '[Rn] 5f^13 7s^2'},
     102: {'symbol': 'No', 'name': 'Nobelium', 'atomic_number': 102, 'atomic_mass': 259, 'electron_configuration': '[Rn] 5f^14 7s^2'},
     103: {'symbol': 'Lr', 'name': 'Lawrencium', 'atomic_number': 103, 'atomic_mass': 266, 'electron_configuration': '[Rn] 5f^14 7s^2 7p^1'},
     104: {'symbol': 'Rf', 'name': 'Rutherfordium', 'atomic_number': 104, 'atomic_mass': 267, 'electron_configuration': '[Rn] 5f^14 6d^2 7s^2'},
     105: {'symbol': 'Db', 'name': 'Dubnium', 'atomic_number': 105, 'atomic_mass': 268, 'electron_configuration': '[Rn] 5f^14 6d^3 7s^2'},
     106: {'symbol': 'Sg', 'name': 'Seaborgium', 'atomic_number': 106, 'atomic_mass': 269, 'electron_configuration': '[Rn] 5f^14 6d^4 7s^2'},
     107: {'symbol': 'Bh', 'name': 'Bohrium', 'atomic_number': 107, 'atomic_mass': 270, 'electron_configuration': '[Rn] 5f^14 6d^5 7s^2'},
     108: {'symbol': 'Hs', 'name': 'Hassium', 'atomic_number': 108, 'atomic_mass': 277, 'electron_configuration': '[Rn] 5f^14 6d^6 7s^2'},
     109: {'symbol': 'Mt', 'name': 'Meitnerium', 'atomic_number': 109, 'atomic_mass': 278, 'electron_configuration': '[Rn] 5f^14 6d^7 7s^2'},
     110: {'symbol': 'Ds', 'name': 'Darmstadtium', 'atomic_number': 110, 'atomic_mass': 281, 'electron_configuration': '[Rn] 5f^14 6d^9 7s^1'},
     111: {'symbol': 'Rg', 'name': 'Roentgenium', 'atomic_number': 111, 'atomic_mass': 282, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^1'},
     112: {'symbol': 'Cn', 'name': 'Copernicium', 'atomic_number': 112, 'atomic_mass': 285, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2'},
     113: {'symbol': 'Nh', 'name': 'Nihonium', 'atomic_number': 113, 'atomic_mass': 286, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^1'},
     114: {'symbol': 'Fl', 'name': 'Flerovium', 'atomic_number': 114, 'atomic_mass': 289, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^2'},
     115: {'symbol': 'Mc', 'name': 'Moscovium', 'atomic_number': 115, 'atomic_mass': 290, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^3'},
     116: {'symbol': 'Lv', 'name': 'Livermorium', 'atomic_number': 116, 'atomic_mass': 293, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^4'},
     117: {'symbol': 'Ts', 'name': 'Tennessine', 'atomic_number': 117, 'atomic_mass': 294, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^5'},
     118: {'symbol': 'Og', 'name': 'Oganesson', 'atomic_number': 118, 'atomic_mass': 294, 'electron_configuration': '[Rn] 5f^14 6d^10 7s^2 7p^6'}
}
class ChemistryCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Chemistry Calculator")

        self.label = tk.Label(master, text="Calculate reaction rate based on the entered value:")
        self.label.pack()

        self.input_frame = tk.Frame(master)
        self.input_frame.pack()

        # Element Selection
        self.element_label = tk.Label(self.input_frame, text="Select Element:")
        self.element_label.grid(row=0, column=0)

        self.element_var = tk.StringVar(master)
        self.element_var.set("1")  # Default value
        self.element_menu = tk.OptionMenu(self.input_frame, self.element_var, *periodic_table.keys())
        self.element_menu.grid(row=0, column=1)

        # Reaction Type Selection
        self.reaction_type_label = tk.Label(self.input_frame, text="Reaction Type:")
        self.reaction_type_label.grid(row=1, column=0)

        self.reaction_type_var = tk.StringVar(master)
        self.reaction_type_var.set("First Order")  # Default value
        self.reaction_type_menu = tk.OptionMenu(self.input_frame, self.reaction_type_var, "First Order", "Second Order", "Third Order")
        self.reaction_type_menu.grid(row=1, column=1)

        # Calculation Type Selection
        self.calculation_type_label = tk.Label(self.input_frame, text="Calculation Type:")
        self.calculation_type_label.grid(row=2, column=0)

        self.calculation_type_var = tk.StringVar(master)
        self.calculation_type_var.set("Molecular Weight Calculation")  # Default value
        self.calculation_type_menu = tk.OptionMenu(self.input_frame, self.calculation_type_var, "Molecular Weight Calculation", "Molarity Calculation", "pH Calculation", "Dilution Calculation", "Stoichiometry Calculation", "Equilibrium Constant Calculation")
        self.calculation_type_menu.grid(row=2, column=1)

        # Add Data Button
        self.add_data_button = tk.Button(self.input_frame, text="Add Data", command=self.add_data)
        self.add_data_button.grid(row=0, column=2)

        # Calculate Button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.data = []

    def add_data(self):
        element_number = int(self.element_var.get())
        element_info = periodic_table[element_number]
        messagebox.showinfo("Selected Element", f"{element_info['name']} ({element_info['symbol']}) selected.\nAtomic Number: {element_info['atomic_number']}\nAtomic Mass: {element_info['atomic_mass']} u\nElectron Configuration: {element_info['electron_configuration']}")

    def calculate(self):
        calculation_type = self.calculation_type_var.get()

        if calculation_type == "Molecular Weight Calculation":
            self.calculate_molecular_weight()
        elif calculation_type == "Molarity Calculation":
            self.calculate_molarity()
        elif calculation_type == "pH Calculation":
            self.calculate_ph()
        elif calculation_type == "Dilution Calculation":
            self.calculate_dilution()
        elif calculation_type == "Stoichiometry Calculation":
            self.calculate_stoichiometry()
        elif calculation_type == "Equilibrium Constant Calculation":
            self.calculate_equilibrium_constant()

    def calculate_molecular_weight(self):
        element_number = int(self.element_var.get())
        element_info = periodic_table[element_number]
        messagebox.showinfo("Molecular Weight", f"Molecular weight of {element_info['name']} ({element_info['symbol']}) is {element_info['atomic_mass']} u.")

    def calculate_molarity(self):
        # Assuming user inputs volume of solution in liters and mass of solute in grams
        volume = float(input("Enter volume of solution in liters: "))
        mass = float(input("Enter mass of solute in grams: "))
        molar_mass = float(input("Enter molar mass of solute in g/mol: "))
        molarity = mass / (volume * molar_mass)
        messagebox.showinfo("Molarity", f"Molarity of the solution is {molarity} mol/L.")

    def calculate_ph(self):
        concentration = float(input("Enter concentration of H+ ions in mol/L: "))
        ph = -math.log10(concentration)
        messagebox.showinfo("pH", f"The pH of the solution is {ph}.")

    def calculate_dilution(self):
        initial_concentration = float(input("Enter initial concentration in mol/L: "))
        initial_volume = float(input("Enter initial volume in liters: "))
        final_volume = float(input("Enter final volume in liters: "))
        final_concentration = (initial_concentration * initial_volume) / final_volume
        messagebox.showinfo("Dilution", f"The final concentration after dilution is {final_concentration} mol/L.")

    def calculate_stoichiometry(self):
        try:
            reactant_coefficient = int(self.reactant_coefficient_entry.get())
            product_coefficient = int(self.product_coefficient_entry.get())
            reactant_moles = float(self.reactant_moles_entry.get())
            product_moles = float(self.product_moles_entry.get())

            if reactant_coefficient <= 0 or product_coefficient <= 0:
                messagebox.showerror("Error", "Coefficients should be greater than 0.")
            elif reactant_moles / reactant_coefficient == product_moles / product_coefficient:
                messagebox.showinfo("Stoichiometry", "The reaction is stoichiometrically balanced.")
            else:
                messagebox.showinfo("Stoichiometry", "The reaction is not stoichiometrically balanced.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid coefficients and moles.")

    def calculate_equilibrium_constant(self):
        # Assuming user inputs concentrations of reactants and products at equilibrium
        reactant_concentration = float(input("Enter concentration of reactant at equilibrium: "))
        product_concentration = float(input("Enter concentration of product at equilibrium: "))
        equilibrium_constant = product_concentration / reactant_concentration
        messagebox.showinfo("Equilibrium Constant", f"The equilibrium constant is {equilibrium_constant}.")
root = tk.Tk()
app = ChemistryCalculator(root)
root.mainloop()
