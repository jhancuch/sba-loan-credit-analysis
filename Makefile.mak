setup:
	python -m venv ./sba
  
install:
	pip install -r requirements.txt
  
test:
	python -m pytest --nbval-lax eda/*.ipynb
  
lint:
	pylint --disable=R,C myrepolib
  
lint2:
	pylint --disable=R,C tests
  
all: install lint lint2 test