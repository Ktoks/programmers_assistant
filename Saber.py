class SABER:
    
    def __init__(self):
        mLocationMap = {word:folder}
        mConfig = {setting:action}
        mLocation = USA
        mLanguage = Eng

# def wait():
#     msvcrt.getch()

def main():
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