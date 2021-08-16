# Apache2-80-and-mod_wsgi-on-Ubuntu---Django


link - https://studygyaan.com/django/how-to-setup-django-applications-with-apache-and-mod-wsgi-on-ubuntu

# We are assuming that you are using Django with Python3. Following are the commands-
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

'''
The above command will install Apache2 the Web Server, mod_wsgi for communicating and interfacing with our 
Django app and pip3, the python package manager for downloading python related tools.
Note – Make sure you have installed above library successfully otherwise you will get invalid command 
‘wsgidaemonprocess‘ error in terminal. It will fix – invalid command ‘wsgidaemonprocess‘, perhaps misspelled 
or defined by a module not included in the server configuration
'''

# Lets Quit the server with CONTROL-C and temporarily get out of the virtual environment by typing
deactivate

# Deploying Django Application on Apache Server

'''
Now that your project is working perfectly fine, its time to deploy Django Application on the Web server. 
The client connections that it receives are going to be translated into the WSGI format that the Django application 
expects the mistreatment of the mod_wsgi module.
Let’s create a virtual host file for our project. With your text editor create a .conf file 
in apache2 /etc/apache2/sites-available/ directory.
'''

sudo nano /etc/apache2/sites-available/djangoproject.conf

# Add the following text to djangoproject.conf file:

<VirtualHost *:80>
	ServerAdmin admin@djangoproject.localhost
	ServerName djangoproject.localhost
	ServerAlias www.djangoproject.localhost
	DocumentRoot /home/user/django_project
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	Alias /static /home/user/django_project/static
	<Directory /home/user/django_project/static>
		Require all granted
	</Directory>

	Alias /static /home/user/django_project/media
	<Directory /home/user/django_project/media>
		Require all granted
	</Directory>

	<Directory /home/user/django_project/my_django_project>
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory>

	WSGIDaemonProcess django_project python-path=/home/user/django_project python-home=/home/user/django_project/env
	WSGIProcessGroup django_project
	WSGIScriptAlias / /home/user/django_project/my_django_project/wsgi.py
</VirtualHost>


# When you are finished making the below changes, save and close the file.
ctr X - Y and hit enter

'''
Tip: If you are getting this error – Invalid command ‘WSGIDaemonProcess’, perhaps misspelled or defined by a module not included in the server configuration

Then the explanation for obtaining the error may well be that you simply haven’t run this command
'''

sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

# Enable the Virtual Host File for Django Project

# Once we created djangoproject.conf the file we need the enable that virtual host file by typing

cd /etc/apache2/sites-available
sudo a2ensite djangoproject.conf

# The above command will give output something like this –

'''
Enabling site djangoproject.
To activate the new configuration, you need to run:
service apache2 reload
'''

# Wrapping Up Some Permissions Issues

sudo ufw allow 'Apache Full'

sudo chmod 664 /home/user/django_project/db.sqlite3
'''
path where database is there eg /home/ubuntu/project/db.sqlite3
'''
sudo chown :www-data /home/user/django_project/db.sqlite3

sudo chown :www-data /home/user/django_project

# Check your Apache files to make sure you did not make any syntax errors:

sudo apache2ctl configtest

'''
It will output – Syntax OK which means no error and everything is working.
'''

# Back to our Project Setup

# Add ALLOWED_HOSTS = ['djangoproject.localhost']

'''
Now we need to run the run server by typing runserver command
'''

python3 manage.py runserver

'''
Quit the server with CONTROL-C. This will not stop the server from running. When you get out, you need to restart Apache to make these changes take effect:
'''

sudo service apache2 restart

tail -f /var/log/apache2/error.log
