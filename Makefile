setup:
	python3 -m venv ~/.sba
  
install:
	pip3 install -r requirements.txt
  
test:
	python3 -m pytest --nbval-lax eda/eda_sba_data.ipynb
	python3 -m pytest --nbval-lax eda/eda_sba_model.ipynb
  
all: setup install test
