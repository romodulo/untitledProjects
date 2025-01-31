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


# import what you need to import
import os
from flask import Flask
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
    app.config.mapping(
        SECRET = 'dev',
        DATABASE = os.path.join(app_instance_path, "flaskr.sqlite"),
    )

    #test out the app.route way (decorator function)
    @app.route("/index", method = ["POST", "GET"])
    def normal_function():
        return "Hello Function!"


    return app

# create functions to handle database


# create a blueprint for views
# create view functions to render html files or otherwise
# wriite html templates
# link css files using the built-in url for function
# make your project installable
# make your project deployable
# *optional: run a production web-server
# Done. 