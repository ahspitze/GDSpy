##
#Tools for opening and working with Gene expression Data Sets (GDS)
# .soft and full soft formats

try:
    import csv
except ImportError:
    print('Dependency warning! This module requires the CSV library')

#floatConvert(frame,bad)
#convert strings to floats
#GDSs will occasionally have problematic values like 'null'
#the second argument flags nonfloatable elements (bad)
#remember to trim before using statistical comparisons
#or otherwise account for missing data
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





def dataRead (file):
    readIt= csv.reader(open(file), delimiter='\t')
#initializations for various counters and lists

    row=[0]
    header=[]   # sample header info for expression values
    probeRef={} # dictionary of probes and their corresponding gene symbols
    probeID=[]  # list of gene symbols
    gExpress=[] # 2D array of gene expression values
    subsets=[]  # 2D list of experimental subsets
    sType=[]    # parallel list of subset types (agent, control, time series, etc) for list in subsets[]
    sDescrip=[] # parallel list of subset names (infection, control, patient 16, etc) for list in subsets []
    GDS={}      # GDS metadata including subsets
    arrayDat={} #wrapper for everything to passed for analysis



    print('loading')

    #process and divide dataset annotation


    while row[0] !='!dataset_table_begin':  
        row=next(readIt)
        if row[0] != '!dataset_table_begin':
            if row[0][:17]=='!subset_sample_id':
                subsets.append(row[0][20:].split(','))
            elif '=' in row[0] and '!' in row[0] and'subset_type' in row[0]:
                a=row[0].split(' = ')
                sType.append(a[1])
            elif '=' in row[0] and '!' in row[0] and'subset_description' in row[0]:
                a=row[0].split(' = ')
                sDescrip.append(a[1])
            elif '=' in row[0] and '!' in row[0] and not 'subset' in row[0]:
                a=row[0].split(' = ')
                try:
                    a[1]=int(a[1])
                except ValueError:
                    pass
                GDS[a[0][1:].lower()]=a[1]
            
                
        else: pass

    GDS['subsets']=subsets
    GDS['subset_types']=sType
    GDS['subset_names']=sDescrip
    samples= GDS['dataset_sample_count']    
        
    #sample names grouped into a header
    row=next(readIt)
    header.append(row[2:samples+2])


    #Begin the data read and terminate before the last row

    while row[0] != '!dataset_table_end' :
        row=next(readIt)
        if row[0] != '!dataset_table_end':
            probeRef[row[0]]=row[1]
            probeID.append(row[1])
            gExpress.append(row[2:(samples+2)])
        else:
            pass
    gExpress=floatConvert(gExpress,-99)
     #consolidate data into a single dictionary so it can be more easily passed to analysis routines
        
    arrayDat['GDS'],arrayDat['header'],arrayDat['gExpress']=GDS,header[0],gExpress
    arrayDat['probeID'], arrayDat['probeRef']=probeID,probeRef
    return arrayDat


def report(file, probeID, GDS):
    print(file,' loaded successfully with ',len(probeID),' features.')
    print('Detected ',GDS['dataset_sample_count'],' samples, ',len(GDS['subsets']),' groups')




###
print('\n','.SOFT library initialized')


###########################################################################    




