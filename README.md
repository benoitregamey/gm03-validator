# GM03 Validator
Web application and API to validate metadata XML against swiss GM03 profile

## Installation
### Set up local development environment (mac osx)
The app uses redis as message broker. So you need redis installed on your machine.
```
brew install redis
```
Clone the repo and install dependencies
```
git clone https://github.com/benoitregamey/gm03-validator.git

cd gm03-validator

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```
### Run the application
On mac os, you need to set the following environment variable fist.
```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES 
```
Then start the redis server
```
redis-server
```
In a new terminal, run celery (needs the celery python package, so make sure to activate the virtual environment)
```
celery -A app.celery_app worker --loglevel INFO
```
And finally run the application (within the virtual environment)
```
python app.py
```