# How to create a django application that counts visitors using redis database


* - Create your virtual enviromment: python3 -m venv my_venv_name or python -m venv my_venv_name
* - Activate your virtual enviroment: 
	* Windows: 
		- CMD:  my_venv_name\Scripts\activate.bat		
		- Powershell:  my_venv_name\Scripts\activate.ps1
	* Linux/Mac OS: source my_venv_name/bin/activate
* - Install packages: pip install django redis(redis is a driver that will allow connection to db )
* - Create le your project: django-admin startproject blog
* - Move to your project: cd blog  
* - Create your application: python manage.py startapp post


