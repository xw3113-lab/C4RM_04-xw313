
def getBondPrice_E(face, couponRate, m, yc):
    
    coupon = face * couponRate
    bondPrice = 0
    
    for t, r in enumerate(yc, start=1):
        cf = coupon
        if t == m:
            cf += face
        bondPrice += cf / ((1 + r) ** t)
    
    return(bondPrice)
