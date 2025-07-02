'''
Title:    On the Particle Sizing and Masses of Universal Matter Objects
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Project Main Function
          Sections work to build Universal Matter objects and report on
          details related to such objects 
'''

from pathlib import Path

import astronomyobjects as ast
import drilldownsizing as dd
import levelonesizeandmass as lvlI
import leveltwosizeandmass as lvlII
import levelthreesizeandmass as lvlIII
import primesizeandmass as prime
import atom as atm

def main():
    """Version 1.0.0: Initial Release"""

    #Define report file path as befits your environment
    #this code puts the sizing_output.txt report file in the same directory as main.py
    current_working_directory = Path(__file__).resolve().parent
    file_pointer = str(current_working_directory) + "/sizing_output.txt"

    rc = open(file_pointer, 'w', encoding='UTF-8')  #empty report file
    rc.close()

    item_refs_list = []
    item_pass_list = []

    item_refs_list = ast.astronomy_objects(item_refs_list, file_pointer)
    item_refs_list = dd.drill_down_sizing(item_refs_list, file_pointer)
    item_refs_list, item_pass_list = lvlI.level_1_size_and_mass(item_refs_list, item_pass_list, file_pointer)
    item_refs_list, item_pass_list = lvlII.level_2_size_and_mass(item_refs_list, item_pass_list, file_pointer)
    item_refs_list, item_pass_list = lvlIII.level_3_size_and_mass(item_refs_list, item_pass_list, file_pointer)
    item_refs_list, item_pass_list = prime.prime_size_and_mass(item_refs_list, item_pass_list, file_pointer)
    item_refs_list, item_pass_list = atm.build_atom(item_refs_list, item_pass_list, file_pointer)

if __name__ == '__main__' :
    main()
