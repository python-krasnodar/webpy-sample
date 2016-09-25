# web.py Sample

This is an example of a simple web application using [web.py](http://webpy.org/).

## About web.py

> "Django lets you write web apps in Django. TurboGears lets you write web apps in TurboGears. Web.py lets you write web apps in Python."

—  Adam Atlas

[web.py](http://webpy.org/) is a web framework for [Python](https://www.python.org/) that is as simple as it is powerful. 
[web.py 0.38](https://github.com/webpy/webpy/releases/tag/webpy-0.38) is the latest released version of web.py.

At the moment, the stable version web.py works with python 2. 

## Sample application

As an example, I wrote a book reservation system.

It displays a catalog of books in the library. The visitor can:

* view the catalog
* search by title or author
* send a request to book a reservation

Administrator access interface where they can manage the directory, fill it with content and process requests for books.

### Up and running

```sh
$ sudo apt-get install libpq-dev python-dev virtualenv
$ virtualenv .venv
$ source .venv/bin/activate
$ cp .env.dist .env
$ docker-compose up -d
(.venv) $ pip install -r requirements.txt
(.venv) $ python code.py
```