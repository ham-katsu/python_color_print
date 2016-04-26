def printc(st, col = 'wh', nl = True):

    output = ''
    colorset = {'wh' : 0, 'white' : 0, 'cri' : 1, 'crimson' : 1,
                'gra' : 3, 'gray' : 3, 're' : 4, 'red' : 4,
                'yel' : 5, 'yellow' : 5, 'blu' : 6, 'blue' : 6,
                'mag' : 7, 'magenta' : 7, 'cy' : 8, 'cyan' :8,
                'gre' : 9, 'green' : 9,
                'hcri' : 11, 'hcrimson' : 11,
                'hgr' : 13, 'hgray' : 13, 'hre' : 14, 'hred' : 14,
                'hyel' : 15, 'hyellow' : 15, 'hblu' : 16, 'hblue' : 16,
                'hmag' : 17, 'hmagenta' : 17, 'hcy' : 18, 'hcyan' :18,
                'hgre' : 19, 'hgreen' : 19,
                }

    try:
        code = colorset[col.lower()]
    
    except:
        code = 0
        printc("! color name !", 'Hre')


    if code == 0:
        output += "\033[1;37m"

    elif code == 1:
        output += "\033[1;38m"

    elif code == 3:
        output += "\033[1;30m"

    elif code == 4:
        output += "\033[1;31m"

    elif code == 5:
        output += "\033[1;33m"

    elif code == 6:
        output += "\033[1;34mm"

    elif code == 7:
        output += "\033[1;35mm"

    elif code == 8:
        output += "\033[1;36mm"

    elif code == 9:
        output += "\033[1;32mm"


    elif code == 11:
        output += "\033[1;48m"

    elif code == 13:
        output += "\033[1;47m"

    elif code == 14:
        output += "\033[1;41m"

    elif code == 15:
        output += "\033[1;43m"

    elif code == 16:
        output += "\033[1;44m"

    elif code == 17:
        output += "\033[1;45m"

    elif code == 18:
        output += "\033[1;46m"

    elif code == 19:
        output += "\033[1;42m"


    
    output += st
    output += "\033[1;m"

    if nl == True:
        print(output)
    
    else:
        print(output, end='')
