def navigate(k):
    k=k.lower()[0]
    if k=='q':
        print('quit')
        return 0
    elif k=='h':
        print('help')
        return 1
    else:
        print('invalid command, "help" for list of commands or "quit" to exit')
        return 99
    
def execute(k):
    if k==1:
        print('no one can help you now')

def console():
    q=99
    while q != 0:
        q= navigate(input(':   '))
        execute(q)

console()
