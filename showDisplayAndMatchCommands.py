#class :D
from tkinter import messagebox
import os
import subprocess
#from settings import *

SETTINGS_WINDOW_HEIGHT = 400
SETTINGS_WINDOW_WIDTH = 500
SETTINGS_WINDOW_TOPIC = "Let's get this digital bread gamers"
SETTINGS_WINDOW_FPS = 15

#    def voice_recognition

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

#commands:
#    python3 _file_
#    cd somewhere
#    run _command_ in directory:
#        cd into directory
#        run command
#        go back to original directory
        
#python3 file running

def match_commands(a1,a2,a3):
    #a1 = directory
    #a2 = language
    #a3 = list of words spoken by the user
    
    if a2.lower() == "python":
        ###
        pass
    elif a2.lower() == "c++" or a2.lower() == "cpp":
        ###
        pass
    elif a2.lower() == "java":
        ###
        pass
    
    #Return string of command to execute

def show_display(a3):
    #Example: "gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'"
    #a3 = list of strings to execute
    output = subprocess.run(a3, shell=True)
    if output.returncode != 0:
        brief = "Command has failed with output:"
        title = "Error"
        brief += "\n" + output.stdout
        messagebox.showwarning(title,brief)
    else:
        brief = "Command has succeeded with output:"
        title = "Success"
        brief += "\n" + output.stdout
        messagebox.showinfo(title,brief)
    
    
    #a3 = string? = {0}
    #stringToExecute = """
    #    "gnome-terminal -e 'bash -c \"{0}; exec bash\"'"
    #                    """.format(a3)
    #os.system(stringToExecute)
        
show_display(["ls", "-al"])
#show_settings()


#create a showDisplay function that recieves arguments and spawns display in
        #forefront after completing command(difficult?),
# or spawns a new linux terminal with config from args[1-3], moving it to the
        #forefront when the command completes
    # creates a new display or new terminal for each command sentence the user
        #inputs
    # should kill any processes it has spawned in the background, then display
        #the output?
    # waits for the exit command or x to be press to close the display window
    # only shuts itself down when quit command issued
