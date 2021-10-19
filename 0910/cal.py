def cal (w, k, o):
    '''
    Функция
    '''
    w_30 = [4, 6, 9, 11]
    w_31 = [1, 3, 5, 7, 8, 10, 12]
    if (o <= 2021 and k <= 12 and w <= 31) and (k > 0 and w > 0 and o > 0):
        if (o < 2021) or (o == 2021 and k < 10) or (o == 2021 and k == 10 and w <= 9):
            if w <= 30 and k in w_30:
                return True
            elif w <= 31 and k in w_31:
                return True
            elif k == 2:
                if (w <= 28) or (o%4 == 0 and w == 29):
                    return True
    else:
        return False

print(cal(15, 10, 2012))