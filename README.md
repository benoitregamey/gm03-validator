# GM03 Validator
Web application and API to validate metadata XML against the swiss GM03 profile

## Installation
### Set up a local development environment (mac osx)
Clone the repo and install dependencies in a python virtual environment
```
git clone https://github.com/benoitregamey/gm03-validator.git

cd gm03-validator

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```
### Run the application
```
python app.py
```
Then visist http://localhost:5000

## Run with Docker
Clone the repo
```
git clone https://github.com/benoitregamey/gm03-validator.git

cd gm03-validator
```
Build and run the docker image
```
docker build -t gm03-validator .
docker run -d -p 5000:5000 --rm gm03-validator
```
Then visist http://localhost:5000