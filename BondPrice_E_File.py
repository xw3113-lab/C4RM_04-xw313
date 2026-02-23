

def getBondPrice_E(face, couponRate, yc):
    y = y / ppy
    n = m * ppy
    coupon = face * couponRate / ppy
    
    sumPVCF = 0
    sum_t_PVCF = 0
    
    for t in range(1, n + 1):
        cf = coupon
        if t == n:
            cf += face
        
        pvcf = cf / ((1 + y) ** t)
        sumPVCF += pvcf
        sum_t_PVCF += t * pvcf
    
    bondDuration = (sum_t_PVCF / sumPVCF) / ppy 
    
    return(bondDuration)
    
