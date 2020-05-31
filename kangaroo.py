def kangaroo(x1, v1, x2, v2):
    #edge cases check:
    if v1 == v2:
        if x1 != x2:
            return "NO"
    if x1 >= x2:
        if v1 > v2:
            return "NO"
    elif x2 >= x1:
        if v2 > v1:
            return "NO"

    if (x2-x1) % (v1-v2) == 0:
        return "YES"
    else:
        return "NO"
        
kangaroo(43,2,70,2)
        
        