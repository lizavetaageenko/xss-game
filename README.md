# XSS-GAME

## Installation

### Install python 2.7 via brew, gzip, anaconda etc.

### Install pip:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```bash
[sudo] python get-pip.py
```

### Install `virtualenv`

```bash
[sudo] pip install virtualenv
```

### Create virtual environment

Go to project directory and run

```bash
virtualenv env
```

### Activate environment

```bash
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### To run specific level, go to level folder and run `.py` file inside of it, e.g.:

```bash
cd level1
python level1.py
```
Open [127.0.0.1:8008](http://127.0.0.1:8008)

## Credits

Origin source: https://xss-game.appspot.com