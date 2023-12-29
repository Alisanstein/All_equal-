def all_equal(lis):
    if lis ==[]:
        return True
    else:
        for i in lis:
            for j in lis:
                if j == i:
                    output = 1
                else: 
                    output = 0 
                    break
            if output == 0:
                break

        if output == 1: return True
        else: return False