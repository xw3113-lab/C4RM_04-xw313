

def getBondPrice_Z(face, couponRate, times, yc):
    
    coupon = face * couponRate
    bondPrice = 0
    
    cfs = [coupon] * len(times)
    cfs[-1] += face
    
    for t, r, cf in zip(times, yc, cfs):
        bondPrice += cf / ((1 + r) ** t)
    
    return(bondPrice)
