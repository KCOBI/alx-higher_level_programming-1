def roman_to_int(roman_string):
    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    numlis = []
    x = 0
    res = 0
    for i in roman_string:
        if i == 'I':
            numlis.append(I)
        if i == 'V':
            numlis.append(V)
        if i == 'X':
            numlis.append(X)
        if i == 'L':
            numlis.append(L)
        if i == 'C':
            numlis.append(C)
        if i == 'D':
            numlis.append(D)
        if i == 'M':
            numlis.append(M)
    for i in range(len(numlis)):
        x = i
        if x == 0:
            res = res + numlis[i]
        elif x == 1:
            if numlis[i-1] < numlis[i]:
                res = res - numlis[i-1]
                res = res + numlis[i] - numlis[i-1]
            else:
                res = res + numlis[i]
        else:
            if numlis[i-1] < numlis[i] and numlis[i-2] < numlis[i]:
                res = res - numlis[i-1] - numlis[i-2]
                res = res + numlis[i] - numlis[i-1] - numlis[i-2]
            elif numlis[i-1] < numlis[i]:
                res = res - 2*numlis[i] + numlis[i]
            else:
                res = res + numlis[i]
    return res
