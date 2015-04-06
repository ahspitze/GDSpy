#get keyboard navigational input and handle exceptions
def navigate(k):
    options=['help','quit','load','analysis','export','diagnostic']
    i=0
    for o in options[0:k]:
        print(i+1,') ',o)
        i=i+1
    k=0
    while k < 1 or k > len(options):
        try:
            k=int(input('Enter the number only :'))
        except ValueError:
            k=0
    return k-1

#    
def filesave(arrayDat):
    name=input('Enter file name to export data as  ')
    print('availible data to export are: ')
    for entries in arrayDat:
        print(entries)
    print('all')
    eType=''
    while not eType in arrayDat and not eType=='all':
        eType=input('Export what? ')
    if eType !='all':       
        export= open(name, 'w')
        export.write(str(arrayDat[eType]))
        export.close()
        print(name,' written successfully')
    else:
        export= open(name, 'w')
        for entries in arrayDat:
            line=str(arrayDat[entries])
            export.write(line)
        export.close()
        print(name,' written successfully')
    
def console():
    k=99
    arrayDat={}
    while k != 1:
        if not arrayDat:
            k= navigate(3)
        else:
            k=navigate(5)
        if k==0:
            print('After a compatible file has been loaded, GDSpy can perform analysis operations or export data to a file.')
            print('You can also export the results of your analysis')
        if k==2:
            request=input('Enter a compatible microarray data file.  ')
            if '.soft' in request:
                import softopen
                arrayDat= softopen.dataRead(request)
                softopen.report(request, arrayDat['probeID'], arrayDat['GDS'])  
            else:
                print('Invalid file format, see documentation for supported formats')
        if k==3:
            if not arrayDat:
                print('No file has been loaded! Enter "load" to load a compatible file')
            else:
                import analysis
                                
                analysis.crunch(arrayDat)
        if k==4:
            if not arrayDat:
                print('No file has been loaded! Enter "load" to load a compatible file')
            else:
                filesave(arrayDat)
        if k==5:
            if not arrayDat:
                print('No file has been loaded! Enter "load" to load a compatible file')
            else:
                print(arrayDat['gExpress'][0:4])


        

print('Welcome to GDSpy \n Select "help" for more info or "load" to load a compatible microarray file')
console()
