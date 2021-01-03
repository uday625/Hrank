def NumberLineJump(x1, v1, x2, v2):
        while True:
            if x1 > x2:
                return 'NO'
            elif v2 >= v1:
                return 'NO'
            x1 = x1 +v1
            x2 = x2 +v2
            if x1==x2:
                return 'YES'


if __name__ == '__main__':
    param =[0, 3, 4, 2]  #YES
    param =[0, 2, 5, 3]  #NO
    param =[21, 6, 47, 3] #NO
    param =[43, 2, 70, 2] #NO

    x1 =param[0]
    v1 =param[1]
    x2 =param[2]
    v2 =param[3]
    NumberLineJump(x1, v1, x2, v2)