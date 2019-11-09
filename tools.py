FORGIVENESS_ERROR = 0.1
# from tk import messagebox
#import tkinter as tk
#from tkinter import messagebox
import gui
from os import walk
import showDisplayAndMatchCommands

BASE_DIRECTORY = "C:\\Users\\aeque\\Desktop\\programmers_assistant\\Testdir\\"
FORGIVENESS_ERROR = 0.1
AUTOCOMPLETE_ACCURACY = 0.8

class InvalidCommand(Exception):
    pass
    
def fix_word(target,options,accuracy):
    #print(">"+target+"<",options)
    #this function receives a target string and a list of optional strings it
    #   might match. It returns the highest accuracy option if it is within
    #   _accuracy_ of target. Otherwise, raises an exception for InvalidCommand
    print(options)
    tests = []
    for i in range(len(options)):
        x = fix_word_R(target,options[i])
        x = (2*x)/(len(target) + len(options[i]))
        tests.append([i,x])
    #check all
    print(tests)
    best = 0
    tests = sort_col(tests,1)
    tests.reverse()
    bests = 1
    while True:
        print(tests)
        if bests < len(tests):
            if abs(tests[bests][1] - tests[0][1]) < 0.01 :
                bests += 1
            else:
                break
        else:
            break
    if bests > 2: 
        if tests[-0][1] > accuracy:
            message = gui.GUI()
            message.ErrorWindow("Command failed: '"+target+
                                "'too vague, "+str(bests) +
                                " possible interpretations.")
            raise InvalidCommand
    if bests > 1:
        if tests[0][1] > accuracy:
        #This isn't implemented right now
            print("There's more than 1 best option. Idk what to do with this.  Total:",bests)
    elif tests[0][1] > accuracy:
        #print(tests)
        return options[tests[0][0]]
    elif tests[0][1] > accuracy - FORGIVENESS_ERROR:
        message = gui.GUI()
        #print(tests)
        result = message.YesNo("Did you mean: '"+options[tests[0][0]]+"'?")
        if result:
            return options[tests[0][0]]
        else:
            raise InvalidCommand
    else:
        raise InvalidCommand

def fix_word_R(target,option):
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
    left = fix_word_R(small[:subs[0][0]],big[:subs[1][0]])
    right = fix_word_R(small[subs[0][1]:],big[subs[1][1]:])
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

def analyzeSentence(sentence):
    print("Sentence received:",sentence)
    try:
        #sentence = "directory language command"
        args = sentence.split(' python ')
        if len(args) == 1:
            print("Must include python in string")
            return
        #args = ["directory","command"]
        
        if args[0].strip() == "here":
            finalDirectory = "."
            print("yoo")
        elif args[0].strip() == "home":
            print("yoo2")
            finalDirectory = ""
        else:
            if "/" in args[0]:
                directoryList = args[0].split("/")
            else:
                directoryList = args[0].split('slash')
            if directoryList[0] == '':
                directoryList[0] = '~'
            #directoryList = ['one','two','three']
            #or directoryList = ['~','one','two','three']

            #Theoretical stuff:       
            start = 0
            if directoryList[0] == "~":
                workingDir = "~"
                start = 1
            else:
                workingDir = BASE_DIRECTORY
            for i in range(start,len(directoryList)):
                working = directoryList[i].lower().strip()
                if len(working) > 0:
                    #Dirs = []
                    #for [dirpath, dirnames, filenames] in walk(workingDir):
                    #    Dirs.extend(dirnames)
                    #    break #Best for loop 2019
                    Dirs = next(walk('.'))[1]
                    #print("Working:",working)
                    #print("Working Directory:",workingDir)
                    #print("DIRS:",Dirs)
                    #print("Options:",dirnames)
                    new = fix_word(working,Dirs,AUTOCOMPLETE_ACCURACY)
                    #print("ValidatedDir:",new)
                    workingDir += new + "\\"
            finalDirectory = workingDir

        ##DEBUG!!
        #print(">"+args[1]+"<")
        #return finalDirectory
        ##DEBUG!!

        actions = args[1].split()

        commands = showDisplayAndMatchCommands.match_commands(finalDirectory,"python",actions)
        if not commands:
            raise InvalidCommand
        #showDisplayAndMatchCommands.show_display(commands)
        showDisplayAndMatchCommands.dummy_display(commands)
    except InvalidCommand:
        message = gui.GUI()
        message.ErrorWindow("Invalid command.")
        

#t = "holy cow!"
#o = ["crow","blow","asglaglvsk","agrw","arw"]
#o = ["cd", "c", "d", "ls", "l", "s", "home", "start", "quit", "."]
#t ="med"
#o = ["big","lil","med"]
#t = "test"
#o = "text"
#t = "st"
#o = "xt"
#<<<<<<< Updated upstream
#print(fix_word(t,o,0.8))


#=======
#root = tk.Tk()
#root.withdraw()
#window = tk.Toplevel()
#fix_word(window,t,o,0.8)
#message(window,"waaaaa","aaaaaaa",0)
#>>>>>>> Stashed changes

#analyzeSentence("dog slash whie slash extralong slash scruffy python run sabre dot pie")
#print("------")
#analyzeSentence("dog slash whie slash extralong python run sabre dot pie and relocate scruffy and cd back and make clean")
#print("------")
#analyzeSentence("slash desktop relocate back")
analyzeSentence("here python run test")
