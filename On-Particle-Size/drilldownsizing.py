'''
Author:   Richard D. Pohl
Date:     Aprile, 2024
Summary:  Calculate and report hypothesized sizes and masses of prejected
          Universal Matter objects
'''

import prtfunction as prt

def drill_down_sizing(item_refs_list, fp):
    """Version 1.0.0: Initial Release"""

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    asteroid:  int = 4
    planet:    int = 3
    sun:       int = 2
    solar_sys: int = 1
    galaxy:    int = 0

    level_one:   int = asteroid
    level_two:   int = planet
    level_three: int = sun
    prime:       int = solar_sys

    #Relative factored size/mass of {f} as hydrogen compared to the galaxy
    f_size_factor = item_refs_list[hydrogen].size / item_refs_list[galaxy].size
    f_mass_factor = item_refs_list[hydrogen].mass / item_refs_list[galaxy].mass
    f_size = item_refs_list[hydrogen].size * f_size_factor
    f_mass = item_refs_list[hydrogen].mass * f_mass_factor

    prtstr = "Summary of Calculated Projections by Size and Mass of Universal Matter Objects\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")
    prt.prt_function(fp, f"The size of a particle of {{f}} is{' ':>23}{f_size:2.3e}{' ':>8}and the mass is {f_mass:2.3e}\n")

    #Relative size and and mass of the three levels of Composite Particles
    #The smallest, Level I
    lvl_1_cp_size_factor = item_refs_list[level_one].size / item_refs_list[galaxy].size
    lvl_1_cp_mass_factor = item_refs_list[level_one].mass / item_refs_list[galaxy].mass
    lvl_1_cp_size = item_refs_list[hydrogen].size * lvl_1_cp_size_factor
    lvl_1_cp_mass = item_refs_list[hydrogen].mass * lvl_1_cp_mass_factor

    # Mid point, Level II
    lvl_2_cp_size_factor = item_refs_list[level_two].size / item_refs_list[galaxy].size
    lvl_2_cp_mass_factor = item_refs_list[level_two].mass / item_refs_list[galaxy].mass
    lvl_2_cp_size = item_refs_list[hydrogen].size * lvl_2_cp_size_factor
    lvl_2_cp_mass = item_refs_list[hydrogen].mass * lvl_2_cp_mass_factor

    # Biggest point, Level III
    lvl_3_cp_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size
    lvl_3_cp_mass_factor = item_refs_list[level_three].mass / item_refs_list[galaxy].mass
    lvl_3_cp_size = item_refs_list[hydrogen].size * lvl_3_cp_size_factor
    lvl_3_cp_mass = item_refs_list[hydrogen].mass * lvl_3_cp_mass_factor

    prt.prt_function(fp, f"The size of a Level I Composite Particle is {' ':>11}{lvl_1_cp_size:5.3e}{' ':>8}and the mass is {lvl_1_cp_mass:5.3e}\n")
    prt.prt_function(fp, f"The size of a Level II Composite Particle is {' ':>10}{lvl_2_cp_size:5.3e}{' ':>8}and the mass is {lvl_2_cp_mass:5.3e}\n")
    prt.prt_function(fp, f"The size of a Level III Composite Particle is {' ':>9}{lvl_3_cp_size:5.3e}{' ':>8}and the mass is {lvl_3_cp_mass:5.3e}\n")

    #Relative factored size/mass of Prime Particle as our sun compared to the galaxy
    prime_size_factor = item_refs_list[prime].size / item_refs_list[galaxy].size
    prime_mass_factor = item_refs_list[prime].mass / item_refs_list[galaxy].mass
    prime_size = item_refs_list[hydrogen].size * prime_size_factor
    prime_mass = item_refs_list[hydrogen].mass * prime_mass_factor

    prt.prt_function(fp, f"The size of a Prime Particle is {' ':>23}{prime_size:5.3e}{' ':>8}and the mass is {prime_mass:5.3e}\n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    return item_refs_list
