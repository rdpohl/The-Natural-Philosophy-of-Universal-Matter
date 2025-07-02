'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Houses list classes and utilty function
'''

import sys

#reference item list of known astronomical objects
class RefItems:
    """Version 1.0.0: Initial Release"""

    def __init__(self, name, size, mass, s_factor, m_factor):
        self.name = name
        self.size = size
        self.mass = mass
        self.s_factor = s_factor
        self.m_factor = m_factor

#inter-function values needed for and produced by function calls
class PassItems:
    """Version 1.0.0: Initial Release"""

    def __init__(self, name, size, mass):
        self.name = name
        self.size = size
        self.mass = mass

def find_record(list_name, find_str):
    """Version 1.0.0: Initial Release"""

    found_bool = False

    if len(list_name) > 0:
        cntr = 0
    else:
        print(f"Find string: {find_str} Not Found")
        sys.exit("Pass Reference Not Found")

    for x in list_name:
        if x.name == find_str:
            found_bool = True
            break
        cntr  += 1

    if found_bool:
        return cntr
    else:
        print(f"Find string: '{find_str}' Not Found")
        sys.exit("Pass Reference Not Found")
