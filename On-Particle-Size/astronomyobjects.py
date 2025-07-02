'''
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  Load list of astronomical objects to be in sizing Universal Matter 
          objects. ite_refs_list is declared in main.py and passed to this
          function.  
'''

import refitems as ri
import prtfunction as prt

def astronomy_objects(item_refs_list, fp):
    """Version 1.0.0: Initial Release"""
    prt.prt_function(fp, "  \n")

    galaxy:    int = 0

    # Load the givens into the list
    item_refs_list.append(ri.RefItems('Galaxy',           1.0   * 10**21,  2.984 * 10**42,  0.0,  0.0)) #  0
    item_refs_list.append(ri.RefItems('Solar System',     5.988 * 10**12,  1.989 * 10**30,  0.0,  0.0)) #  1
    item_refs_list.append(ri.RefItems('Sun',              1.393 * 10**9,   1.989 * 10**30,  0.0,  0.0)) #  2
    item_refs_list.append(ri.RefItems('Avg Planet ',      5.009 * 10**7,   3.333 * 10**27,  0.0,  0.0)) #  3
    item_refs_list.append(ri.RefItems('Avg Asteroid',     1.5   * 10**2,   9.360 * 10**13,  0.0,  0.0)) #  4
    item_refs_list.append(ri.RefItems('Space Dust',       2.000 * 10**-6,  1.100 * 10**-13, 0.0,  0.0)) #  5
    item_refs_list.append(ri.RefItems('Hydrogen',         1.2   * 10**-10, 1.674 * 10**-27, 0.0,  0.0)) #  6
    item_refs_list.append(ri.RefItems('Proton',           8.6   * 10**-16, 1.673 * 10**-27, 0.0,  0.0)) #  7
    item_refs_list.append(ri.RefItems('Electron',         1.0   * 10**-14, 9.109 * 10**-31, 0.0,  0.0)) #  8
    item_refs_list.append(ri.RefItems('Photon',           1.0   * 10**-20, 1.0   * 10**-55, 0.0,  0.0)) #  9
    item_refs_list.append(ri.RefItems('Quark',            1.0   * 10**-18, 6.151 * 10**-27, 0.0,  0.0)) # 10
    item_refs_list.append(ri.RefItems('Planck\'s Length', 1.616 * 10**-35, 0.0   * 10**0,   0.0,  0.0)) # 11

    # now load claculated items based on the first (0) row
    for i in item_refs_list:
        if i.name == 'Galaxy' or i.name =='Planck\'s Length':
            continue
        else:
            i.s_factor = i.size / item_refs_list[galaxy].size
            i.m_factor = i.mass / item_refs_list[galaxy].mass

    #Now printout the list as part of the report
    #print Title
    prtstr = "On Universal Matter Particle Sizing\n"
    prt.prt_function(fp, prtstr)
    prt.prt_function(fp, "  \n")

    #print column header
    prt.prt_function(fp, "Table of Sizes and Masses for Common Astronomical Objects \n")
    prt.prt_function(fp, f"{'Object':<15}{'Ref#':>4}{' ':>12}{'Size':>9}{' ':>10}{'Mass':>9}{' ':>13}{'S-Factor':>9}{' ':10}{'M-Factor':>9}\n")
    prt.prt_function(fp, f"{'--------------':<15}{'----':>4}{' ':>12}{'---------':>9}{' ':>10}{'---------':>9}{' ':>13}{'---------':>9}{' ':>10}{'---------':>9} \n")
    cntr = 0
    for x in item_refs_list:
        prt.prt_function(fp, f"{x.name:15}{cntr:>4}{' ':>12}{x.size:>5.3e}{' ':>10}{x.mass:5.3e}{' ':>13}{x.s_factor:5.3e}{' ':>10}{x.m_factor:5.3e}\n")
        cntr  += 1

    prt.prt_function(fp, "----------------------------------------------------------------------------------------------------\n")

    return item_refs_list
