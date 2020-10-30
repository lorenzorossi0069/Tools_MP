#! python3

import pandas as pd
import pyodbc as pyodbc 	#needs pip install pyodbc
import sys
import mod_MSoffice as mod

#in order to use graphic interface
import threading
import time
#import wx  # not found?
from tkinter import Tk
from tkinter.filedialog import askopenfilename

AccessTableNames = ['AnalogInput','AnalogOutput','DigitalInput','DigitalOutput']

#UseMode can be:
# GUI    =  Gui interface
# FIXED  =  for debug: keep fixed names and paths as source and destination
# CLI    =  command line interface
UseMode = 'GUI'
        
#MAIN
if __name__ == '__main__':
        #Create log file
        #logging.basicConfig(filename='Excel 2 Access.log', level=logging.INFO, format='%(asctime)s %(message)s')

        #clear path variables
        ExcelFilePath=''
        AccessFilePath=''

        #GUI interface
        if UseMode == 'GUI':
                Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                ExcelFilePath = askopenfilename(title="Source (Excel file)", filetypes=[("Excel files", "*.xlsx")]) # show an "Open" dialog box and return the path to the selected file
                print('ExcelFilePath = '+ExcelFilePath)
                if ExcelFilePath =='':
                        print('You didn\'t select an input Excel.xlsx file')
                        sys.exit()
                
                AccessFilePath = askopenfilename(title="Destination (Access file)", filetypes=[("Access files", "*.mdb")]) # show an "Open" dialog box and return the path to the selected file
                print('AccessFilePath = '+AccessFilePath)
                if AccessFilePath =='':
                        print('You didn\'t select a precompiled Access.mdb file')
                        sys.exit()

        #fixed filenames (debug mode)
        elif UseMode == 'FIXED':
                ExcelFilePath = r'C:\MP_KERNEL\MyStuff\Python\PrepConf\Source.xlsx'
                print('ExcelFilePath = '+ExcelFilePath)
                             
                AccessFilePath = r'C:\MP_KERNEL\MyStuff\Python\PrepConf\Dest.mdb'
                print('AccessFilePath = '+AccessFilePath)

        #Get the arguments from COMMAND LINE:
        elif UseMode == 'CLI':                            
                ExcelFilePath = "--"
                AccessFilePath = "--"
                if len(sys.argv) == 3:
                        #Expected number of arguments is correct
                        ExcelFilePath =   sys.argv[1]
                        AccessFilePath =  sys.argv[2]
                else:
                        print("Expected number of arguments is incorrect")
                        print("python configurator <ExcelFilePath> <AccessFilePath>")
                        sys.exit()
        else:
                #__file__ or sys.argv[0] is filename
                print('UseMode must be GUI, CLI or FIXED: edit UseMode in '+__file__)
                sys.exit()



###-----------------uso modulo mod con funzioni MS office (Excel ed Access)
f=mod.Excel(ExcelFilePath)
f.read()
xdo=f.extract_DO()
xdi=f.extract_DI()
xao=f.extract_AO()
xai=f.extract_AI_PT()


access = mod.Access(AccessFilePath)
access.open()
### read original access tables  :++++++++++++++++++++++++++++++++++++++
##print ('before execution')
##for table in AccessTableNames:
##        print('\nTable '+table)
##        access.readTable(table)
##        print(access.dbdf)
##

### end of experimantal code (remember to CLOSE)------------

AccessTableNames = ['AnalogInput','AnalogOutput','DigitalInput','DigitalOutput']


for table in AccessTableNames:
        #print('')
        print('Cleaning '+table)
        access.clearTable(table)
 
print('\n--AO')
access.writeTable(xao,'AnalogOutput')

print('\n--DO')
access.writeTable(xdo,'DigitalOutput')

print('\n--AI')
access.writeTable(xai,'AnalogInput')

print('\n--DI')
access.writeTable(xdi,'DigitalInput')

### read Access tables at end:++++++++++++++++++++++++++++++++++++++
##print ('after execution')
##for table in AccessTableNames:
##        print('\nTable '+table)
##        access.readTable(table)
##        print(access.dbdf)
##

### end of experimantal code (remember to CLOSE)------------


access.close()















        
