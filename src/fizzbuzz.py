import sys
import os
import re


is_v3 = sys.version_info[0] > 2 and True or False


version = '1.0 Python3'

config = {}

EOL = '\n'

IsDebug = 0
IsTrace = 1

def check(x):
    out = ''
    if x <= 0:
        pass
    s= not IsDebug and f"{x}:" or ''
    if IsTrace:
        print(f"Trace:{x}")
    if x%15 == 0:
        out=(f"{s}FizzBuzz")
    elif x%5 == 0:
        out =(f"{s}Buzz")
    elif x%3 == 0:
        out=(f"{s}Fizz")

    if out:
        print(out)
    return out

def walk(v1, v2=0, **kw):
    global IsDebug, IsTrace
    IsDebug=kw.get('debug', 0)
    IsTrace=kw.get('trace', 0)
    out = []
    begin = v1 > 0 and v1
    end = v2>0 and v2+1 or v1+1
    for x in range(begin, end):
        out.append(check(x))

    out = [x for x in out if x]
    if IsTrace:
        print('Trace:', out)
    return out

def interactive():
    while True:
        x=input('Type an integer, please, or q for exit:')
        if x == 'q' or not x.isdigit():
            return
        else:
            check(int(x))

def test():
    assert ':'.join(walk(0,12, debug=1)) == 'FizzBuzz:Fizz:Buzz:Fizz:Fizz:Buzz:Fizz'
    assert ':'.join(walk(100, debug=1, trace=0)) == 'Buzz'
    
    print('Test OK')

if __name__ == "__main__":
    argv = sys.argv


    if len(argv) == 1 or argv[1].lower() in ('/h', '-h', 'help', '--help', '/?'):
        print('--> FizzBuzz script')
        print('--> ')
        print('--> python3 fizzbuz.py [{-i|-c|-r|-t}] [start [finish]]')
        print('--> ')
        print('--> -i: interactive mode with type a number request')
        print('--> example:fizzbuz.py -i')
        print('--> ')
        print('--> -c: only check a given start value')
        print('--> example:fizzbuz.py -c 21')
        print('--> ')
        print('--> -r: walk through the values range from start to finish')
        print('--> example:fizzbuz.py -r 0 100 or fizzbuz.py 0 100')
        print('--> ')
        print('--> -t: tests')
        print('--> ')
        print('--> start and finish should be an integer number>=0.')
        print('--> ')
        print('--> %s' % version)
    else:
        x1 = x2 = None
        is_interact = 0
        is_check = 0
        is_range = 0
        is_test = 0
        for arg in argv[1:]:
            if arg.startswith('-'):
                if arg == '-i':
                    is_interact = 1
                if arg == '-c':
                    is_check = 1
                if arg == '-r':
                    is_range = 1
                if arg == '-t':
                    is_test = 1
            elif arg.isdigit():
                if x1 is None:
                    x1=int(arg)
                elif is_range or not is_check:
                    x2=int(arg)
                    is_range = 1
                    is_check = 0

        if IsTrace:
            print(f"Trace:{x1}:{x2}")

        if is_test:
            test()
        elif is_interact:
              interactive()      
        else:
            walk(x1,x2 or 0, trace=0)
