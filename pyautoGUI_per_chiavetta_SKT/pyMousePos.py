import pyautogui
#import time
pyautogui.FAILSAFE = True #True is default

w,h=pyautogui.size()
print('screen resolution: W= ',w,', H= ',h)

###Animation demo
##
##for i in range(2):
##      pyautogui.moveRel(10, 0, duration=0.25)
##      pyautogui.moveRel(0, 10, duration=0.25)
##      pyautogui.moveRel(-10, 0, duration=0.25)
##      pyautogui.moveRel(0, -10, duration=0.25)

##x,y=pyautogui.position()
##print('mouse pointer: X= ',x,', Y= ',y)

print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        strlen=len(positionStr)
        print(positionStr,end='')
        print('\b' * strlen, end='', flush=True)

         
        #time.sleep(1.0)
except KeyboardInterrupt:
     print('\nDone.')


