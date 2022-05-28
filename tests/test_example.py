from src.example import reverse

IsDebug = 0
IsTrace = 1

def test_start():

    if IsTrace:
       print('>>>Tests started.')

def test_reverse():
    assert reverse('!dlroW ,olleH') == 'Hello, World!'
    if IsTrace:
        print('>>>test_reverse 1 ...: OK')
    assert reverse('1234567890') == '0987654321'
    if IsTrace:
        print('>>>test_reverse 2 ...: OK')
    assert reverse([1,2,3,4,5,6,7,8,9,0]) == [0,9,8,7,6,5,4,3,2,1]
    if IsTrace:
        print('>>>test_reverse 3 ...: OK')
    if IsDebug:
        if IsTrace:
            print('>>>test_reverse 4 ...: ERROR')
        assert reverse('1234567890') == '9876543210'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_finish():

    if IsTrace:
       print('>>>Tests completed successfully.')
