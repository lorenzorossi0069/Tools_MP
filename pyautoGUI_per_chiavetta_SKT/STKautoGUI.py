#! python3

import pyautogui
import datetime
import time
import sys
import os
import shutil
#import threading
import subprocess
import csv

#function definitions------------
def CheckFileExists(pathDir, fileName):
	#os.chdir(pathDir)
	if (os.path.isfile (fileName)):
		filesFound = True
		#print('SKT program found: now starting...')
	else:
		print ('file ' + fileName +' not found (in '+pathDir)
		sys.exit()

def CalcSKTpassword():   
    # "SKT" +(formula di calcolo; Dom=1)
    now = datetime.datetime.now()
    print (now.strftime("%Y-%m-%d"))
    yyyy = now.year
    mm = now.month
    dd = now.day
    wd = now.weekday()+2    # py_Dom = 0
    if wd>7:
        wd=1

    SKTpwd = 'SKT'+str(000000) #formula originale cancellata
    print(SKTpwd)
    return SKTpwd

def getPathDict():
        f=open('pathLocations.csv')
        pathsData=csv.reader(f)
        
        pathsDataList=list(pathsData) #potrebbe non servire?

        pathsDataDict={}
        for k,v in pathsDataList:
                pathsDataDict.setdefault(k,v)

        return pathsDataDict
        
#-------------------------------------
w, h = pyautogui.size()
print('screen size: ',w,',',h)

orig_path = os.getcwd()
print('orig_path = ',orig_path)



#CheckFileExists(r'C:\MP_KERNEL\TOOLS_private\W10\SPT2018_XLT (2.2.2)\Bin','UsbKeyTool.exe')

SKTpwd = CalcSKTpassword()
print('password = ',SKTpwd)

pathDict = getPathDict()
##f=open('pathLocations.csv')
##pathsData=csv.reader(f)
##        
##pathsDataList=list(pathsData) #potrebbe non servire?
##pathsDataDict={}
##for k,v in pathsDataList:
##        pathsDataDict.setdefault(k,v)
##print('dict:')
##print(pathsDataDict)
##for i in pathsDataDict.items():
##        print(i)
##
##
##
##
##sys.exit()

print('dict:')
for i in pathDict.items():
        print(i)

#os.chdir(r'C:\MP_KERNEL\TOOLS_private\W10\SPT2018_XLT (2.2.2)\Bin')
print('Launch program...')
##subprocess.Popen(r'C:\MP_KERNEL\TOOLS_private\W10\SPT2018_XLT (2.2.2)\Bin\UsbKeyTool.exe')
programToStart = str(pathDict['absPathBin'])+'\\UsbKeyTool.exe'
print(programToStart)
subprocess.Popen(programToStart)

time.sleep(5)

print('Press Ctrl-C to quit.')
try:
##    print('currentpath = ',str(os.getcwd()))
##    os.chdir(orig_path)
##    print('currentpath = ',str(os.getcwd()))

    #==============================================================
    #phase 1: launch SKT program and autoinsert calculated password
    
    #print('now path = ',str(os.getcwd()))
    #answ=pyautogui.locateOnScreen(r'C:\MP_KERNEL\2019MyStuff\Python\AutoGUI\1STKpwd.png')
    imgLocated = None

    SKTimg = str(pathDict['relPathPicsSKT'])+'\\1STKpwd.png'

    pyautogui.click(1,1) #move mouse out of where image will be located
    while (imgLocated == None):
        ##imgLocated=pyautogui.locateOnScreen('1STKpwd.png')
        imgLocated=pyautogui.locateOnScreen(SKTimg)
        print('password prompt not seen')
        
    x0 = imgLocated.left
    y0 = imgLocated.top
    w = imgLocated.width
    h = imgLocated.height
    print('x0,y0,w,h= ',x0,', ',y0,', ',w,', ',h)
    print('windows (x0,y0,x1,y1) = (',x0,',',y0,',',(x0+w),',',(y0+h))
    
    pyautogui.center(imgLocated)
    pyautogui.click(imgLocated)
    pyautogui.typewrite(SKTpwd)
    pyautogui.press('enter')

    #==============================================================
    #phase 2: select parameters file
    #subprocess.Popen(r'C:\MP_KERNEL\TOOLS_private\W10\SPT2018_XLT (2.2.2)\Bin\UsbKeyTool.exe')
    SecDataFilesPath= str(pathDict['absPathSecDataFiles'])
    ##subprocess.Popen('explorer'+' '+SecDataFilesPath)
    os.system('explorer'+' '+SecDataFilesPath)
    

    
    


    
except KeyboardInterrupt:
    print('\nQuitted due to Ctrl-C.')
      
