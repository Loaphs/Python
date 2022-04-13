import pynput
from pynput.keyboard import Key, Controller 
import time

keyboard = Controller()

def wait():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(.1)
    wait()

wait()