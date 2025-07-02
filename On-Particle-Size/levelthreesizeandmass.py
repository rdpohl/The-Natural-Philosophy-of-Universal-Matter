'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Level Three Composite Particle
'''

import refitems as ri
import prtfunction as prt

def level_3_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_number = ri.find_record(item_pass_list, 'Level II')
    item_size   = item_pass_list[item_number].size
    item_mass   = item_pass_list[item_number].mass

    item_number_sma = ri.find_record(item_pass_list, 'Level II Counts')
    item_s_sizea   = item_pass_list[item_number_sma].size
    item_m_massa   = item_pass_list[item_number_sma].mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    hydrogen:  int = 6
    sun:       int = 2
    galaxy:    int = 0

    level_three: int = sun

    #now project size/mass of Level II Composite Particle
    #get drill-down factor as size/mass of hyrdrogen to galaxy size/mass
    cp_3_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size
    cp_3_mass_factor = item_refs_list[level_three].mass / item_refs_list[galaxy].mass

    #use the factor and drill down from hydrogen to determine {f} size/mass
    cp_lvl_3_size = item_refs_list[hydrogen].size * cp_3_size_factor
    cp_lvl_3_mass = item_refs_list[hydrogen].mass * cp_3_mass_factor

    count_of_lvl_2_in_lvl_3_by_size = cp_lvl_3_size / item_size
    count_of_lvl_2_in_lvl_3_by_mass = cp_lvl_3_mass / item_mass

    prtstr = "Level III Composite Particle Summary of Size and Mass\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size and Mass\n")
    prt.prt_function(fp, f"Level III CP in Level II Units{' ':>20}size {cp_lvl_3_size:5.3e}{' ':>19}mass {cp_lvl_3_mass:5.3e}\n")
    prt.prt_function(fp, f"Level III CP In Level II Units{' ':>11}count by size {count_of_lvl_2_in_lvl_3_by_size:5.3e}{' ':>10}count by mass {count_of_lvl_2_in_lvl_3_by_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")

    #now process calculated values
    lvl_3_size = count_of_lvl_2_in_lvl_3_by_size * item_size
    lvl_3_mass = count_of_lvl_2_in_lvl_3_by_mass * item_mass

    find_number = ri.find_record(item_pass_list, 'Level II')
    find_size   = item_pass_list[find_number].size
    find_mass   = item_pass_list[find_number].mass
    lvl_3_effect_size   = lvl_3_size + (count_of_lvl_2_in_lvl_3_by_size * find_size)
    lvl_3_effect_mass   = lvl_3_mass + (count_of_lvl_2_in_lvl_3_by_mass * find_mass)

    lvl_3_in_effect_size = lvl_3_size * 1.05   #?? 5%
    lvl_3_in_effect_mass = lvl_3_mass * 1.05

    prt.prt_function(fp, "Calculated Size and Mass\n")
    prt.prt_function(fp, f"Total Level III Effective Conductor{' ':>12}by size {lvl_3_effect_size:5.3e}{' ':>16}by mass {lvl_3_effect_mass:5.3e}\n")
    prt.prt_function(fp, f"Total Level III Ineffective Conductor{' ':10}by size {lvl_3_in_effect_size:5.3e}{' ':>16}by mass {lvl_3_in_effect_mass:5.3e}\n")
    prt.prt_function(fp, f"{' ':>55}{'---------'}{' ':>24}{'---------'}\n")

    avg_lvl_3_size = lvl_3_effect_size + lvl_3_in_effect_size
    avg_lvl_3_mass = lvl_3_effect_mass + lvl_3_in_effect_mass

    prt.prt_function(fp, f"Total Level III {' ':>23}Average by size {avg_lvl_3_size:5.3e}{' ':>16}by mass {avg_lvl_3_mass:5.3e}\n")

    #now summarize inicatives
    f_size_counta = item_s_sizea * count_of_lvl_2_in_lvl_3_by_size
    f_mass_counta = item_m_massa * count_of_lvl_2_in_lvl_3_by_mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Level III:{' ':>32}{f_size_counta:5.3e}{' ':>23}{f_mass_counta:5.3e}\n")

    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    item_pass_list.append(ri.PassItems('Level III Effective', lvl_3_effect_size, lvl_3_effect_mass))
    item_pass_list.append(ri.PassItems('Level III Ineffective', lvl_3_in_effect_size, lvl_3_in_effect_mass))
    item_pass_list.append(ri.PassItems('Level III Counts', f_size_counta, f_mass_counta))

    return item_refs_list, item_pass_list
