from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle(
    'css/main.scss', 
    'css/administration.css',
    'caf/icon/activity.css', 
    'css/event/edit.css',
    'css/event/event.css',
    filters='pyscss', 
    output='all.css')
assets.register('scss_all', scss)