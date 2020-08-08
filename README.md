# EmployeeDetails
To display the employee details using custom management commands  in Django rest API framework

# Get the copy of  project using git clone command
$ git clone https://github.com/apafinal1/EmployeeDetails.git

# optional
# if u get any error will cloning use the below command :
# error: RPC failed; curl 56 OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054

$ git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080


$ cd EmployeeDetails

# To activate virtual envirnoment 
$ source venv/Scripts/activate

# change the path to project directory.
$ cd userdetails

# Installing the pre-required packages using pip
$ pip install -r requirements.txt

# Migrating the tables in database
$ python manage.py migrate

# Create Super user account for login as admin
$ python manage.py createsuperuser

# Visit admin page to create a user 
$ python manage.py runserver

# Goto browser and add some data.
http://127.0.0.1:8000/admin/

# the data will be reflected in one more page using API's.
http://127.0.0.1:8000/final/

# Executing the output using custom management command
$ python manage.py user --total=1

# For verification we can use postman tool.
1. open postman tool and enter the url and select "GET" request
2. save and send the below url.
	http://127.0.0.1:8000/final/




