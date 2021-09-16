#!bin/bash

python -m virtualenv env

source env/Scripts/activate

pip install -q -r requirements.txt

python -m virtualenv env

source env/Scripts/activate

pip install -q -r requirements.txt

python main.py

deactivate