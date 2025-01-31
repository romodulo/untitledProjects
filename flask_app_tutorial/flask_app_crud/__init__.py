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
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, "flask_app_crud.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #test out the app.route way (decorator function)
    @app.route("/index2", methods = ["POST", "GET"])
    def custom_render_function():
        return render_template("index.html")

    def test_py_concepts():
        dictmine = {"so": "three", "far": "ten"}
        objectTwo = dictmine.get("far-out", 0)
        print("objectTwo:", objectTwo)
        #test pop
        objectTwo = dictmine.pop("far-out", "noValueGiven")
        print("objectTwo:", objectTwo)
    # commented-out:
    # test_py_concepts()


# create functions to handle database
    # import sqlite3
    # from datetime import datetime
    # import click
    # from flask imports current_app, g
#create the db.py file to initialize the database
    from . import db
    db.init_app(app)


# create a blueprint for views (start with "blogs-view" first)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
# create a blueprint for views (go with "auth-view" next)
    from . import auth
    app.register_blueprint(auth.bp)

    
# create view functions to render html files or otherwise
# write html templates
# link css files using the built-in url for function

    #return app
    return app

# make your project installable
# make your project deployable
# *optional: run a production web-server
# Done. 