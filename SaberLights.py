import snowboydecoder
import sys
import signal
import time
#import Saber
from pixels import Pixels, pixels
from google_home_led_pattern import GoogleHomeLedPattern
import speech_recognition as sr




interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
def doStuff():
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)
    r=sr.Recognizer()
    mic=sr.Microphone()
    pixels.wakeup()
    with mic as source:
        audio = r.listen(source)
    query = r.recognize_google(audio)
    #time.sleep(1)
    pixels.think()
    time.sleep(1)
    pixels.speak()
    print(query)
    time.sleep(1)
    pixels.off()



detector.start(detected_callback=doStuff,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)
print("Goodbye!")
detector.terminate()
