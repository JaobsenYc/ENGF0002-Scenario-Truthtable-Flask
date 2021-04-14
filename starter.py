"""
        :copyright: © 2020 by the Lin team.
        :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
        :license: MIT, see LICENSE for more details.
    """
from flask import Flask, render_template, send_from_directory
from app import create_app
from app.config.code_message import MESSAGE
from app.config.http_status_desc import DESC
from app.model.lin import (
    Group,
    GroupPermission,
    Permission,
    User,
    UserGroup,
    UserIdentity,
)

app = create_app(
    group_model=Group,
    user_model=User,
    group_permission_model=GroupPermission,
    permission_model=Permission,
    identity_model=UserIdentity,
    user_group_model=UserGroup,
    config_MESSAGE=MESSAGE,
    config_DESC=DESC,)


if app.config.get("ENV") != "production":

    @app.route('/', defaults={'path': ''})
    @app.route('/')
    def catch_all():
        return render_template("/index/index.html")


    @app.route('/user/static/<path:filename>')
    def base_static(filename):
        return send_from_directory(app.root_path + '/../dist/user/static/', filename)


    @app.route('/#/user/')
    @app.route('/user/')
    def user():
        return render_template("/user/index.html")

if __name__ == "__main__":
    app.logger.warning(
        """
        ----------------------------
        |  app.run() => flask run  |
        ----------------------------
        """
    )
    app.run()
