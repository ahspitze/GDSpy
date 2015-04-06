
def crunch(arrayDat):

    #unpack relevant variables
    header=arrayDat['header']
    gExpress=arrayDat['gExpress']
    GDS=arrayDat['GDS']
    subsets=GDS['subsets']
    sType=GDS['subset_types']
    sName=GDS['subset_names']

    print('Enter the number of the operation to perform :')
    procedure=int(input(' 1) fold change 2) back '))
    if procedure==1:
        xfoldChange=foldChange(sType, sName, subsets, header, gExpress)
        arrayDat['fold change']=xfoldChange
        print('analyzed ',len(xfoldChange),'. Maximum ', max(xfoldChange))
    return arrayDat


#Calc Fold Change#
#finds the fold-change from the first set of samples to the second
#e.g. sample at 1 day= 10 -> sample 3 days=100 is a 10-fold change
def foldChange(sType, sName, subsets, header, gExpress):    
    samples=pickTwo(sType, sName,subsets)
    xfoldChange=[]
    error=0

    #loop through gExpress using header[j] in subset to sort values into totals
    #probes iterated by i, samples iterated by j
    i=0
    for probe in gExpress:
        j=0
        totalA=0
        totalB=0
        
        for gsm in header:
            
            if gsm in samples[0]:
                totalA = gExpress[i][j]+ totalA
                
            elif gsm in samples[1]:
                totalB= gExpress[i][j]+ totalB
            else:
                error='very yes'
            j=j+1
        meanA=totalA/len(samples[0])
        meanB=totalB/len(samples[1])
        try:
            #fold change from A to B
            xfoldChange.append(meanB/meanA)
        except ZeroDivisionError:
            #to catch errors for zero values
            xfoldChange.append(-99)
        i=i+1
    if error=='very yes':
        print('completed with errors')
    return xfoldChange

#define 2 subsets for comparison, get that info from the user
def pickTwo(sType, sName, subsets):

    
    t=[]
    print('Compare within which subset type?')
    for types in set(sType):
        t==t.append(types)
        print(len(t), ') ', types)
    select=int(input('Enter the number only :'))-1
    i=0
    for types in sType:
        if types==t[select]:
            sType[i]=1
        else:
            sType[i]=0
        i=i+1
    i=0
    j=0
    n=[]

    #choose two subsets of same type
    print('Compare which subsets? (select first subset)')
    for names in sName:
        if sType[i]==1:
            print(j+1, ') ', names)
            n.append(names)
            j=j+1
        i=i+1
            
    select=int(input('Enter the number only :'))-1
    i=0
    j=0
    m=[]
    print('Compare which subsets? (select second subset)')
    for names in n:
        if names != n[select]:
            print(j+1, ') ',names)
            m.append(names)
            j=j+1
        
    select2=int(input('Enter the number only :'))-1

    #populate lists groupA and groupB from subsets
    #relies on the fact that sName and subsets are parallel arrays
    for names in sName:
        if names==n[select]:
            groupA=(subsets[i])
        elif names==m[select2]:
            groupB=(subsets[i])
        else:
            sName[i]=0
        i=i+1

    samples=[groupA,groupB]
    return samples
            
        
