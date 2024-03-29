# activity-planner

## Setup Instructions

1. Install Python 3.10.10
```bash
brew install python@3.10.10
```

2. Create a Python virtual environment:
```bash
python -m venv env
```

1. Activate the virtual environment:
```bash
source env/bin/activate
```
1. Install the required packages:
```bash
pip install -r requirements.txt
```
1. Run Migrations
```bash
python manage.py migrate
```
1. Run server
```bash
python manage.py runserver
```