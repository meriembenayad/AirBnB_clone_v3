## . AirBnB clone - RESTful API
### Resources

**Read or watch**:

- **REST API** [concept page](concept_restapi.md.md)
- [Learn REST: A RESTful Tutorial](https://www.restapitutorial.com/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Flask cheatsheet](https://drive.google.com/file/d/1ELsns6ECZzy8MkTnzTf2RlXhFtCUfVCp/view?usp=drive_link)
- [What are Flask Blueprints, exactly?](https://stackoverflow.com/questions/24420857/what-are-flask-blueprints-exactly)
- [Flask](https://palletsprojects.com/p/flask/)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
- [Flask tests](https://flask.palletsprojects.com/en/1.1.x/testing/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

### Learning Objectives

#### General

### General

- What REST means?
- What API means?
- What CORS means?
- What is an API?
- What is a REST API?
- What are other type of APIs?
- Which is the HTTP method to retrieve resource(s)?
- Which is the HTTP method to create a resource?
- Which is the HTTP method to update resource?
- Which is the HTTP method to delete resource?
- How to request REST API?

### Requirements

#### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests

- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project: ex: for `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

## More Info

![Flask](flask.jpeg)

#### Install Flask

```shell
$ pip3 install Flask
```

### Tasks

<details>
<summary>0. Restart from scratch!</summary>

Absolutely not! We've progressed too much in the project to consider starting over.

However, let's once again embark on creating a new codebase.

For this endeavor, you'll need to fork this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2.git "codebase"):

- Change the repository name to `AirBnB_clone_v3`
- Modify the `README.md`:
    - Include your name as a project contributor
    - Incorporate details about your fresh contributions
    - Enhance it further!
- If you hold ownership of this codebase, initiate a new repository named `AirBnB_clone_v3` and transfer all files from `AirBnB_clone_v2`

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
</details>

<details>
<summary>1. Never fail!</summary>

From the outset, we've been utilizing the `unittest` module. But are you aware of the significance of `unittests`? They're crucial because whenever you introduce a new feature or refactor a piece of code, you want to ensure nothing else is disrupted.

At Holberton, we have an extensive suite of tests, all of which pass! Specifically for the Intranet, we have:

- `5,213` assertions _(as of 08/20/2018)_
- `13,061` assertions _(as of 01/25/2021)_

Your project **must** adhere to the following requirements:

- All existing tests must pass (don't remove them…)
- Add as many new tests as possible (tests are compulsory for some tasks)

```shell
guillaume@ubuntu:~/AirBnB_v3$ python3 -m unittest discover tests 2>&1 | tail -1
OK
guillaume@ubuntu:~/AirBnB_v3$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v3$ 
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
</details>

<details>
<summary>2. Improve storage</summary>

Revise `DBStorage` and `FileStorage` by incorporating two new methods. **Ensure all modifications are made in the `storage_get_count` branch**:

A method to fetch a single object:

- Prototype: `def get(self, cls, id):`
    - `cls`: class
    - `id`: string that represents the object ID
- This returns the object corresponding to the class and its ID, or `None` if it doesn't exist.

A method to tally the quantity of objects in storage:

- Prototype: `def count(self, cls=None):`
    - `cls`: class (optional)
- This returns the count of objects in storage that match the given class. If no class is provided, it returns the count of all objects in storage.

Remember to add new tests for these two methods on each storage engine.

```shell
guillaume@ubuntu:~/AirBnB_v3$ cat test_get_count.py
#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py 
All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ ./test_get_count.py 
All objects: 19
State objects: 5
First state: [State] (af14c85b-172f-4474-8a30-d4ec21f9795e) {'updated_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378824), 'name': 'Arizona', 'id': 'af14c85b-172f-4474-8a30-d4ec21f9795e', 'created_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378763)}
guillaume@ubuntu:~/AirBnB_v3$ 
```
For this task, you **must** make a pull request on GitHub.com, and ask at least one of your peer to review and merge it.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `models/engine/db_storage.py, models/engine/file_storage.py, tests/test_models/test_engine/test_db_storage.py, tests/test_models/test_engine/test_file_storage.py`
</details>

<details>
<summary>3. Status of your API</summary>

It’s the moment to initiate your API!

The initial endpoint (route) should be designed to report the status of your API. This is a common practice in API development to ensure that the API is functioning correctly. Good luck with your API development! 

```shell
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```
_In another terminal:_
```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
guillaume@ubuntu:~/AirBnB_v3$ 
```
Isn't it magical? (Remember, it's a JSON, so the structure is what matters, not the aesthetics)

Let's get started:

- At the project's root, create a folder named `api` and include an empty file named `__init__.py`.
- Inside `api`, create another folder named `v1`:
    - Add an empty file named `__init__.py`.
    - Create a file named `app.py`:
        - Define a variable `app` as an instance of `Flask`.
        - Import `storage` from `models`.
        - Import `app_views` from `api.v1.views`.
        - Register the blueprint `app_views` with your Flask instance `app`.
        - Declare a method to handle `@app.teardown_appcontext` that calls `storage.close()`.
        - Within `if __name__ == "__main__":`, run your Flask server (variable `app`) with:
            - host = environment variable `HBNB_API_HOST` or `0.0.0.0` if not defined.
            - port = environment variable `HBNB_API_PORT` or `5000` if not defined.
            - `threaded=True`.
- Inside `v1`, create a folder named `views`:
    - Add a file named `__init__.py`:
        - Import `Blueprint` from `flask` [doc](https://flask.palletsprojects.com/en/1.1.x/blueprints/).
        - Define a variable `app_views` as an instance of `Blueprint` (url prefix must be `/api/v1`).
        - Perform a wildcard import of everything in the package `api.v1.views.index` => PEP8 will complain about it, but don't worry, it's normal and this file (`v1/views/__init__.py`) won't be checked.
    - Create a file named `index.py`.
        - Import `app_views` from `api.v1.views`.
        - On the object `app_views`, create a route `/status` that returns a JSON: `"status": "OK"` (see example).

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/__init__.py, api/v1/__init__.py, api/v1/views/__init__.py, api/v1/views/index.py, api/v1/app.py`
</details>

<details>
<summary>4. Some stats?</summary>

Set up an endpoint that fetches the count of objects for each type:

- The file to modify is `api/v1/views/index.py`.
- The route to use is `/api/v1/stats`.
- You are required to utilize the recently incorporated `count()` function from `storage`.

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/stats
{
  "amenities": 47, 
  "cities": 36, 
  "places": 154, 
  "reviews": 718, 
  "states": 27, 
  "users": 31
}
guillaume@ubuntu:~/AirBnB_v3$ 
```
_(No need to have a pretty rendered output, it’s a JSON, only the structure is important)_
***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/index.py`
</details>

<details>
<summary>5. Not found</summary>

Designers exhibit immense creativity when tasked with designing a "404 page" or a "Not found" page. [Here are 34 examples of brilliantly designed 404 error pages](https://www.creativebloq.com/web-design/best-404-pages-812505).

However, today's task is unique because you'll be using JSON instead of HTML and CSS!

In the `api/v1/app.py` file, you need to establish a handler for `404` errors that delivers a response with a `404` status code in JSON format. The content should be: `"error": "Not found"`.

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/nop HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Fri, 14 Apr 2017 23:43:24 GMT
< 
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/app.py`
</details>

<details>
<summary>6. State</summary>

Set up a new view for `State` objects that manages all standard RESTFul API operations:

- In the `api/v1/views/states.py` file.
- You should use `to_dict()` to convert an object into a valid JSON.
- Update `api/v1/views/__init__.py` to import this new file.

Fetch the list of all `State` objects: `GET /api/v1/states`.

Fetch a `State` object: `GET /api/v1/states/<state_id>`.

- If the `state_id` is not associated with any `State` object, trigger a `404` error.

Remove a `State` object: `DELETE /api/v1/states/<state_id>`.

- If the `state_id` is not associated with any `State` object, trigger a `404` error.
- Return an empty dictionary with the status code `200`.

Create a `State`: `POST /api/v1/states`.

- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- If the dictionary doesn’t contain the `name` key, trigger a `400` error with the message `Missing name`.
- Return the new `State` with the status code `201`.

Update a `State` object: `PUT /api/v1/states/<state_id>`.

- If the `state_id` is not associated with any `State` object, trigger a `404` error.
- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- Update the `State` object with all key-value pairs of the dictionary.
- Ignore keys: `id`, `created_at` and `updated_at`.
- Return the `State` object with the status code `200`.

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/
[
  {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
  }, 
  {
    "__class__": "State", 
    "created_at": "2017-04-14T16:21:42", 
    "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269", 
    "name": "Arizona", 
    "updated_at": "2017-04-14T16:21:42"
  }, 
...
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
 {
  "__class__": "State", 
  "created_at": "2017-04-14T00:00:02", 
  "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
  "name": "Louisiana", 
  "updated_at": "2017-04-14T00:00:02"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/ HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 22
> 
* upload completely sent off: 22 out of 22 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 195
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sat, 15 Apr 2017 01:30:27 GMT
< 
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:27.557877", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California", 
  "updated_at": "2017-04-15T01:30:27.558081"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X PUT http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:28", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California is so cool", 
  "updated_at": "2017-04-15T01:51:08.044996"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "__class__": "State", 
  "created_at": "2017-04-15T01:30:28", 
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6", 
  "name": "California is so cool", 
  "updated_at": "2017-04-15T01:51:08"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X DELETE http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/states.py, api/v1/views/__init__.py`
</details>

<details>
<summary>7. City</summary>

Just like `State`, set up a new view for `City` objects that manages all standard RESTFul API operations:

- In the `api/v1/views/cities.py` file.
- You should use `to_dict()` to convert an object into a valid JSON.
- Update `api/v1/views/__init__.py` to import this new file.

Fetch the list of all `City` objects of a `State`: `GET /api/v1/states/<state_id>/cities`.

- If the `state_id` is not associated with any `State` object, trigger a `404` error.

Fetch a `City` object: `GET /api/v1/cities/<city_id>`.

- If the `city_id` is not associated with any `City` object, trigger a `404` error.

Remove a `City` object: `DELETE /api/v1/cities/<city_id>`.

- If the `city_id` is not associated with any `City` object, trigger a `404` error.
- Return an empty dictionary with the status code `200`.

Create a `City`: `POST /api/v1/states/<state_id>/cities`.

- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the `state_id` is not associated with any `State` object, trigger a `404` error.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- If the dictionary doesn’t contain the `name` key, trigger a `400` error with the message `Missing name`.
- Return the new `City` with the status code `201`.

Update a `City` object: `PUT /api/v1/cities/<city_id>`.

- If the `city_id` is not associated with any `City` object, trigger a `404` error.
- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- Update the `City` object with all key-value pairs of the dictionary.
- Ignore keys: `id`, `state_id`, `created_at` and `updated_at`.
- Return the `City` object with the status code `200`.

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/not_an_id/cities/
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities
[
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
    "name": "New Orleans", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }, 
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "45903748-fa39-4cd0-8a0b-c62bfe471702", 
    "name": "Lafayette", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }, 
  {
    "__class__": "City", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "e4e40a6e-59ff-4b4f-ab72-d6d100201588", 
    "name": "Baton rouge", 
    "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
    "updated_at": "2017-03-25T02:17:06"
  }
]
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683
{
  "__class__": "City", 
  "created_at": "2017-03-25T02:17:06", 
  "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
  "name": "New Orleans", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-03-25T02:17:06"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities -H "Content-Type: application/json" -d '{"name": "Alexandria"}' -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/ HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 22
> 
* upload completely sent off: 22 out of 22 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 249
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 16 Apr 2017 03:14:05 GMT
< 
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:05.655490", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Alexandria", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:14:05.655748"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X PUT http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af -H "Content-Type: application/json" -d '{"name": "Bossier City"}'
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:06", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Bossier City", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:15:12.895894"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{
  "__class__": "City", 
  "created_at": "2017-04-16T03:14:06", 
  "id": "b75ae104-a8a3-475e-bf74-ab0a066ca2af", 
  "name": "Bossier City", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-04-16T03:15:13"
}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X DELETE http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{}
guillaume@ubuntu:~/AirBnB_v3$ 
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/b75ae104-a8a3-475e-bf74-ab0a066ca2af
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/cities.py, api/v1/views/__init__.py`
</details>

<details>
<summary>8. Amenity</summary>

Just like `State`, set up a new view for `Amenity` objects that manages all standard RESTFul API operations:

- In the `api/v1/views/amenities.py` file.
- You should use `to_dict()` to convert an object into a valid JSON.
- Update `api/v1/views/__init__.py` to import this new file.

Fetch the list of all `Amenity` objects: `GET /api/v1/amenities`.

Fetch an `Amenity` object: `GET /api/v1/amenities/<amenity_id>`.

- If the `amenity_id` is not associated with any `Amenity` object, trigger a `404` error.

Remove an `Amenity` object: `DELETE /api/v1/amenities/<amenity_id>`.

- If the `amenity_id` is not associated with any `Amenity` object, trigger a `404` error.
- Return an empty dictionary with the status code `200`.

Create an `Amenity`: `POST /api/v1/amenities`.

- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- If the dictionary doesn’t contain the `name` key, trigger a `400` error with the message `Missing name`.
- Return the new `Amenity` with the status code `201`.

Update an `Amenity` object: `PUT /api/v1/amenities/<amenity_id>`.

- If the `amenity_id` is not associated with any `Amenity` object, trigger a `404` error.
- You should use `request.get_json` from Flask to convert the HTTP body request into a dictionary.
- If the HTTP body request is not a valid JSON, trigger a `400` error with the message `Not a JSON`.
- Update the `Amenity` object with all key-value pairs of the dictionary.
- Ignore keys: `id`, `created_at` and `updated_at`.
- Return the `Amenity` object with the status code `200`.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/amenities.py, api/v1/views/__init__.py`
</details>

<details>
<summary>9. User</summary>

Set up a new view for `User` objects that manages all standard RESTFul API operations:

- In the `api/v1/views/users.py` file.
- You should use `to_dict()` to convert an object into a valid JSON.
- Update `api/v1/views/__init__.py` to import this new file.

Fetch the list of all `User` objects: `GET /api/v1/users`.

Fetch a `User` object: `GET /api/v1/users/<user_id>`.

- If the `user_id` is not associated with any `User` object, trigger a `404` error.

Remove a `User` object: `DELETE /api/v1/users/<user_id>`.

- If the `user_id` is not associated with any `User` object, trigger a `404` error.
- Return an empty dictionary with the status code `200`.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/users.py, api/v1/views/__init__.py`
</details>

<details>
<summary>10. Place</summary>

Construct a new view for `Place` objects that accommodates all standard RESTFul API operations:

- This should be done in the `api/v1/views/places.py` file.
- Utilize `to_dict()` to convert an object into valid JSON.
- Update `api/v1/views/__init__.py` to incorporate this new file.

To fetch the list of all `Place` objects of a `City`, use: `GET /api/v1/cities/<city_id>/places`
- If the `city_id` doesn't correspond to any `City` object, return a `404` error.

To fetch a `Place` object, use: `GET /api/v1/places/<place_id>`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.

To delete a `Place` object, use: `DELETE /api/v1/places/<place_id>`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.
- The response should be an empty dictionary with the status code `200`.

To create a `Place`, use: `POST /api/v1/cities/<city_id>/places`
- Use `request.get_json` from Flask to convert the HTTP request into a dictionary.
- If the `city_id` doesn't correspond to any `City` object, return a `404` error.
- If the HTTP request body isn't valid JSON, return a `400` error with the message `Not a JSON`.
- If the dictionary doesn't contain the key `user_id`, return a `400` error with the message `Missing user_id`.
- If the `user_id` doesn't correspond to any `User` object, return a `404` error.
- If the dictionary doesn't contain the key `name`, return a `400` error with the message `Missing name`.
- The response should be the new `Place` with the status code `201`.

To update a `Place` object, use: `PUT /api/v1/places/<place_id>`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.
- Use `request.get_json` from Flask to convert the HTTP request into a dictionary.
- If the HTTP request body isn't valid JSON, return a `400` error with the message `Not a JSON`.
- Update the `Place` object with all key-value pairs of the dictionary.
- Ignore the keys: `id`, `user_id`, `city_id`, `created_at`, and `updated_at`.
- The response should be the `Place` object with the status code `200`.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/places.py, api/v1/views/__init__.py`
</details>

<details>
<summary>11. Reviews</summary>

Develop a new view for the `Review` object that manages all standard RESTFul API operations:

- This should be done in the `api/v1/views/places_reviews.py` file.
- Use `to_dict()` to convert an object into valid JSON.
- Update `api/v1/views/__init__.py` to include this new file.

To fetch the list of all `Review` objects of a `Place`, use: `GET /api/v1/places/<place_id>/reviews`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.

To fetch a `Review` object, use: `GET /api/v1/reviews/<review_id>`
- If the `review_id` doesn't correspond to any `Review` object, return a `404` error.

To delete a `Review` object, use: `DELETE /api/v1/reviews/<review_id>`
- If the `review_id` doesn't correspond to any `Review` object, return a `404` error.
- The response should be an empty dictionary with the status code `200`.

To create a `Review`, use: `POST /api/v1/places/<place_id>/reviews`
- Use `request.get_json` from Flask to convert the HTTP request into a dictionary.
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.
- If the HTTP request body isn't valid JSON, return a `400` error with the message `Not a JSON`.
- If the dictionary doesn't contain the key `user_id`, return a `400` error with the message `Missing user_id`.
- If the `user_id` doesn't correspond to any `User` object, return a `404` error.
- If the dictionary doesn't contain the key `text`, return a `400` error with the message `Missing text`.
- The response should be the new `Review` with the status code `201`.

To update a `Review` object, use: `PUT /api/v1/reviews/<review_id>`
- If the `review_id` doesn't correspond to any `Review` object, return a `404` error.
- Use `request.get_json` from Flask to convert the HTTP request into a dictionary.
- If the HTTP request body isn't valid JSON, return a `400` error with the message `Not a JSON`.
- Update the `Review` object with all key-value pairs of the dictionary.
- Ignore the keys: `id`, `user_id`, `place_id`, `created_at`, and `updated_at`.
- The response should be the `Review` object with the status code `200`.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/places_reviews.py, api/v1/views/__init__.py`
</details>

<details>
<summary>12. HTTP access control (CORS)</summary>

A cross-origin HTTP request occurs when a resource requests another resource from a different domain or port than its own.

You can read the complete definition [here](https://intranet.alxswe.com/rltoken/D55IFF8lgZDLPyIX6b6C5A "here").

Why is this important?

This is crucial because you will soon enable a web client to make requests to your API. If your API doesn't have the correct CORS setup, your web client will be unable to access your data.

Setting up CORS with Flask is straightforward, you will use the `CORS` class from the `flask_cors` module.

To install it, use the following command: `$ pip3 install flask_cors`

You need to update `api/v1/app.py` to create a `CORS` instance that allows: `/*` for `0.0.0.0`

You will make further updates when you deploy your API to production.

After these changes, you should be able to see this HTTP Response Header: `< Access-Control-Allow-Origin: 0.0.0.0`

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683 -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/1da255c0-f023-4779-8134-2b1b40f87683 HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Access-Control-Allow-Origin: 0.0.0.0
< Content-Length: 236
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 16 Apr 2017 04:20:13 GMT
< 
{
  "__class__": "City", 
  "created_at": "2017-03-25T02:17:06", 
  "id": "1da255c0-f023-4779-8134-2b1b40f87683", 
  "name": "New Orleans", 
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", 
  "updated_at": "2017-03-25T02:17:06"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$ 
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/app.py`
</details>

<details>
<summary>13. Place - Amenity</summary>

Develop a new view for the association between `Place` objects and `Amenity` objects that manages all standard RESTFul API operations:

- This should be done in the `api/v1/views/places_amenities.py` file.
- Use `to_dict()` to convert an object into valid JSON.
- Update `api/v1/views/__init__.py` to include this new file.
- Depending on the storage:
    - `DBStorage`: list, create, and delete `Amenity` objects from the `amenities` relationship.
    - `FileStorage`: list, add, and remove `Amenity` ID in the `amenity_ids` list of a `Place` object.

To fetch the list of all `Amenity` objects of a `Place`, use: `GET /api/v1/places/<place_id>/amenities`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.

To delete an `Amenity` object from a `Place`, use: `DELETE /api/v1/places/<place_id>/amenities/<amenity_id>`
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.
- If the `amenity_id` doesn't correspond to any `Amenity` object, return a `404` error.
- If the `Amenity` isn't linked to the `Place` before the request, return a `404` error.
- The response should be an empty dictionary with the status code `200`.

To link an `Amenity` object to a `Place`, use: `POST /api/v1/places/<place_id>/amenities/<amenity_id>`
- No HTTP body is needed.
- If the `place_id` doesn't correspond to any `Place` object, return a `404` error.
- If the `amenity_id` doesn't correspond to any `Amenity` object, return a `404` error.
- If the `Amenity` is already linked to the `Place`, return the `Amenity` with the status code `200`.
- The response should be the `Amenity` with the status code `201`.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/places_amenities.py, api/v1/views/__init__.py`
</details>

<details>
<summary>14. Security improvements!</summary>

At present, the `User` object is configured to store the user password in plaintext, which is highly insecure!

To rectify this, enhance the `User` object as follows:

- Modify the `to_dict()` method of `BaseModel` to exclude the `password` key, **unless it's being used by `FileStorage` for disk data storage**. Hint: Use default parameters.
- Whenever a new `User` object is instantiated or a password is updated, the password should be hashed to an [MD5](https://docs.python.org/3.4/library/hashlib.html) value.
- In the `DBStorage` database, the stored password should now be an MD5 hash value.
- In the `FileStorage` file, the stored password should now be an MD5 hash value.

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `models/base_model.py, models/user.py`
</details>

<details>
<summary>15. Search</summary>

Currently, the only method to list `Place` objects is through `GET /api/v1/cities/<city_id>/places`.

While this is good, it's not sufficient…

You need to modify `api/v1/views/places.py` to include a new endpoint: `POST /api/v1/places_search`. This will fetch all `Place` objects based on the JSON content in the request body.

The JSON can optionally include three keys:

- `states`: a list of `State` IDs
- `cities`: a list of `City` IDs
- `amenities`: a list of `Amenity` IDs

The rules for the search are as follows:

- If the HTTP request body is not valid JSON, return a `400` error with the message `Not a JSON`.
- If the JSON body is empty or all key lists are empty, fetch all `Place` objects.
- If the `states` list is not empty, the results should include all `Place` objects for each listed `State` ID.
- If the `cities` list is not empty, the results should include all `Place` objects for each listed `City` ID.
- The `states` and `cities` keys are inclusive. The search results should include all `Place` objects in storage related to each `City` in every `State` listed in `states`, plus every `City` listed individually in `cities`, _unless_ that `City` was already included by `states`.
    - For example:
        - State A has 2 cities A1 and A2
        - State B has 3 cities B1, B2 and B3
        - A1 has 1 place
        - A2 has 2 places
        - B1 has 3 places
        - B2 has 4 places
        - B3 has 5 places
    - If the search is for states = State A and cities = B2, the result will include all 4 places from city B2 and the place from city A1 and the 2 places from city A2 (because they are part of State A). This totals to 7 places.
- If the `amenities` list is not empty, limit the search results to only `Place` objects having all listed `Amenity` IDs.
- The `amenities` key is exclusive, acting as a filter on the results generated by `states` and `cities`, or on all `Place` objects if `states` and `cities` are both empty or missing.
- Results will only include `Place` objects having all listed `amenities`. If a `Place` doesn’t have even one of these `amenities`, it won’t be retrieved.

```shell
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/places_search -H "Content-Type: application/json" -d '{"states": ["2b9a4627-8a9e-4f32-a752-9a84fa7f4efd", "459e021a-e794-447d-9dd2-e03b7963f7d2"], "cities": ["5976f0e7-5c5f-4949-aae0-90d68fd239c0"]}'
[
  {
    "__class__": "Place", 
    "created_at": "2017-03-25T02:17:06", 
    "id": "dacec983-cec4-4f68-bd7f-af9068a305f5", 
    "name": "The Lynn House", 
    "city_id": "5976f0e7-5c5f-4949-aae0-90d68fd239c0", 
    "user_id": "3ea61b06-e22a-459b-bb96-d900fb8f843a", 
    "description": "Our place is 2 blocks from Vista Park (Farmer's Market), Historic Warren Ballpark, and about 2 miles from Old Bisbee where there is shopping, dining, and site seeing. We offer continental breakfast. You get the quiet life with great mountain and garden views. This is a 100+ year old cozy home which has been on both the Garden and Home tours. You have access to whole house, except for 1 restricted area (She-Shack).  Hosts are on site in a casita in the back from 8pm until 7am when we are in town.<BR /><BR />Our home has two bedrooms, one king and one queen.  There are 2 bathrooms, 1  1950's soak tub with shower and 1 with shower only.  Guests have access to the living/dining room area, and the kitchen (except for use of stove/oven).  Each morning, coffee/tea, and muffins are ready for guests.  A small frig is available in the dining room with water/juice and an area for guest items.  1 parking space is directly across the street.", 
    "number_rooms": 2,
    "number_bathrooms": 2,
    "max_guest": 4,
    "price_by_night": 82, 
    "latitude": 31.4141, 
    "longitude": -109.879, 
    "updated_at": "2017-03-25T02:17:06"
  },
    {
    "__class__": "Place", 
    "created_at": "2017-03-25T12:17:06", 
    "id": "85f979ad-a345-4190-9d1b-719bb3c642ba", 
    "name": "Little blue House in New Orleans", 
    "city_id": "1da255c0-f023-4779-8134-2b1b40f87683", 
    "user_id": "44b3ab44-4798-4a3a-9f72-ee1eeace4b33", 
    "description": "Nice place closed to Bourbon street.", 
    "number_rooms": 1,
    "number_bathrooms": 1,
    "max_guest": 3,
    "price_by_night": 42, 
    "latitude": 29.951065, 
    "longitude": -90.071533, 
    "updated_at": "2017-03-25T02:17:06"
  },
...
guillaume@ubuntu:~/AirBnB_v3$
```

***
**Repo:**
- GitHub repository: `AirBnB_clone_v3`
- File: `api/v1/views/places.py`
</details>

***
### AUTHORS:
- Meriem Ben Ayad
- Thami Baladi
