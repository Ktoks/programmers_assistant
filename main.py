import Saber
import sys
import getopt
# def wait():
#     msvcrt.getch()

def main(argv):
    try:
        opts, args = getopt.getopt(argv, opts)
    except getopt.GetoptError:
        print ("error in getopts")
        sys.exit(2)
    saber = saber.SABER()
    #voiceRecognition(saber)?????
    keyWord = input('Listening... Press Ctrl+C to exit')
    if keyWord == 'start':
        running = True
        while running == True:
            keyWord = input('Listening... Press Ctrl+C to exit')
            sentence = saber.voiceRecognition(keyWord)
            saber.analyzeSentence(sentence)
            location = saber.findDirectory[args[1]]
            saber.display.showDisplay()
            keyWord = input('Listening... Press Ctrl+C to exit')
            if keyWord == 'quit':
                running = False

main()
