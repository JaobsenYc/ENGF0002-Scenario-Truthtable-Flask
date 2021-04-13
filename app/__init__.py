"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""

from dotenv import load_dotenv
from flask import Flask


def register_blueprints(app):
    from app.api.cms import create_cms
    from app.api.v1 import create_v1

    app.register_blueprint(create_v1(), url_prefix="/v1")
    app.register_blueprint(create_cms(), url_prefix="/cms")


def register_cli(app):
    from app.cli import db_cli, plugin_cli

    app.cli.add_command(db_cli)
    app.cli.add_command(plugin_cli)


def register_api(app):
    from lin.apidoc import api

    api.register(app)


def apply_cors(app):
    from flask_cors import CORS

    CORS(app)


def load_app_config(app):
    env = app.config.get("ENV")
    load_dotenv(".{env}.env".format(env=env))
    app.config.from_object(
        "app.config.{env}.{Env}Config".format(env=env, Env=env.capitalize())
    )


def set_global_config(**kwargs):
    from lin.config import global_config

    for k, v in kwargs.items():
        if k.startswith("config_"):
            global_config[k[7:]] = v


def create_app(register_all=True, **kwargs):
    load_dotenv(".flaskenv")
    app = Flask(__name__, static_folder="../assets")
    load_app_config(app)
    if register_all:
        from lin import Lin

        set_global_config(**kwargs)
        register_blueprints(app)
        register_api(app)
        apply_cors(app)
        Lin(app, **kwargs)
        register_cli(app)
    return app
