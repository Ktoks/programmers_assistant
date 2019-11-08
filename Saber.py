import snowboydecoder
import sys
import signal

class SABER:

    def __init__(self):
        mLocationMap = {word:folder}
        mConfig = {setting:action}
        mLocation = USA
        mLanguage = Eng    
    

#######     HELPER FUNCTIONS FOR LISTEN      ########

    def signal_handler(signal, frame):
        global interrupted
        interrupted = True

    def interrupt_callback():
        global interrupted
        return interrupted

######      END HELPER FUNCTIONS      ###############

    def findDirectory(arg):
        for key in mLocationMap:
            if arg == key:
                return mLocationMap[key]
        return "Directory not found."

    def listen(self):
	if len(sys.argv) == 1:
    		print("Error: need to specify model name")
    		print("Usage: python demo.py your.model")
    		sys.exit(-1)

	model = sys.argv[1]

	signal.signal(signal.SIGINT, signal_handler)

	detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
	print('Listening... Press Ctrl+C to exit')

	detector.start(detected_callback=snowboydecoder.ding_callback,
               		 interrupt_check=interrupt_callback,
               		      sleep_time=0.03)

	detector.terminate()

        mLocation = args[1]
        mLanguage = args[2]
        mCommand = args[3]

    def findDirectory(location):
        # NEEDS TO LOOKUP THE COMMAND AND COMPARE location WITH A SAVED LOCATION IN OUR DICTIONARY
        # return the actual location


# def wait():
#     msvcrt.getch()

def analyzeSentence(sentence):
    	args = sentence.split()
	argumentDictionary = {}
	argumentDictionary["directory"] = findDirectory(args[1])
	argumentDictionary["language"] = findLanguage(arg[2])
	argumentDictionary["command"] = matchCommands(args[3:])
	return argumentDictionary

def voiceRecognition():
	saber = SABER()
	saber.listen()

def main(argv):

    try:
        opts, args = getopt.getopt(argv, opts)
    except getopt.GetoptError:
        print ("error in getopts")
        sys.exit(2)
        

    saber = SABER()
    keyWord = input('Listening... Press Ctrl+C to exit')
    if keyword == 'start':
        running = True
        while running == True:
            sentence = voiceRecognition()
            display = sentence.analyzeSentence()
            display.showDisplay()
            keyWord = input('Listening... Press Ctrl+C to exit')
            if keyword == 'quit':
                running = False

main()
