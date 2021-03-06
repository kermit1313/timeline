[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT) [![Python version](https://img.shields.io/badge/python-v3.8-blue)](https://www.python.org/downloads/release/python-387/) [![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Stations

## Set up environment

### Prerequirements

* Python 3.8
* virtualenv

### Create virtualenv for project

```bash
python3 -m virtualenv .venv
```

* On windows:

```powershel
.venv\Scripts\activate.bat
```

* On Linux

```bash
source .venv/Scripts/activate
```

### Install requirements

```bash
pip install -r requirements/base.txt
```

for development purposes:

```bash
pip install -r requirements/local.txt
```

## Usage

List of commands and options

```bash
PYTHONPATH=. python stations/manage.py --help
```

### Calculate command

Runs calculation process to generate gant / timeline chart.

```bash
PYTHONPATH=. python stations/manage.py calculate -f sample/data.xlsx --sheetname "AD1" --start-date-time "2021-02-27 16:00"
```
