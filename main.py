import saber
# def wait():
#     msvcrt.getch()

def analyzeSentence(sentence):
	args = sentence.split('python')
	if len(args) == 1:
		print("Must include python in string")
		return
	directoryList = args[0].split()
	actualDirectory = directoryList[1:].join(" ")
	argumentDictionary = {}
	argumentDictionary["directory"] = findDirectory(actualDirectory)
	#argumentDictionary["language"] = findLanguage(arg[2])
	argumentDictionary["command"] = matchCommands(args[1])
	return argumentDictionary

def voiceRecognition():
	return saber.listen()

def main():
    try:
        opts, args = getopt.getopt(argv, opts)
    except getopt.GetoptError:
        print ("error in getopts")
        sys.exit(2)
    saber = saber.SABER()
    #voiceRecognition(saber)?????
    keyWord = input('Listening... Press Ctrl+C to exit')
    if keyword == 'start':
        running = True
        while running == True:
            keyWord = input('Listening... Press Ctrl+C to exit')
            sentence = voiceRecognition(keyword)
            analyzeSentence(sentence)
            location = findDirectory[arg1]
            display.showDisplay()
            keyWord = input('Listening... Press Ctrl+C to exit')
            if keyword == 'quit':
                running = False

main()
