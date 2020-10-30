#! python3

# ModulePrepareConf.py
# module functions for PrepareConf
#(Prepare AccessDB Config.mdb starting from Excel Channel Diagram of Microplan)

import pandas as pd
import pyodbc as pyodbc 	#needs pip install pyodbc
import sys

class Excel:
    '''Excel object at specified path'''
    def __init__(self, ExcelFilePath):
        '''init Excel object'''
        self.ExcelFilePath = ExcelFilePath
             
    def read(self):
        '''read excel file'''
        self.xdf = pd.read_excel(self.ExcelFilePath)
        #replace all NaN values with a null string
        self.xdf.fillna('',inplace=True)
        self.nRows, self.nCols = self.xdf.shape
        return self.xdf

    def extract_DO(self):
        '''Returns a reference to self.DO_xdf'''

        columnNames_DO = ['ChName','ChAlias','DeviceId','Description','Circuit','Address','Invert','NoReset']

        self.DO_xdf=pd.DataFrame(columns=columnNames_DO)
        
        print('--- DO channels ---')
        i=0
        for y in range(self.nRows):
            cell=self.xdf.iloc[y,1]
            if 'DO' in cell:
                ChName = self.xdf.iloc[y,1] #da sostituire con TECHNICAL NAME!!!!!!!!!! o da editare poi a mano
                ChAlias = self.xdf.iloc[y,2]
                DeviceId = 'Wago' #da editare poi a mano

                Description = self.xdf.iloc[y,3]
                if Description == '':
                    Description = 'DO available'
                    
                Circuit = 'electric' #da editare poi a mano
                Address = i
                i=i+1
                Invert = False #da editare poi a mano
                NoReset = False #da editare poi a mano
                
                #create a list of above set values
                tmpList= [ChName,ChAlias,DeviceId,Description,Circuit,Address,Invert,NoReset]
                
                tmpDf = pd.DataFrame([tmpList],columns=columnNames_DO)
                tmpDf.fillna('--',inplace=True)
                
                self.DO_xdf = self.DO_xdf.append(tmpDf,ignore_index=True)      
        return self.DO_xdf

    def extract_DI(self):
        '''Returns a reference to self.DI_xdf'''

        columnNames_DI = ['ChName','ChAlias','DeviceId','Description','Address']

        self.DI_xdf=pd.DataFrame(columns=columnNames_DI)
        
        print('--- DI channels ---')
        i=0
        for y in range(self.nRows):
            cell=self.xdf.iloc[y,1]
            if 'DI' in cell:
                ChName = self.xdf.iloc[y,1] #da sostituire con TECHNICAL NAME!!!!!!!!!! o da editare poi a mano
                ChAlias = self.xdf.iloc[y,2]
                DeviceId = 'Wago' #da editare poi a mano

                Description = self.xdf.iloc[y,3]
                if Description == '':
                    Description = 'DI available'
                    
                Address = i
                i=i+1
                                
                #create a list of above set values
                tmpList= [ChName,ChAlias,DeviceId,Description,Address]
                
                tmpDf = pd.DataFrame([tmpList],columns=columnNames_DI)
                tmpDf.fillna('--',inplace=True)
                
                self.DI_xdf = self.DI_xdf.append(tmpDf,ignore_index=True)      
        return self.DI_xdf

    def extract_AO(self):
        '''Returns a reference to self.AO_xdf'''
        columnNames_AO = ['ChName','ChAlias','Description','DeviceId','InitString','MinOutElect','MaxOutElect','MinOutReal',
         'MaxOutReal','InitValue','Unit','FixedOffset','Invert','ShowPanel','Manual','ReverseActing',
         'PIDCycleT','PIDProp','PIDInt','PIDDer']

        self.AO_xdf=pd.DataFrame(columns=columnNames_AO)
                
        print('--- AO channels ---')
        i=0
        for y in range(self.nRows):
            cell=self.xdf.iloc[y,1]
            if 'AO' in cell:
                
                ChName = self.xdf.iloc[y,1] #da sostituire con TECHNICAL NAME!!!!!!!!!! o da editare poi a mano
                ChAlias = self.xdf.iloc[y,2]
                
                Description = self.xdf.iloc[y,3]
                if Description == '':
                    Description = 'AO available'
                
                DeviceId = 'Wago' #da editare poi a mano
                InitString = 'AO:'+str(i)
                i=i+1
                MinOutElect = 0
                MaxOutElect = 32767
                MinOutReal = 0
                MaxOutReal = 100
                InitValue = 0
                Unit = '%'
                FixedOffset = 0
                Invert = False
                ShowPanel = False
                Manual = False
                ReverseActing = False
                PIDCycleT = 100
                PIDProp = 100
                PIDInt = 0
                PIDDer = 0
                                
                #create a list of above set values
                tmpList = [ChName,ChAlias,Description,DeviceId,InitString,MinOutElect,MaxOutElect,MinOutReal,MaxOutReal,InitValue,Unit,
                           FixedOffset,Invert,ShowPanel,Manual,ReverseActing,
                           PIDCycleT,PIDProp,PIDInt,PIDDer]

                tmpDf = pd.DataFrame([tmpList],columns=columnNames_AO)
                tmpDf.fillna('--',inplace=True)
                
                self.AO_xdf = self.AO_xdf.append(tmpDf,ignore_index=True)      
        return self.AO_xdf


    def extract_AI_PT(self):
        '''Returns a reference to self.AI_PT_xdf'''
        
        columnNames_AI_PT = ['ChName','ChAlias','DeviceId','Description',
                              'Address','AddressSimu','SignalType',
                              'ConversionType','Grade','FixedOffset',
                              'Damping','MINScale','MAXScale','DefaultError',
                              'RepName','Unit','Params','Precision',
                              'Scale','UserInput']

        self.AI_PT_xdf=pd.DataFrame(columns=columnNames_AI_PT)
                
        print('--- AI_PT channels ---')
        i=0
        for y in range(self.nRows):
            cell=self.xdf.iloc[y,1]
            #if 'AO' in cell:
            if ('AI' in cell) or ('PT' in cell) or ('TC' in cell):
                
                ChName = self.xdf.iloc[y,1]
                ChAlias = self.xdf.iloc[y,2]
                DeviceId = 'Wago' #da editare poi a mano

                Description = self.xdf.iloc[y,3]
                if Description == '':
                    if 'AI' in cell:
                        Description = 'AI available'
                    if 'PT' in cell:
                        Description = 'PT available'
                    if 'TC' in cell:
                        Description = 'TC available'


                Address = i;        i=i+1
                AddressSimu = i;    i=i+1
                
                if ('PT' in cell):
                    SignalType =  'WAI0-20'
                else:
                     SignalType =  'WAI0-20' #tutto ciò che non è PT?
                     
                ConversionType = 1
                Grade = 1
                FixedOffset = 0
                Damping = 1
                MINScale = 0
                MAXScale = 100 #da modificare!!
                DefaultError = 'Error on '#+str(cell)
                RepName = 'prova' #str(cell) #+'-'+'Unità'
                Unit = 'Unit'
                Params = 'aaa'
                Precision = 0
                Scale = 0
                UserInput = False               
               
                                
                #create a list of above set values
                tmpList = [ChName,ChAlias,DeviceId,Description,Address,AddressSimu,SignalType,
                      ConversionType,Grade,FixedOffset,Damping,MINScale,MAXScale,DefaultError,
                      RepName,Unit,Params,Precision,Scale,UserInput]

                tmpDf = pd.DataFrame([tmpList],columns=columnNames_AI_PT)
                tmpDf.fillna('--',inplace=True)
                
                self.AI_PT_xdf = self.AI_PT_xdf.append(tmpDf,ignore_index=True)      
        return self.AI_PT_xdf


    def writeAppend(self, indf):
        '''Append a dataframe to an Excel worksheet'''
        pass
        

class Access:
    '''Access object at specified path'''
    def __init__(self, AccessFilePath):
        '''init Acess class object with conn_string'''
        self.AccessFilePath = AccessFilePath

    def open(self):
        '''open connection to Access DB'''
        self.conn_string = (
                r"Driver={Microsoft Access Driver (*.mdb)};"
                r"Dbq="+self.AccessFilePath+";"
                r"UID=admin;"
                r"PWD=myPassword;") #note: insert correct password instead of myPassword
        try:
            self.conn=pyodbc.connect(self.conn_string)
            self.cursor = self.conn.cursor()
        except:
            print('error: connection to Access failed')
            sys.exit()



    def close(self):
        '''close connection to Access DB'''
        self.conn.close()
        print('closed connection')
    

     
    def clearTable(self, table):
        '''Delete all records in Access table'''
        try:
            sqlString = 'DELETE FROM ' + table
            self.cursor.execute(sqlString)
            self.conn.commit()
        except:
            print('exception at delete table step')
            self.conn.close()
            print('error clearing Access table: close connection')
            sys.exit()


        
    def writeTable(self, df, table):
        '''Write on (empty) Access DB table'''
        print('\nwriting on access table '+table)
        try:
            #columns list format must be: [col_1],[col_2],[col_3],[col_4]
            cols=''   
            for colName in list(df.columns):
                cols=cols+'['+ colName + '],'

            #remove last string's comma char ( , )
            cols=cols[0:-1]
            
            print ('cols = '+cols) #debug print
      
            #prepare the command string (done once for each record in a loop cycle)
            for i in range(df.shape[0]): #dim[0]=number of records (y)
                #xdf.iloc[i] select i-th row of dataframe table, enclosed in squared brackets []
                record = str(list(df.iloc[i]))
                #remove first and last characters from string (squared brackets [])
                record=record[1:-1] 
                #compose SQL command for a single record
                sqlString = 'INSERT INTO '+ table + ' (' + cols + ') VALUES (' + record + ')'
                #print('sqlString = '+sqlString) #debug print
                #execute SQL command
                self.cursor.execute(sqlString)
                
                #commit change (for each record)
                self.conn.commit() 

        except Exception as emsg:
            print('\nexception at write table when at line '+str(i))
            print(str(emsg))
            self.conn.close()
            self.conn.close()
            print('error: close connection')
            sys.exit()



    def readTable(self, table):
        '''read access table; to be done: save to a Datafrane!!! '''
        try:
            sqlString = 'select * from ' + table
            #execute SQL command, and save result into qry
            qry = self.cursor.execute(sqlString)

            #get results set (all rows)
            self.dbdf = pd.DataFrame(qry.fetchall())

            #return query result
            return self.dbdf
            
        except Exception as emsg:
            print('exception reading Access'' table '+table)
            print(str(emsg))
            self.conn.close()
            self.conn.close()
            print('error: close connection')
            sys.exit()


 
