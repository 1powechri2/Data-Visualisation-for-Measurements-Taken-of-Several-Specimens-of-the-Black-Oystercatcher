# THIS IS A CURRENT WORK IN PROGRESS

## A Project that Integrates React and D3.js with Django for some client
## facing data visualization

The dataset is, Black Oystercatcher specimen measurements from UC Berkley Museum
of Vertebrate Zoology and California Academy of Sciences

Python version: 3.7.4

Django version: 2.2.4

Database: PostgreSQL

To run the project you must first create a database in postgresql named data_playground.

In the setting.py file change the DATABASES dictionary:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'data_playground',
        'USER': 'me',
        'PASSWORD': '*****',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

to match the information on your machine.

Now you can run the migrations and seed the dataset into the database. Navigate
into the project directory and from the terminal run these commands:
  $ python manage.py migrate
  $ python manage.py makemigrations data_playground
  $ python manage.py migrate
  $ python manage.py seed_data
