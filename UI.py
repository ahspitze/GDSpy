def navigate(k):
    k=k.lower()[0]
    if k=='q':
        print('quit')
        return 0
    elif k=='h':
        print('help')
        return 1
    elif k=='l':
        print('load')
        return 2
    elif k=='d':
        print('diagnostic')
        return 3
    elif k=='e':
        print('export')
        return 4
    elif k=='a':
        print('analysis')
        return 5    
    else:
        print('invalid command, Enter "help" for list of commands or "quit" to exit')
        return 99

#    
def filesave(arrayDat):
    name=input('Enter file name to export data as  ')
    print('availible data to export are: ')
    for entries in arrayDat:
        print(entries)
    print('all')
    eType=input('Export what? ')
    if eType !='all':       
        export= open(name, 'w')
        export.write(str(arrayDat[eType]))
        export.close()
    else:
        export= open(name, 'w')
        for entries in arrayDat:
            line=str(arrayDat[entries])
            export.write(line)
        export.close()
    
def console(k):
    arrayDat={}
    while k != 0:
        k= navigate(input(':   '))
        if k==1:
            print('no one can help you now')
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
                print(arrayDat['gExpress'][0:4])
        if k==4:
            if not arrayDat:
                print('No file has been loaded! Enter "load" to load a compatible file')
            else:
                filesave(arrayDat)
        if k==5:
            if not arrayDat:
                print('No file has been loaded! Enter "load" to load a compatible file')
            else:
                import analysis
                                
                analysis.crunch(arrayDat)
        

print('Welcome to GDSpy \n Enter "load" to load a dataset or "help" for more options')
console(99)
