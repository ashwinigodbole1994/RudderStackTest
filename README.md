This repository contains REST API Testing automation code using Pytest framework

The project uses:
1. Python 3.9 and higher
2. Pytest
3. Requests
4. Pytest inbuitlt reporting
5. CI (GitHub actions)

Testing application:

url: https://api.rudderstack.com

### How to start
To install on mac use:
```
pip install pytest
```

By using Mac Terminal, Python and pip
1. Place the repository files into the directory of your choice.
2. Create virtual environment
```
py -m venv env
```
```
3. Install project's dependencies  
```
pip install -r requirements.txt
```

### How to run tests

```
All tests:
```
pytest
```

```
Also you can directly run any test by clicking on green icon btn supported in pytest 
```

**The folder structure is divided into following structure**
1. common directory : the common folder contains all the common classes which needs to be consumed overall framework . eg constant.ts helper classs wher helper methods are store 
2. src : the src directory contains modules wise folder . and each module has associated step classes having  method associated with it . eg auth folder has class related to authentication, same way for source and destination too
3. tests: Tests directory consist of all test related class files . All test start with prefix **test_** Pytest understand that they are test using this pregix
4. conftest.py: this is the entry file for running all test . All fixture and variable are defined in this file .If you have multiple test modules and want to share fixtures among them, placing the fixtures in conftest.py makes them automatically available to all the test modules.
