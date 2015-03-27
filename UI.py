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
    else:
        print('invalid command, "help" for list of commands or "quit" to exit')
        return 99

    
def filesave(arrayDat):
    name=input('Type file name to export data as')
    export= open(name, 'w')
    for entries in arrayDat:
        line=str(entries)+'\n'
        export.write(line)
    export.close()


    
def console():
    k=99
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
                print('No file has been loaded! Type "load" to load a compatible file')
            else:
                print(arrayDat['gExpress'][0:4])
        if k==4:
            if not arrayDat:
                print('No file has been loaded! Type "load" to load a compatible file')
            else:
                filesave(arrayDat)

        


console()
