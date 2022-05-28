# hexlet_fizzbuzz

##HEXLET FizzBuzz test for [test job](https://hexlet-ru.notion.site/8b301b64d4834a3e91f709f8ada1187a)

###**Install:**

Check Python3 installed in your system together with `poetry` for tests (look at `poetry_info.txt`for setup)
Clone the repository from the GitHub-origin source to any `folder`:
```
cd <folder>
```

```
git clone https://github.com/ichar/hexlet_fizzbuzz
```

###**CLI:**
Open bin-folder with the CLI-script and set execute-mode flag for the script
```
cd /hexlet_fizzbuzz/bin
chmod +x ./fizz_buzz
```
and run it:
```
./fizz_buzz
```

###**Help:**
```
-> HEXLET FizzBuzz script
--> 
--> python3 fizzbuz.py [{-i|-c|-r|-t|-h}] [start [finish]]
--> 
--> -i: interactive mode with type a number request
--> example:fizzbuz.py -i
--> 
--> -c: only check a given start value
--> example:fizzbuz.py -c 21
--> 
--> -r: walk through the values range from start to finish, can be omitted
--> example:fizzbuz.py -r 0 100 or fizzbuz.py 0 100
--> 
--> -t: self tests
--> 
--> -h|-?|help: this help
--> 
--> start and finish should be an integer>=0, by default 0.
--> 
--> For tests run -t (module inner tests) or poetry branch from the root-package directory:
-->      poetry run pytest -s
```
###**Usage options:**

Run the ClI(examples):
  1) print results from 0 to 100 range:
```
  ./fizz_buzz 0 100
```
  2) check number 99 only:
```
  ./fizz_buzz -c 99
```
  3) run with interactive mode:
```
  ./fizz_buzz -i
```

**##Tests**
  -t: runs inner test mode (self tests) or use poetry as written above

  4) self-tests:
```
  ./fizz_buzz -t
```
Self-tests is valid if you'll get message:'Inner Tests OK'

  5) poetry-tests with script-prints:
```
  poetry run pytest -s
```
Poentry test s valid with these outputs:
tests/test_fizzbuzz.py >>>FizzBuzz Tests started.
...
.>>>FizzBuzz Tests completed successfully.




[Author] (https://ru.hexlet.io/u/mkarox)
