import RPi.GPIO as GPIO
import flicklib
import keyboard

@flicklib.tap()
def tap(position):
    print(position)
    if position == 'west':
        keyboard.press_and_release('left')
    if position == 'east':
        keyboard.press_and_release('right')
    if position == 'center':
        keyboard.press_and_release('space')

while True:
    pass
