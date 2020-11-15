# Thistle Cockroach

Thistle Cockroach it's a another simple project developed in python but with small amount of magic. You can convert saddly 3D factors (X, Y, Z) from json to real svg graphic of your item in 2D !  

# QuickStart:
This quickstart will show you how to install dependencies and run application locally.

## System Dependencies:
    python3.x and pip3.x, python3-devel, python3-setuptools, build-essential, gcc
    port 8000:8000
    port 80:80
    
#### At first you need to clone this repository by:
    git clone 

#### Create virtualenv with your version of python3:
    virtualenv --python=python3.9 .venv
    source .venv/bin/activate
    
#### Install python3 dependencies:
    pip3 install -r requirements.txt
    
# You can run application as:

#### Development version:
    python3 manage.py runserver
    or
    uwsgi --ini uwsgi.ini
* this version runs at 8000 port

#### Docker version:
    docker build -t cockroach .
    docker run --network=host -d -ti cockroach
* this version run at 8000 port

#### With dockerized nginx:
in nginx/ direcory
   
    docker build -t cockroachnginx .
    docker run --network=host -d -ti cockroachnginx
* this version run with nginx at 80 port 

#### Docker-compose version:
    docker-compose up --build
* this version run with nginx at 80 port
* I'm highly recommend this version ( you know, one command, one small coffe and voila ! ).

#### For test you can make request like:
    curl -v -X POST -d <data from example input.json> -H "Content-Type: application/json" http://0.0.0.0:<running-port>/api/v1/cockroach/projection/
#### Response:
    image in svg

You should use Postman or curl, because in django rest framework UI response after POST request redirect automatically to /projection/ GET who doesn't exists.



## Run Unit tests
In main project directory, with activated virtualenv, you should execute:

    py.test --cov=. --flake8

## TODO
* Add logging to file
* Change initial values of drawing_place ( now it's harcoded 1000x1000 )
* Add database, to better manage generated images, serve images
* Use DRF dataclasses alongside DRF serializers. It will be better with swagger auto generation without model based serializers 


# Enjoy
