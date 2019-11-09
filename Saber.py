from snowboy.examples.Python3 import snowboydecoder
import sys
import signal
import showDisplayAndMatchCommands
import tools

INTERRUPTED = False
class SABER:

    def __init__(self):
        self.mLocationMap = {}   # word:folder
        self.mConfig = {}        # setting:action
        self.mLocation = {}      # location:directory
        self.mLanguage = {}      # language:configuration


#######     HELPER FUNCTIONS FOR LISTEN      ########

    def signal_handler(self, signal, frame):
        global INTERRUPTED
        INTERRUPTED = True

    def interrupt_callback(self):
        global INTERRUPTED
        return INTERRUPTED

######      END HELPER FUNCTIONS      ###############

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


# def wait():
#     msvcrt.getch()

    def voiceRecognition(self):
        saber = SABER()
        saber.listen()


# def voiceRecognition():
# 	return saber.listen()
