# TO DO List

## Features

- To do list frontend and backend

## Technologies Used

- Python Django with REST APIs
- Swagger for API Testing
- React js for frontend 

## Installation

# Backend Code
git clone [https://github.com/yourusername/your-repo.git](https://github.com/staz-tamjeed10/todo_list.git)https://github.com/staz-tamjeed10/todo_list.git

cd todo_list/backend/

virtualenv venv

## If Mac:
source ./venv/bin/activate
## If windows:
./venv/Scripts/activate
## create .env file
SECRET_KEY=django-insecure-y#oz(c=f153d_5b6+0w6hy-0wn-(9md32n*h%b59ro1@24wcw6

DEBUG=True

DATABASE_ENGINE=django.db.backends.sqlite3

DATABASE_NAME=db.sqlite3

## Then:
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser

### give username and password to superuser of your admin panel
## Open Admin Panel:
http://127.0.0.1:8000/admin/
## You can test APIs with swagger
http://127.0.0.1:8000/api/swagger/

# Open frontend:
## take this repo clone for Frontend:
git clone https://github.com/staz-tamjeed10/todo_frontend.git

cd ./todo_frontend

## run commands:
npm install

npm start

## create .env to connect frontend with backend:
REACT_APP_API_URL=http://localhost:8000/api


## Now both frontend and backend will work perfectly.
