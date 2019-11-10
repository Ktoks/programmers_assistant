#class :D
from tkinter import messagebox
import os
import subprocess
#from settings import *
from commandDatabase import *
import tools

#from tools import InvalidCommand
class InvalidCommand(Exception):
    pass

SETTINGS_WINDOW_HEIGHT = 400
SETTINGS_WINDOW_WIDTH = 500
SETTINGS_WINDOW_TOPIC = "Let's get this digital bread gamers"
SETTINGS_WINDOW_FPS = 15

AUTOCOMPLETE_ACCURACY = 0.8

##def show_settings():
##    screen = pygame.display.set_mode((SETTINGS_WINDOW_WIDTH,SETTINGS_WINDOW_HEIGHT))
##    pygame.display.set_caption(SETTINGS_WINDOW_TOPIC)
##    #surface = pygame.Surface((SETTINGS_WINDOW_WIDTH,SETTINGS_WINDOW_HEIGHT))
##    
##    carryOn = True
##    while carryOn:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                carryOn = False
##        #surface.fill((255,255,255))
##        #surface.blit(screen,(0,0))
##        screen.fill((255,255,255))
##        pygame.display.update()



def match_commands(a1,a2,a3):
    #print(a1,a2)
    if type(a3) != list:
        a3 = [a3]
    #a1 = directory
    #a2 = language
    #a3 = list of words spoken by the user

    commands = ["cd "+a1]

    action = ""
    baseCommand = True
    breakPast = False
    for item in a3:
        if len(item) < 1:
            continue
        if breakPast:
            breakPast = False
            if item == "pie":
                action += "py"
            else:
                action += item.strip()
            continue
        if item.strip()[-1] == ".":
            breakPast = True
            action += item.strip()
            continue
        if baseCommand:

            baseCommand = False
            try:
                print('base command stripped',item.strip())
                action = pythonCommandLibrary[item.strip().lower()]
                print('mapped action',action)
            except:
                print("error py command library")
                return False
            continue
        if item.strip() == "and":
            #Another command is coming in.
            commands.append(action)
            baseCommand = True
            action = ""
            continue
        if item.strip() == "dot"or item.strip() == ".":
            action += "."
            breakPast = True
            continue
        if item.strip() == "back":
            action += " .."
            continue
        action += " " + item.strip()
    if len(a3) > 1:
        if a3[-2].lower().strip() == "run":
            options = []
            direct = a1[:]
            if direct == '':
                direct = '/home/pi'
            
            #try:
            #print("AAAAAAAAAAAAAAAAAA",next(walk(direct)))
            things = []
            for item in os.listdir(direct):
                if "." != item[0] and "." in item:
                    things.append(item)

            action = tools.fix_word(a3[-1]+".py", things,AUTOCOMPLETE_ACCURACY)
                
    if len(action) > 0:
        commands.append(action)
    return commands
    #Return string of command to execute

def dummy_display(a3):
    for item in a3:
        print(item)

def show_display(a3):
    #a3 = list of strings to execute
    response = ""
    #output = subprocess.run(a3, shell=True,stdout=response)
    #p = subprocess.check_output(a3)
    try:
        #subprocess.call(a3[0],shell=True)
        p = subprocess.check_output(a3[0] + ";" + a3[1],shell=True)
    except subprocess.CalledProcessError:
        print("Invalid commands")
        #if output.returncode != 0:
        brief = "Command has failed with output:"
        title = "Error"
        #brief += "\n" + p
        #message = gui.GUI()
        #message.ErrorWindow(brief)
    else:
        brief = "Command has succeeded with output:"
        title = "Success"
        print(title)
        finalOut = []
        p = p.split(b"\n")
        for item in p:
            finalOut.append(item.decode("utf-8"))
        print(finalOut) 
	#brief += "\n" + p
        #message = gui.GUI()
        #message.MessageWindow(brief)
