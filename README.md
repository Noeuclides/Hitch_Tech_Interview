# Hitch Tech Interview

This repository consists of three tests related to data processing with pandas.

## Requirements
Python 3.7 < is needed, and also have postgresql configured on your local machine.

## Installation

Use the package manager [pipenv](https://pipenv-es.readthedocs.io/es/latest/) to set the virtualenv.
Once the repo is cloned, in the root directory run:
```bash
pipenv install
pipenv shell
```

### Usage

1. FixIt:
In the root directory is a file called FixIT.py that has a debugged code for some class methods and its calls.
```bash
python fixIT.py
```

2. pandasPractice:
In the directory inside the django project hitch_api, there is another directory called scripts that has the pandasPractice.py file that has processing data with pandas of a excel files (scripts/data dir).
```bash
python hitch_api/scripts/pandasPractice.py 
```

3. API:
The hitch_api directory contains the django project for the api based on the datasets on the scripts/data dir.
After activate the virtualenv run the following commands:

```bash
cd hitch_api
psql postgres -f scripts/create_db.sql
python manage.py migrate
python scripts/set_db.py
```
Then run the server and go to the browser
```bash
python manage.py runserver
```

The endpoints of the API are:
- api/player
- api/player/retrieve_update_destroy/<int:pk>
- api/team
- api/position
- api/college