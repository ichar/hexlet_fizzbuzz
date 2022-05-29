import sys

# Hexlet Python Mentor test job:
# https://hexlet-ru.notion.site/8b301b64d4834a3e91f709f8ada1187a
#


IS_V3 = sys.version_info[0] > 2 and True or False

_VERSION_ = '1.0 with tests Python3, https://ru.hexlet.io/u/mkarox'

ISDEBUG = 0
ISTRACE = 1


def check(x):
    """
        Checks a number and print results or return it.

        Arguments:
            x -- int, nimber to check, x >= 0
        Returns:
            results string code as {Fizz|Buzz|FizzBuzz} or empty string
    """
    if ISTRACE:
        print(f"check:{x}...")
    out = ''
    if x <= 0:
        pass
    s = not ISDEBUG and f"{x}:" or ''
    if ISTRACE:
        print(f"Trace:{x}")
    if x % 15 == 0:
        out = f"{s}FizzBuzz"
    elif x % 5 == 0:
        out = f"{s}Buzz"
    elif x % 3 == 0:
        out = f"{s}Fizz"

    if out:
        print(out)
    return out


def walk(v1, v2=0, **kw):
    """
        Iterates given number sequences from v1 to v2 and checks 
        the results.

        Arguments:
            v1 -- int, start from this
            v2 -- int, finish to this
        Keyword arguments:
            debug -- bool or 1|0, set ISDEBUG option (prints prefered 
                        value to check in output such as 21:'21:Fizz')
            trace -- bool or 1|0, set ISTRACE option (prints script's 
                        trace output: Trace:....)

        Returns:
            out -- str: final script's result-string as join any given 
                    values to check specially for tests
    """
    global ISDEBUG, ISTRACE
    ISDEBUG = kw.get('debug', 0)
    ISTRACE = kw.get('trace', 0)
    if ISTRACE:
        print('walk...')
    out = []
    begin = v1 if v1 > 0 else 0
    end = v2 + 1 if v2 > 0 else v1 + 1
    for x in range(begin, end):
        out.append(check(x))

    out = [x for x in out if x]
    if ISTRACE:
        print('Trace out:', out)
    return out


def interactive():
    """
        Runs interactive script mode
    """
    if ISTRACE:
        print('interactive...')
    while True:
        x = input('Type an integer, please, or q for exit:')
        if x == 'q' or not x.isdigit():
            return
        check(int(x))


def inner_tests():
    """
        Inner tests (self-tests)
    """
    if ISTRACE:
        print('inner_tests...')
    assert ':'.join(walk(0, 12, debug=1)) == 'FizzBuzz:Fizz:Buzz:Fizz:Fizz:Buzz:Fizz'
    assert ':'.join(walk(100, debug=1, trace=0)) == 'Buzz'

    print('Inner Tests OK')


def inner_help():
    """
        Prints help for the script.

        Valid command line options for activate: 
            /h, 
            -h, 
            help, 
            --help, 
            /?, 
            -?
    """
    if ISTRACE:
        print('help...')

    print('--> HEXLET FizzBuzz script')
    print('--> ')
    print('--> python3 fizzbuzz.py [{-i|-c|-r|-t|-h}] [start [finish]]')
    print('--> ')
    print('--> -i: interactive mode with type a number request')
    print('--> example:fizzbuzz.py -i')
    print('--> ')
    print('--> -c: only check a given start value')
    print('--> example:fizzbuzz.py -c 21')
    print('--> ')
    print('--> -r: walk through the values range from start to finish, can be omitted')
    print('--> example:fizzbuzz.py -r 0 100 or fizzbuzz.py 0 100')
    print('--> ')
    print('--> -t: self tests')
    print('--> ')
    print('--> -h|-?|help: this help')
    print('--> ')
    print('--> start and finish should be an integer>=0, by default 0.')
    print('--> ')
    print('--> For tests run -t (module inner tests) or poetry branch from the root-package directory:')
    print('-->      poetry run pytest -s')
    print('--> ')
    print('--> ')
    print('--> %s' % _VERSION_)
    return 0


def main():
    """
        Main script enter point. Check arguments passed in command line
        and runs it in the given mode.

        Nothing returns.

        Script's Global Flags:
            ISDEBUG: 1|0 runs debug mode during script running.
            ISTRACE: 1|0 prints script Trace output in the execution 
            points (look at the docstrings above).
    """
    if not IS_V3:
        print('Sorry. The script is not convenient for interpreter version'
              'Please install Python3.')
        sys.exit(-1)
    if ISTRACE:
        print('main...')

    argv = sys.argv
    #
    #   CHECK HELP
    #
    if len(argv) == 1 or argv[1].lower() in ('/h', '-h', 'help', '--help', '/?', '-?'):
        sys.exit(inner_help())
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
                start = int(arg)
            elif is_range or not is_check:
                finish = int(arg)
                is_range = 1
                is_check = 0

    if ISTRACE:
        print(f"Trace Data:{start}:{finish}")

    if is_test:
        inner_tests()
    elif is_interact:
        interactive()
    elif is_check:
        check(start)
    else:
        walk(start, finish, trace=0)


if __name__ == "__main__":
    main()
