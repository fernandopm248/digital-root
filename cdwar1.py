def digital_root (n):
    total = 10
    while total > 9 :
        total = 0
        x = str(n)
        stringfy = []
        cont = (len(x))
        i = 0
        e = 1
        num = []



        while i < cont :
            stringfy += x[i:e]
            i += 1
            e += 1

        for i in range(len(stringfy)):
            t = int(stringfy[i])
            num.append(t)

        total = sum(num)

        n = total
        stringfy.clear()
        num.clear()
    print(total)














digital_root(493193)