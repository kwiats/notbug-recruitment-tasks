# notbug recruitment tasks

# Frontend

### Prerequisites

Install `Node.js` which includes Node Package Manager, then install Angular CLI with `npm install -g @angular/cli`.

Also, you need to install rxjs and axios modules with `npm install axios` and `npm install rxjs`.

## Recruitment tasks:

```
1.1. Angular app – create application which allow user to store in
localstorage cars. To each car user are allowed to store information
about services (parts and costs) and display them in the list in car details
view.
```

#### Readme for 1.1

Firstly go to, `cd Frontend/1.1/app`, then run `ng serve` for a dev server. Navigate to `http://localhost:4200/`.

```
1.2. RxJs – create a script which will make avg of age persons which
living in Poland from data bellow.
```

#### Readme for 1.2

Firstly go to `cd Frontend/1.1/app`, then run `node script.js` and look at terminal to see results.

```
1.3. Angular app – create app to display list of pokemons and details view for each
of them. Data need to be fetched from https://pokeapi.co using HTTP requests.
```

#### Readme for 1.3

Firstly go with `cd Frontend/1.3/app`, then run `ng serve` for a dev server. Navigate to `http://localhost:4200/`.

# Backend

## Prerequisites

Go with `cd Backend`, then create virtual enviroment with `virtualenv .venv`. Install all dependencies with `pip install -r requirements.txt`

## Recruitment tasks:

```
2.1. Create Flask app which will be REST API app for To-Do list, which allow user to
create task, list, update and delete them. Data could be “mocked”, extra points for
using SQLite or PostgreSQL. URLS need to be in REST API convention.
```

#### Readme for 2.1

Firstly go with `cd Backend/2.1/` then run `python3 app.py`. You can test it by using `postman` with prepared json `nobug.postman_collection.json`.

```
2.2. Create Django App – blog app with registration and possibility to create new
entries and update them by authors after login in. App should also allow user to
create a new accounts.

```

#### Readme for 2.2

Firstly go with `cd Backend/2.2/`, then run `python manage.py runserver` for a dev server. Navigate to `http://localhost:8000/`.

```
2.4. Python:
• Create good script to create new list, which only contains users from Poland. Try to do it
with List Comprehension.
users = [{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name":
"Yeti"}]
• Display sum of first ten elements starting from element 5:
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
• Fill list with powers of 2, n [1..20]
```

#### Readme for 2.4

Firstly go with `cd Backend/2.4/`, then run `python3 task_python.py` and look at terminal for results.
