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


Demo
---
![Alt text](preview_images/homescreen.png?raw=true "Homepage.")
![Alt text](preview_images/allprojects.png?raw=true "List of all projects.")
![Alt text](preview_images/projectdetail.png?raw=true "Single project details.")
![Alt text](preview_images/allblogposts.png?raw=true "List of all blog posts.")
![Alt text](preview_images/blogpost.png?raw=true "Single blog post.")
![Alt text](preview_images/commentsection.png?raw=true "Comment section")



