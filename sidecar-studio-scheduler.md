command line commands used to create django project

<mkdir studioScheduler

<source env_studioscheduler/bin/activate

<which python

<pip install --upgrade pip

<pip3 install django

<python -m django --version

> 3.0.2

<django-admin startproject studioscheduler

<python manage.py runserver

<python manage.py startapp studioapp

downloaded and installed postgresql to use instead of sqlite ||sqlite3
used socratica youtube tutorial => https://youtu.be/fZQI7nBu32M
postgresql listening on port = 5432
installed postgresql and pgAdmin4
created dbStudioapp

<pip install psycopg2
installed
error caused

<brew upgrade postgresql

<brew reinstall openssl>

>

    ld: library not found for -lssl
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    error: command 'gcc' failed with exit status 1

<pipenv install psycopg2==2.7.7

> ERROR: ERROR: Package installation failed...

<pg_config --version

> PostgreSQL 12.1
> (env_studioscheduler)

<pip install python-dev-tools
success

pip install --upgrade pip

> Collecting pip
> Using cached https://files.pythonhosted.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl
> ERROR: python-dev-tools 2019.12.4 has requirement pip==19.3.1, but you'll have pip 20.0.2 which is incompatible.
> Installing collected packages: pip
> Found existing installation: pip 19.3.1

    Uninstalling pip-19.3.1:
      Successfully uninstalled pip-19.3.1

Successfully installed pip-20.0.2

# the other options are mysql and 1 other

# Django has official support for sqlite, mysql, postgresql and oracle

<which pg_config

>

    /usr/local/bin/pg_config
    (env_studioscheduler)

<pg_config --version

>

    PostgreSQL 12.1

<pip install --upgrade wheel

> Requirement already up-to-date: wheel in ./env_studioscheduler/lib/python3.8/site-packages (0.33.6)

pip install --upgrade setuptools

>

    Downloading setuptools-45.1.0-py3-none-any.whl (583 kB)
     |████████████████████████████████| 583 kB 2.7 MB/s

ERROR: python-dev-tools 2019.12.4 has requirement pip==19.3.1, but you'll have pip 20.0.2 which is incompatible.
Installing collected packages: setuptools
Attempting uninstall: setuptools
Found existing installation: setuptools 41.2.0
Uninstalling setuptools-41.2.0:
Successfully uninstalled setuptools-41.2.0
Successfully installed setuptools-45.1.0

<env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
#from https://stackoverflow.com/questions/26288042/error-installing-psycopg2-library-not-found-for-lssl

>

    Collecting psycopg2

Using cached psycopg2-2.8.4.tar.gz (377 kB)
Building wheels for collected packages: psycopg2
Building wheel for psycopg2 (setup.py) ... done
Created wheel for psycopg2: filename=psycopg2-2.8.4-cp38-cp38-macosx_10_9_x86_64.whl size=136241 sha256=83912fb29bc817bb903cec05f15de3f9406dbc0481b9ee5aa2e39810a60f94b6
Stored in directory: /Users/LHD/Library/Caches/pip/wheels/ac/07/3e/87adc95a2be1ee727bc54f487ce874bd6765ec9f206effb0df
Successfully built psycopg2
Installing collected packages: psycopg2
Successfully installed psycopg2-2.8.4

<python manage.py migrate
#success

    'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbstudioapp',
        'USER': 'postgres',
        'PASSWORD': 'notshown',
        'HOST': 'localhost',
        'PORT': '5432',

#in settigns file: updated TIME_ZONE from UTC to
#TIME_ZONE = 'EST'
