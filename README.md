# bot-crosswordsParser
## Purpose
This repo captures clues from NYTimes The Mini Crossword game. Captured clues are saved as JSON. Also, printed on the screen if desired.

## Dependencies
### Python
You need Python 3 run. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.
In Ubuntu, Mint and Debian you can install Python 3 like this:
```
$ sudo apt-get install python3 python3-pip
```

### Python Modules
bot-crosswordsParser depends on a few python modules to do its job. You can automatically installed like this:
```
$ pip install -r requirements.txt
```

## How to Build / Install and Run
### Clone Repository
To check out and use the latest source code
```
$ git clone https://github.com/batuhan0sanli/bot-crosswordsParser.git
```

### Virtual Environment Setup
To run independently
```
$ cd bot-crosswordsParser            # change to your project's directory
$ virtualenv -p python3 env          # create the env folder with a new virtual environment for python3
$ source env/bin/activate            # adjust shell to use binaries inside env as default
$ pip install --upgrade pip          # upgrade the package management tool pip
$ pip install -r requirements.txt    # download and compile a package into local env
```

### Run
```
$ python main.py
```

## Usage
```
usage: main.py [-h] [-s] [-l] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -s, --succesful       Returns information when the JSON file is succesfully saved.
  -l, --log             Log to the console.
  -p PATH, --path PATH  JSON file path.
```

## Examples
#### Only save JSON in same path
```
$ python main.py
```

#### Only save JSON in other path
```
$ python main.py -p ~/Desktop/crosswordsParser-clues.json
```

#### Save JSON and print the 'successful saved' message
```
$ python main.py -s

JSON file saved successfully.
```

#### Save JSON and print all message
```
$ python main.py -sl

=== Across ===
1. ___ Today (newspaper)
4. Down in the dumps
5. D.J.'s service
7. Internet giant that began as Jerry and David's Guide to the World Wide Web in 1994
8. Really fun time
=== Down ===
1. Same old, same old
2. Sister of Malia, daughter of Michelle
3. Spanish farewell
5. "I'm to blame for that," slangily
6. Foldable bed
JSON file saved successfully.
```
