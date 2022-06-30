setup:
	python3 -m venv ~/.sba
  
install:
	pip3 install -r requirements.txt
  
test:
	python3 -m pytest --nbval eda/*.ipynb
  
all: setup install test