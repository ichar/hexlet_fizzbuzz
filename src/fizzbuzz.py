import sys

#
# https://hexlet-ru.notion.site/8b301b64d4834a3e91f709f8ada1187a
#


is_v3 = sys.version_info[0] > 2 and True or False


version = '1.0 with tests Python3, https://ru.hexlet.io/u/mkarox'

config = {}

EOL = '\n'

IsDebug = 0
IsTrace = 1

def check(x):
    if IsTrace:
        print(f"check:{x}...")
    out = ''
    if x <= 0:
        pass
    s= not IsDebug and f"{x}:" or ''
    #if IsTrace:
    #    print(f"Trace:{x}")
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
    if IsTrace:
        print('walk...')
    out = []
    begin = v1 and v1 > 0 and v1 or 0
    end = v2>0 and v2+1 or v1+1
    for x in range(begin, end):
        out.append(check(x))

    out = [x for x in out if x]
    if IsTrace:
        print('Trace out:', out)
    return out

def interactive():
    if IsTrace:
        print('interactive...')
    while True:
        x=input('Type an integer, please, or q for exit:')
        if x == 'q' or not x.isdigit():
            return
        else:
            check(int(x))

def inner_tests():
    if IsTrace:
        print('inner_tests...')
    assert ':'.join(walk(0,12, debug=1)) == 'FizzBuzz:Fizz:Buzz:Fizz:Fizz:Buzz:Fizz'
    assert ':'.join(walk(100, debug=1, trace=0)) == 'Buzz'
    
    print('Inner Tests OK')

def help():
    if IsTrace:
        print('help...')

    print('--> HEXLET FizzBuzz script')
    print('--> ')
    print('--> python3 fizzbuz.py [{-i|-c|-r|-t|-h}] [start [finish]]')
    print('--> ')
    print('--> -i: interactive mode with type a number request')
    print('--> example:fizzbuz.py -i')
    print('--> ')
    print('--> -c: only check a given start value')
    print('--> example:fizzbuz.py -c 21')
    print('--> ')
    print('--> -r: walk through the values range from start to finish, can be omitted')
    print('--> example:fizzbuz.py -r 0 100 or fizzbuz.py 0 100')
    print('--> ')
    print('--> -t: self tests')
    print('--> ')
    print('--> -h|-?|help: this help')
    print('--> ')
    print('--> start and finish should be an integer>=0, by default 0.')
    print('--> ')
    print('--> For tests run -t (module inner tests) or poetry branch from the root-pakage directory:')
    print('-->      poetry run pytest -s') 
    print('--> ')
    print('--> ')
    print('--> %s' % version)
    return 0
    

def main():
    if IsTrace:
        print('main...')

    argv = sys.argv
#
#   CHECK HELP
#
    if len(argv) == 1 or argv[1].lower() in ('/h', '-h', 'help', '--help', '/?', '-?'):
        sys.exit(help())
#
#   START SCRIPT
#
#   Options:
    is_interact = 0
    is_check = 0
    is_range = 0
    is_test = 0
#   Data to iterate
    start = finish = None
#   Parsing of arguments...
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
            if start is None:
                start=int(arg)
            elif is_range or not is_check:
                finish=int(arg)
                is_range = 1
                is_check = 0

    if IsTrace:
        print(f"Trace Data:{start}:{finish}")

    if is_test:
        inner_tests()
    elif is_interact:
          interactive()
    elif is_check:
        check(start)
    else:
        walk(start,finish or 0, trace=0)


if __name__ == "__main__":
    main()
