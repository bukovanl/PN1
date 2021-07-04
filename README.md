# Get Weather
This exercise is about to show current weather at City defined by environment variable 'CITY_NAME'.

### How to use

To set these variable, run:

`$ source ./set_env`

To get current weather, run:

`$ python3 getweather.py`

### How it works

We get current weather from (https://openweathermap.org/current). To do that, we use **pyowm** python module.

## Ansible
We can use ansible to install **docker** on Ubuntu 16.04. It will enable **syslog** logging as well.
To install docker, run:

`ansible-playbook -i "localhost, " -c local --ask-become-pass site.yml`

## Dockerfile
You can get current weather using docker container as well. You can build docker image from Dockerfile.

To build docker image, run:

`$ docker build --rm -t "weather:dev" .`

To run docker image:

`$ docker run -e OPENWEATHER_API_KEY="87d0f24673cb20cbda37754b71a96e6d" -e CITY_NAME="Bratislava" weather:dev`

To check output:

`grep openweathermap /var/log/syslog`

