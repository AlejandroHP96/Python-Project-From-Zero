# **Python Project from zero**

## **Project structure**

	-  main.py: is the main file of project, this file is used for execute the program

	-  setup.py: this script is the center of all activity in building, distributing and installing modules.

	-  setup.cfg: configuration file for project.

	-  pyproject.toml: this file contains build suystem requirements and information, with are used by pip to build the package. 
		https://python-poetry.org/docs/pyproject/ 

	-  .gitignore: file contains all folder and files for git ignore.

	-  app/: folder for code of program
	
	-  assets/: folder for save documents, images, videos...
	
	-  config/: folder that contains project necesary configuration.

	-  config/requirements.txt: file contain all library used in project with each the version.

	-  logs/: folder contains all code information like errors for example.

	-  tests/: folder with all project tests.


## **Virtual Enviroment**

Enviroment separated from local system for install all libraries that need the project.

There are many libraries for create a virtual enviroment but I'm going to used 'venv'

### **VENV**
NOTE: add enviroment folder in .gitignore file


#### **Installation**

	-  pip install venv

#### **Create Virtual Enviroment**

	-  python3 -m venv name_venv

#### **Activate VENV**
	
	-  Windows: Scripts\bin\activate
	-  Linux: Source env/bin/activate

## **Linter**

Linter is plugging for check if code is good formating.

There are many linters, in this case I'm going to used pylint.

### **PyLint**

Configuration file is .pylintrc

#### **Installation**

	-  pip install pylint

## **Code Formatting**


