setup:
	python3 -m venv ~/.sample
  
install:
	pip3 install -r requirements.txt
  
test:
	python3 -m pytest --nbval-lax sample_requests.py
  
all: setup install test
