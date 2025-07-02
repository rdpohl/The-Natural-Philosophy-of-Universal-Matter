"""
Author:   Richard D. Pohl
Date:     April, 2024
Summary:  House function used to print report file
"""

def prt_function(filename, prtstr):
    """Version 1.0.0: Initial Release"""

    rc = open(filename, 'a',encoding='utf-8')

    rc.write(prtstr)

    rc.close()
