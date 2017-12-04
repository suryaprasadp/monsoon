
# coding: utf-8

# In[68]:


#tabula-py can be used to parse pdf to data frame,csv and other formats. it can be installed using pip install tabula-py.
from tabula import convert_into


#importing pandas for dataframes 
import pandas as pd

#FUNCTION DEF: CONVERTS TABLE IN PDF TO CSV FILE FORMAT
#INPUT: PATH TO PDF FILE
#TASK: GENERATED CSV FILE
#OUTPUT: NULL

def pdftabletocsv(path):
    
    
    print("in parse")
    #writing the table from pdf into csv file
    convert_into(path,"output.csv",output_format='csv')
    
    
    #THE READ DATA IS NOT FORMATTED PROPERLY,HAVE TO CLEAN IT UP
    
    
    #read the csv file into pandas dataframe
    df = pd.read_csv('output.csv')
    
    
    # Remove the clubbing of 2016 column with Particulars By using decimal point as refernce to seperate number and strings
    
    
    for i in range(0,df.shape[0]): # looping through the rows of that column
        
        
        if(df.isnull().iloc[i,2]):  #if nan no need to do anything
            continue
        else:        
            data=format(df.iloc[i,2]).split('.')       #split by decimal point into 2 strings
            df.iloc[i,2]=data[0]+ '.'+ data[1][0:2]    # concat 2 decimal points to the number in first part  
            df.iloc[i,3]=data[1][2:]                   
            
            
    #mangle_dup_cols not supported yett, have to manually replace 2015. to 2015
    #unnamed columns are replaced by empty space

    df.columns = df.columns.str.replace('Unnamed.*', '')
    df.rename(columns={'2015.1': '2015','2016 Particulars' :'2016'}, inplace=True)
    df.columns.values[3]="Particulars"
    
    
    
    #the previous content in csv file has to be deleted
    f = open("output.csv", "w")
    f.truncate()
    f.close()
    
    #writing to csv file
    df.to_csv('output.csv',index=False)
    
    print("outparse")
    
    return

#pdftabletocsv('/home/surya/BalSheet.pdf')

    





# 
# 

# In[ ]:





