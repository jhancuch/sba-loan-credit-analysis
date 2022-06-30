setup:
	python -m venv ~/.sba
  
install:
	pip install -r requirements.txt
  
test:
	python -m pytest --nbval-lax eda/*.ipynb
  
all: setup install test