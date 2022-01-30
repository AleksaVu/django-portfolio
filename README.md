# Blog and portfolio sample application

Simple django aplications form my github projects and future blog posts.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AleksaVu/django-portfolio.git
$ cd django-portfolio
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3.9 -m venv .venv
$ source .venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(.venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip3` has finished downloading the dependencies:
```sh
(env)$ cd myblog
(env)$ python3.9 manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


