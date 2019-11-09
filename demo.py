#import snowboydecoder
import os
import sys
import signal
import time
#import Saber
from pixels import Pixels, pixels
from google_home_led_pattern import GoogleHomeLedPattern
import speech_recognition as sr
import tools
#from pocketsphinx import LiveSpeech,get_model_path



interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


#model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


print('Listening... Press Ctrl+C to exit')

# main loop
def doStuff():
    r=sr.Recognizer()
    mic=sr.Microphone(sample_rate=32000,chunk_size=512)

    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)
    while True:
        pixels.wakeup()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        pixels.think()
        try:
            possibleQueries = r.recognize_google(audio,show_all=True)
        except UnknwonValueError:
            print("I didnt hear that, try again!")
            continue
        
        if possibleQueries == []:
            print("Sorry, I didnt catch that, try again ........")
            continue
        else:
            possibleQueries=possibleQueries['alternative']
        print(possibleQueries)
        query=""
        for item in possibleQueries:
            sentence = item['transcript'].split()
            for word in sentence:
                word = word.lower()
            if sentence[0].lower() == 'saber' or sentence[0].lower() == 'sabre' or sentence[len(sentence)-1].lower() == 'quit':
                query = item['transcript']

        print(query)
        if query=='':
            print('Sorry, we werent able to translate that sentence....')
        else:
            l = query.split()
            if l[0].lower() == 'saber' or l[0].lower() == 'sabre':
                print("Good command!!!")
                print(" ".join(l[1:]) )
                tools.analyzeSentence( " ".join(l[1:])  )
            elif l[len(l)-1]== 'quit':
                print("Goodbye!")
                pixels.off()
                break
        pixels.off()
        time.sleep(2)


doStuff()
#detector.start(detected_callback=doStuff,
#               interrupt_check=interrupt_callback,
#               sleep_time=0.03)
#print("Goodbye!")
#detector.terminate()
