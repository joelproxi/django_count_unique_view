# How to create a django application that counts visitors using redis database


1. Create your virtual enviromment: 
	sh`
	python3 -m venv my_venv_name or python -m venv my_venv_name
 	`
2 - Activate your virtual enviroment: 
	* Windows: 
		- CMD: 
			  sh`
			  my_venv_name\Scripts\activate.bat	
			  `
		- Powershell:  
			sh`
			  my_venv_name\Scripts\activate.ps1	
			`
	* Linux/Mac OS: source my_venv_name/bin/activate
3 - Install packages: pip install django redis(redis is a driver that will allow connection to db )
4 - Create le your project: django-admin startproject blog
5 - Move to your project: cd blog  
6 - Create your application: python manage.py startapp post


