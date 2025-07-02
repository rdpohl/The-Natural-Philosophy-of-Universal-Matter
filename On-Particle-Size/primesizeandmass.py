'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Build and Report on a Prime Composite Particle
'''

import refitems as ri
import prtfunction as prt

def prime_size_and_mass(item_refs_list, item_pass_list, fp):
    """Version 1.0.0: Initial Release"""

    item_eff_number   = ri.find_record(item_pass_list, 'Level III Effective')
    item_eff_size     = item_pass_list[item_eff_number].size
    item_eff_mass     = item_pass_list[item_eff_number].mass
    item_ineff_number = ri.find_record(item_pass_list, 'Level III Ineffective')
    item_ineff_size   = item_pass_list[item_ineff_number].size
    item_ineff_mass   = item_pass_list[item_ineff_number].mass

    item_number_smb = ri.find_record(item_pass_list, 'Level III Counts')
    item_s_sizeb    = item_pass_list[item_number_smb].size
    item_m_massb    = item_pass_list[item_number_smb].mass

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "  \n")

    hydrogen:    int = 6
    sun:         int = 2
    solar_sys:   int = 1
    galaxy:      int = 0

    level_three: int = sun
    prime:       int = solar_sys

    #now project size/mass of Level II Composite Particle
    #get drill-down factor as size/mass of hyrdrogen to galaxy size/mass
    cp_prime_size_factor = item_refs_list[prime].size / item_refs_list[galaxy].size
    cp_prime_mass_factor = item_refs_list[prime].mass / item_refs_list[galaxy].mass

    #use the factor and drill down from hydrogen to determine {f} size/mass
    cp_prime_size = item_refs_list[hydrogen].size * cp_prime_size_factor
    cp_prime_mass = item_refs_list[hydrogen].mass * cp_prime_mass_factor

    lvl_3_cp_size_factor = item_refs_list[level_three].size / item_refs_list[galaxy].size
    lvl_3_cp_mass_factor = item_refs_list[level_three].mass / item_refs_list[galaxy].mass
    lvl_3_cp_size = item_refs_list[hydrogen].size * lvl_3_cp_size_factor
    lvl_3_cp_mass = item_refs_list[hydrogen].mass * lvl_3_cp_mass_factor

    count_of_prm_in_lvl_3_by_size = cp_prime_size /  lvl_3_cp_size
    count_of_prm_in_lvl_3_by_mass = cp_prime_mass /  lvl_3_cp_mass

    prtstr = "Prime Composite Particle Summary of Size and Mass\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "Projections of Size and Mass\n")
    prt.prt_function(fp, f"Prime CP in Level III Units{' ':>23}size {lvl_3_cp_size:5.3e}{' ':>19}mass {lvl_3_cp_mass:5.3e}\n")
    prt.prt_function(fp, f"Prime CP In Level III Units{' ':>14}count by size {count_of_prm_in_lvl_3_by_size:5.3e}{' ':>10}count by mass {count_of_prm_in_lvl_3_by_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")

    #now process calculated values
    prime_eff_size   = count_of_prm_in_lvl_3_by_size * item_eff_size
    prime_eff_mass   = count_of_prm_in_lvl_3_by_mass * item_eff_mass
    prime_ineff_size = count_of_prm_in_lvl_3_by_size * item_ineff_size
    prime_ineff_mass = count_of_prm_in_lvl_3_by_mass * item_ineff_mass

    count_of_eff_prime_in_lvl_3_by_size   = cp_prime_size / item_eff_size
    count_of_eff_prime_in_lvl_3_by_mass   = cp_prime_mass / item_eff_mass
    count_of_ineff_prime_in_lvl_3_by_size = cp_prime_size / item_ineff_size
    count_of_ineff_prime_in_lvl_3_by_mass = cp_prime_mass / item_ineff_mass

    prt.prt_function(fp, "Calculated Size and Mass\n")
    prt.prt_function(fp, "Effective Conductor\n")
    prt.prt_function(fp, f"Prime CP {' ':>41}size {prime_eff_size:5.3e}{' ':>19}mass {prime_eff_mass:5.3e}\n")
    prt.prt_function(fp, f"Prime CP {' ':>32}count by size {count_of_eff_prime_in_lvl_3_by_size:5.3e}{' ':>10}count by mass {count_of_eff_prime_in_lvl_3_by_mass:5.3e}\n")
    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Ineffective Conductor\n")
    prt.prt_function(fp, f"Prime CP {' ':>41}size {prime_ineff_size:5.3e}{' ':>19}mass {prime_ineff_mass:5.3e}\n")
    prt.prt_function(fp, f"Prime CP {' ':>32}count by size {count_of_ineff_prime_in_lvl_3_by_size:5.3e}{' ':>10}count by mass {count_of_ineff_prime_in_lvl_3_by_mass:5.3e}\n")

    #now summarize inicatives
    count_by_size_ei = count_of_eff_prime_in_lvl_3_by_size + count_of_ineff_prime_in_lvl_3_by_size
    count_by_mass_ei = count_of_eff_prime_in_lvl_3_by_mass + count_of_ineff_prime_in_lvl_3_by_mass
    f_size_countb = item_s_sizeb * count_by_size_ei
    f_mass_countb = item_m_massb * count_by_mass_ei

    prt.prt_function(fp, "  \n")
    prt.prt_function(fp, "Itemized Details\n")
    prt.prt_function(fp, f"Count {{f}} in Prime:{' ':>36}{f_size_countb:5.3e}{' ':>23}{f_mass_countb:5.3e}\n")


    prt.prt_function(fp, "-------------------------------------------------------------------------------------------------\n")

    item_pass_list.append(ri.PassItems('Prime Effective', prime_eff_size, prime_eff_mass))
    item_pass_list.append(ri.PassItems('Prime Ineffective', prime_ineff_size, prime_ineff_mass))

    return(item_refs_list, item_pass_list)
