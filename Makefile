setup:
	python3 -m venv ~/.sba
  
install:
	pip3 install -r requirements.txt
  
test_eda:
	python3 -m pytest --nbval-lax eda/eda_sba_data.ipynb
	
test_model:
	python3 -m pytest --nbval-lax eda/eda_sba_model.ipynb
	
test_app:
	python3 -m pylint engine/app/main.py
  
all: setup install test_eda test_model test_app
