def minion_game(string):
    # your code goes here
    vouls = 'auioe'
    k = 0
    s = 0
    l = len(string)
    
    for i in range(l):
        if string[i] in vouls or string[i] in vouls.upper():
            k += l - i
        else:
            s += l - i
            
    if k > s:
        print("Kevin", k)
    elif s > k:
        print("Stuart", s)
    else:
        print("Draw")
