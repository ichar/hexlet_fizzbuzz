from src.fizzbuzz import check, walk

IsTrace = 1


def test_start():
    if IsTrace:
       print('>>>FizzBuzz Tests started.')

def test_check():
    
    assert check(12)== '12:Fizz'
    assert check(25)== '25:Buzz'
    assert check(90)== '90:FizzBuzz'
    assert ':'.join(walk(0,12, debug=1)) == 'FizzBuzz:Fizz:Buzz:Fizz:Fizz:Buzz:Fizz'

def test_finish():

    if IsTrace:
       print('>>>FizzBuzz Tests completed successfully.')
