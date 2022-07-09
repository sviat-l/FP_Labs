def fast_implemention(posittion1='b5', posittion2='f4'):
    x1, y1 = ord(posittion1[0]) -ord('a') , int(posittion1[1])
    x2, y2 = ord(posittion2[0]) -ord('a') , int(posittion2[1])
    return set( chr(ord('a') + i) + str(j) for i in range(8) for j in range(8)
             if i not in (x1, x2) and j not in (y1, y2) and abs(x2 - i) != (abs(x1 - j)))
