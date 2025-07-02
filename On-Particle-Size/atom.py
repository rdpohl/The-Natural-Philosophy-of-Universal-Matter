'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  This module puts the full build together forming a hydrogen atom 
'''

import refitems as ri
import prtfunction as prt

def build_atom(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_eff_number   = ri.find_record(item_pass_list, 'Prime Effective')
    item_eff_size     = item_pass_list[item_eff_number].size
    item_eff_mass     = item_pass_list[item_eff_number].mass
    item_ineff_number = ri.find_record(item_pass_list, 'Prime Ineffective')
    item_ineff_size   = item_pass_list[item_ineff_number].size
    item_ineff_mass   = item_pass_list[item_ineff_number].mass

    lvl3_eff_number   = ri.find_record(item_pass_list, 'Level III Effective')
    lvl3_eff_size     = item_pass_list[lvl3_eff_number].size
    lvl3_eff_mass     = item_pass_list[lvl3_eff_number].mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    #let's put all of the build info together
    #this is all calculated values
    prtstr = "Hydrogen Atom Summary of Size and Mass\n"
    prt.prt_function(fp, prtstr)

    #debug
    #for x in item_pass_list:
    #    prt.prt_function(fp, f"name {x.name} size {x.size:5.3e} mass {x.mass:5.3e} \n")

    prtstr = "Prime Particle Summary\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, f"Prime Effective {' ':>34}size {item_eff_size:5.3e}{' ':>19}mass {item_eff_mass:5.3e}\n")
    prt.prt_function(fp, f"Prime Ineffective {' ':>32}size {item_ineff_size:5.3e}{' ':>19}mass {item_ineff_mass:5.3e}\n")
    prt.prt_function(fp, f"Prime Effective {' ':>34}size {item_eff_size:5.3e}{' ':>19}mass {item_eff_mass:5.3e}\n")
    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")

    tally_size = item_eff_size + item_ineff_size + item_eff_size
    tally_mass = item_eff_mass + item_ineff_mass + item_eff_mass
    prt.prt_function(fp, f"Prime Tally {' ':>43}{tally_size:5.3e}{' ':>24}{tally_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")

    #calculate number of Composite Particles (CP) circulating around the three prime particles
    num_level_1:  float = 1.00e+09
    num_level_2:  float = 1.00e+06

    item_1_number = ri.find_record(item_pass_list, 'Level I')
    item_1_size   = item_pass_list[item_1_number].size
    item_1_mass   = item_pass_list[item_1_number].mass

    addl_lvl_1_size: float = num_level_1 * item_1_size
    addl_lvl_1_mass: float = num_level_1 * item_1_mass

    prt.prt_function(fp, f"Conducted Level 1 {' ':>32}size {addl_lvl_1_size:5.3e}{' ':>19}mass {addl_lvl_1_mass:5.3e}\n")

    item_2_number = ri.find_record(item_pass_list, 'Level II')
    item_2_size   = item_pass_list[item_2_number].size
    item_2_mass   = item_pass_list[item_2_number].mass

    addl_lvl_2_size: float = num_level_2 * item_2_size
    addl_lvl_2_mass: float = num_level_2 * item_2_mass

    prt.prt_function(fp, f"Conducted Level 2 {' ':>32}size {addl_lvl_2_size:5.3e}{' ':>19}mass {addl_lvl_2_mass:5.3e}\n")

    #calculate number of CP conducted between first Eff & the Ineff and between same Ineff &
    #    second Eff (two join points) that is the proton
    num_prime_conducted_size:  float = (addl_lvl_1_size + addl_lvl_2_size) * 2 #doubled for two points of contact
    num_prime_conducted_mass:  float = (addl_lvl_1_mass + addl_lvl_2_mass) * 2 # ditto
    prt.prt_function(fp, f"Conducted Between 3 Primes {' ':>23}size {num_prime_conducted_size:5.3e}{' ':>19}mass {num_prime_conducted_mass:5.3e}\n")

    #add the size and mass of the electron, this is a level III effective conductor
    prt.prt_function(fp, f"Electron (Lvl 3 Eff) {' ':>29}size {lvl3_eff_size:5.3e}{' ':>19}mass {lvl3_eff_mass:5.3e}\n")

    # Richard D. Pohl, Author's Note:
    # I have made a significant effort to treat each level of objects used in the
    # Hypothesis of Universal Matter and quantitatively assemble into a hydrogen
    # build report. Arriving at this point I realized that two processes found only
    # at this level need to be fleshed out, namely
    #
    #   (1.) Fill out the size of the atom by showing that, as the electron is
    #        catapulted away from the nucleus, it sets up a path at a considerable
    #        distance from the nucleus; and
    #   (2.) Add mass to the atom by showing that the conducted matter coursing
    #        from the two effective CPs to, into, and back from the ineffective CP
    #        builds substantial mass via spring actions of this conducted join.
    #
    # However, after a fair amount of effort, I find that I am woefully unprepared
    # to accomplish the task as the physics and maths are far out of my abilities. So
    # I have decided to leave these steps out of the program and leave well enough
    # alone. I hope others will engage in the task and complete the build

    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")

    addl_size = lvl3_eff_size + addl_lvl_1_size + addl_lvl_2_size + num_prime_conducted_size
    addl_mass = lvl3_eff_mass + addl_lvl_1_mass + addl_lvl_2_mass + num_prime_conducted_mass
    prt.prt_function(fp, f"Additions to Tally {' ':>36}{addl_size:5.3e}{' ':>24}{addl_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")

    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")
    full_size = tally_size + lvl3_eff_size + addl_size
    full_mass = tally_mass + lvl3_eff_mass + addl_mass
    prt.prt_function(fp, f"Grand Tally {' ':>38}size {full_size:5.3e}{' ':>19}mass {full_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    return item_refs_list, item_pass_list
