# CS 316 Flask Application Example

### Starting the App
1. activate a new virtual environment using either venv or conda (python 3.7.4)
2. once the environment is active, run `pip install -r requirements.txt`
3. 
  * Mac/Linux: from the root of the project run `export FLASK_APP=flask_template.py` followed by `flask run`

  * Windows: in the command prompt run `C:\path\to\app>set FLASK_APP=flask_template.py` followed by `flask run`

4. run `python seed_test_db.py`


For deployment
`gunicorn -D -b 0.0.0.0 flask_template:app`