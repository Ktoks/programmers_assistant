

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
    best = 0
    tests = sort_col(tests,1)
    bests = 1
    while True:
        if abs(tests[-(bests+1)][1] - tests[-1][1]) < 0.01 :
            bests += 1
        else:
            break
    if bests > 1:
        print("There's more than 1 best option. Idk what to do with this.  Total:",bests)
    elif tests[-1][1] > accuracy:
        print("There's a winner:",options[tests[-1][0]])
    elif tests[-1][1] > accuracy - FORGIVENESS_ERROR:
        print("There's something close to being valid. Did you mean:",options[tests[-1][0]])
    else:
        print("Nothing is close. Try again matey.")

def similarityR(target,option):
    #print(target,option)
    if len(target) == 0 or len(option) == 0:
        return 0
    
    if len(target) > len(option):
        big = target
        small = option
    else:
        big = option
        small = target

    subs = get_largest_substring(small,big)
    #print(subs)
    if not subs:
        return 0
    myLen = subs[0][1] - subs[0][0]
    left = similarityR(small[:subs[0][0]],big[:subs[1][0]])
    right = similarityR(small[subs[0][1]:],big[subs[1][1]:])
    #print(myLen,left,right)
    return myLen + left + right

def get_largest_substring(small,big):
    for i in range(len(small),0,-1): #1
        for j in range(len(small)-i+1):#2
            for k in range(len(big)-i+1):#2
                if small[j:j+i] == big[k:k+i]:
                    return [[j,j+i],[k,k+i]]
    return False

def sort_col(data,col):
    if len(data) < 2:
        return data
    #Merge sort here. Find midpoint
    midpoint = len(data)//2
    #Split and sort both sides
    left = sort_col(data[:midpoint],col)
    right = sort_col(data[midpoint:],col)
    #Combine them
    L,R = 0,0
    Ll,Rl = len(left),len(right)
    new = []
    while L+R != len(data):
        if L == Ll:
            new.append(right[R])
            R += 1
        elif R == Rl:
            new.append(left[L])
            L += 1 
        elif left[L][col] < right[R][col]:
            new.append(left[L])
            L += 1
        else:
            new.append(right[R])
            R += 1
    return new

t = "arrow"
o = "arow"
#t ="i am going home"
#o = "gone home"
#t = "test"
#o = "text"
#t = "st"
#o = "xt"
print((2*similarityR(t,o))/(len(t) + len(o)))
