# How to run the application

## Pre-requisites
* python3.8+
* pip
* postgresql with psql client

# Create virtual environment
* `python3.8 -m venv ~/test-backend`
* `source ~/test-backend`
* `pip install -r requirements.txt`

# Database configuration
* make sure to create and setup conference database with all permissions to postgres user
* set password = `new_password` for running current application
* If you already have already have test database change the database uri in the `factory.py`

# Migrate Database Commands
```
 flask db init
 flask db migrate
 flask db upgrade
 ```

# Run the application
* `python run_app.py`

# Access `http://127.0.0.1:5000/` to check swagger doc

# Postman collection link
* Backend-postman.json 

# Comments
* As the document mentioned basic conference building website the below are expected
    * need to add test cases
    * there are edge cases as per real world scenario which I can fix if needed.