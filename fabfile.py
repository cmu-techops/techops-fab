from fabric.api import *

def run():
	local('python manage.py runserver')
