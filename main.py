import saber
# def wait():
#     msvcrt.getch()

def analyzeSentence(sentence):
	args = sentence.split('python')
	if len(args) == 1:
		print("Must include python in string")
		return
	directoryList = args[0].split()
	actualDirectory = directoryList[1:].
	argumentDictionary = {}
	argumentDictionary["directory"] = findDirectory(args[0][1:])
	#argumentDictionary["language"] = findLanguage(arg[2])
	argumentDictionary["command"] = matchCommands(args[3:])
	return argumentDictionary

def voiceRecognition():
	return saber.listen()

def main():
    saber = saber.SABER()
    #voiceRecognition(saber)?????
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

m
