##
#Tools for opening and working with Gene expression Data Sets (GDS)
# .soft and full soft formats

import csv

#floatConvert(frame,bad)
#convert strings to floats
#GDSs will occasionally have problematic values like 'null'
#the second argument flags nonfloatable elements (bad)
#you can use negatives to push them to the bottom of ordering functions
#remember to trim before using statistical comparisons
def floatConvert(frame,bad):
    countX=0    
    for x in frame:
        countY=0
        for y in x:
            try:
                frame[countX][countY]=float(y)
                countY=countY+1
            except ValueError:
                frame[countX][countY]=bad
                countY=countY+1
        countX= countX+1
    return  frame




#csv objectt
file='array2.soft'
fileIt= open(file)
readIt= csv.reader(fileIt, delimiter='\t')



#initializations for various counters and lists

row=[0]
info=[]
header=[]
probeRef=[]
probeID=[]
gExpress=[]
samples=0


#First group all database annotation into a list called info
#and use this data to count the number of samples
while row[0] !='!dataset_table_begin':  
    row=next(readIt)
    if row[0] != '!dataset_table_begin':
        info.append(row[0])
        if row[0][:4]=='#GSM':
            samples=samples+1
    else: pass
    
#column names grouped into a header
row=next(readIt)
header.append(row)


#Begin the data read and terminate before the last row

while row[0] != '!dataset_table_end' :
    row=next(readIt)
    if row[0] != '!dataset_table_end':
        probeRef.append(row[0])
        probeID.append(row[1])
        gExpress.append(row[2:(samples+2)])
    else:
        pass
    
print(file,' loaded successfully with ',len(probeRef),' probes.')
print('Detected ',samples,' samples.')





gExpress=floatConvert(gExpress,-1)






#print(gExpress[0:4])

###
print('\n','done')


###########################################################################    




