# create a virtual environment
#     python3 -m venv .myvenv
#     activate .myvenv: source .myvenv/bin/activate
# create some files, and directories for the application
#     each template is under a specific directory tree...
# create an application factory
#     function definition name: create_app()
#     config = None as the parameter


# notes**at some point, I will need to connect the database
# connect the database
#     import sqlite3
#     copied-notes: from datetime import datetime

# create a blueprint

# Recap: 
# venv
# pip install flask
# import what you need to import
# create multiple directories:
# templates, static, sub-directories for different templates:
# auth
# start writing an application factory function
# *specifics: import g and initialize or set g.db
# to connect database. 
# *endOfSpecifics
# create functions to handle database
# create a blueprint for views
# create view functions to render html files or otherwise
# wriite html templates
# link css files using the built-in url for function
# make your project installable
# make your project deployable
# *optional: run a production web-server
# Done. 

# To-do List Idea
# Business Plan Tracker
#   What do I want to do? 




# Recap: 
# venv
# ### done
# pip install flask
# ### done
# import what you need to import
# ### i.progress

# create multiple directories:
# ### i.progress
#
# create multiple directories:
# templates, 
# static, 
#
# sub-directories for different templates:
# auth

# start writing an application factory function
# ### i.progress

# create functions to handle database
# create a blueprint for views
# create view functions to render html files or otherwise
# wriite html templates
# link css files using the built-in url for function
# make your project installable
# make your project deployable
# *optional: run a production web-server
# Done. 
# *Notes: One curcial step I forgot was to place the
#           application factory function in a __init__.py
#           file. 
# *Notes: "ensure the app.instance_path exists"
#           | use the try except operator
#           |



# import what you need to import
import os
from flask import (Flask, render_template)
#need to import Bluepring, g, render_template, redirect, url_for

# create multiple directories:
# templates, done
# static, done
#
# sub-directories for different templates:
# auth, done
# blog, done

# start writing an application factory function
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True) #instance relative config set to True
    app.config.from_mapping(
        SECRET = 'dev',
        DATABASE = os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #test out the app.route way (decorator function)
    @app.route("/index", methods = ["POST", "GET"])
    def custom_render_function():
        return render_template("index.html")


    return app

# create functions to handle database
    # import sqlite3
    # from datetime import datetime
    # import click
    # from flask imports current_app, g
import sqlite3
from datetime import datetime
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES

        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

def test_py_concepts():
    dictmine = {"so": "three", "far": "ten"}
    objectTwo = dictmine.get("far-out", 0)
    print("objectTwo:", objectTwo)
    #test pop
    objectTwo = dictmine.pop("far-out", "noValueGiven")
    print("objectTwo:", objectTwo)
test_py_concepts()


# create a blueprint for views
# create view functions to render html files or otherwise
# write html templates
# link css files using the built-in url for function
# make your project installable
# make your project deployable
# *optional: run a production web-server
# Done. 