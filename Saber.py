import snowboy.examples.Python3.snowboydecoder
import sys
import signal
import showDisplayAndMatchCommands

INTERRUPTED = False
class SABER:

    def __init__(self):
        mLocationMap = {}   # word:folder
        mConfig = {}        # setting:action
        mLocation = {}      # location:directory
        mLanguage = {}      # language:configuration


#######     HELPER FUNCTIONS FOR LISTEN      ########

    def signal_handler(self, signal, frame):
        global INTERRUPTED
        INTERRUPTED = True

    def interrupt_callback(self):
        global INTERRUPTED
        return INTERRUPTED

######      END HELPER FUNCTIONS      ###############

    def findDirectory(self, arg):
        for key in self.mLocation:
            if arg == key:
                return self.mLocation[key]
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

        mLocation = model[1]
        mLanguage = model[2]
        mCommand = model[3]

    def findDirectory(self, location):
        pass
        # NEEDS TO LOOKUP THE COMMAND AND COMPARE location WITH A SAVED LOCATION IN OUR DICTIONARY
        # return the actual location


# def wait():
#     msvcrt.getch()

# def analyzeSentence(self, sentence):
#     args = sentence.split()
#     argumentDictionary = {}
#     argumentDictionary["directory"] = findDirectory(args[1])
#     argumentDictionary["language"] = findLanguage(arg[2])
#     argumentDictionary[
#         "command"] = showDisplayAndMatchCommands.matchCommands(args[3:])
#     return argumentDictionary

    def voiceRecognition(self):
        saber = SABER()
        saber.listen()

    def analyzeSentence(self, sentence):
        args = sentence.split('python')
        if len(args) == 1:
            print("Must include python in string")
            return
        directoryList = args[0].split()
        actualDirectory = directoryList[1:].join(" ")
        argumentDictionary = {}
        argumentDictionary["directory"] = findDirectory(actualDirectory)
        #argumentDictionary["language"] = findLanguage(arg[2])
        argumentDictionary[
            "command"] = showDisplayAndMatchCommands.matchCommands(args[1])
        return argumentDictionary

# def voiceRecognition():
# 	return saber.listen()
