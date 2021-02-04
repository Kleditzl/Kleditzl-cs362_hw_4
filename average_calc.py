def average(x):
    summ = 0
    if len(x) > 0:
        for i in range(0, len(x)):
            summ = x[i] + summ
        ret = summ/len(x)
        return ret
    else:
        return 0