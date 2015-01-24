

def find_z_shade_percentage(xbar, sd, condition_percentage, cutoff_per = 0., high_low = 1, cutoff_hi_low = 0):
    """
    The basis of this function is to find either upper and lower of a given percentage based on empirical formula of z score OR
    to find out the percentage area between two z scores.
    This is rough code. Scope of improvization but I am not going to because this was just a quick n dirty thing I came up with to answer a few questions out of an exercise, just for practice.
    high_low: 0 => lower than '%' given, 1 => higher than '%'
    """
    #could improvize code by include following values in a global dict
    z3_z2 = z2_z3 = 2.35
    z2_z1 = z1_z2 = 13.5
    z3_less = z3_more = 0.15
    z1_half = 34

    z1_hi = z1_lo = z2_hi = z2_lo = z3_hi = z3_lo = 0.
    #Zs = (z1_hi, z1_lo,z2_hi, z2_lo, z3_hi, z3_lo)

    z1_hi, z1_lo = xbar+sd, xbar-sd
    z2_hi, z2_lo = z1_hi+sd, z1_lo-sd
    z3_hi, z3_lo = z2_hi+sd, z2_lo-sd

    #each key has lower, higher percentage
    Z_list = {
        round(z1_hi, 2): (100-(z1_z2+z2_z3+z3_more), z1_z2+z2_z3+z3_more),
        round(z1_lo, 2): (z2_z1+z3_z2+z3_less, 100-(z2_z1+z3_z2+z3_less)),
        round(z2_hi, 2): (100 - (z2_z3+z3_more), z2_z3+z3_more),
        round(z2_lo, 2): (z3_z2+z3_less, 100-(z3_z2+z3_less)),
        round(z3_hi, 2): (100-z3_more, z3_more),
        round(z3_lo, 2): (z3_less, 100 - z3_less)
        }
    print Z_list
    if not cutoff_per:
        return Z_list[condition_percentage][high_low]
    elif cutoff_per and high_low == 0 and cutoff_hi_low == 0:
        return Z_list[condition_percentage][high_low] - Z_list[cutoff_per][cutoff_hi_low]
