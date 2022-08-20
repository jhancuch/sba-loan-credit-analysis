setup:
	python3 -m venv ~/.sba
  
install:
	pip3 install -r requirements.txt
  
test_eda:
	python3 -m pytest --nbval-lax eda/eda_sba_data.ipynb
	python3 -m pytest --nbval-lax eda/eda_sba_model.ipynb

test_sample:
	python3 -m pylint sample/sample_requests.py
	python3 -m pylint sample/func.py
	
test_app:
	python3 -m pylint app/app/main.py
  
all: setup install test_eda test_sample test_app
