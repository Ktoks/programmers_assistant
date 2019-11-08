def similarity(target,options,accuracy):
    #this function receives a target string and a list of optional strings it
    #   might match. It returns the highest accuracy option if it is within
    #   _accuracy_ of target. Otherwise, returns False for not recognized.
    tests = []
    for i in range(len(options)):
        x = similarityR(target,options[i])
        x = (2*x)/(len(target) + len(option))
        tests.append(i,x)
    #check all

def similarityR(target,option):
    if len(target) == 0 or len(option) == 0:
        return 0
    
    if len(target) >= len(option):
        big = target
        small = option
    else:
        big = option
        small = target

    finished = False
    for i in range(len(small),0,-1):
        #Must end at 1
        for j in range(len(small)-i+1):
            for k in range(len(big)-i+1):
                if small[j:i+1] == big[k:i+1]:
                    longestSmall = [j,i+1]
                    longestBig = [k,i+1]
                    print(small[j:i+1],big[k:i+1])
                    print(longestSmall,longestBig)
                    finished = True
                    break
            if finished: break
        if finished: break
    if not finished:
        return 0
    
    left = similarityR(big[:longestBig[0]], small[:longestSmall[0]])
    right = similarityR(big[longestBig[1]+1:],
                                     small[longestSmall[1]+1:])
    return (longestSmall[1] - longestSmall[0]) + left + right

t ="i am going home"
o = "gone home"
#t = "zzzhatppp"
#o = "qqqhatlll"
print((2*similarityR(t,o))/(len(t) + len(o)))
