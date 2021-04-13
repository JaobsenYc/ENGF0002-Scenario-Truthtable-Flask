"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""

import os
from datetime import timedelta


class BaseConfig(object):
    """
    基础配置
    """

    # read configuration from env

    # assign secret key
    SECRET_KEY = os.getenv("SECRET_KEY", "https://github.com/TaleLin/lin-cms-flask")


    # set database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:////" + os.getcwd() + os.path.sep + "lincms.db",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # get token
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # default file upload restrictions
    FILE = {
        "STORE_DIR": "assets",
        "SINGLE_LIMIT": 1024 * 1024 * 2,
        "TOTAL_LIMIT": 1024 * 1024 * 20,
        "NUMS": 10,
        "INCLUDE": set(["jpg", "png", "jpeg"]),
        "EXCLUDE": set([]),
    }

    # log setting
    LOG = {
        "LEVEL": "DEBUG",
        "DIR": "logs",
        "SIZE_LIMIT": 1024 * 1024 * 5,
        "REQUEST_LOG": True,
        "FILE": True,
    }

    COUNT_DEFAULT = 10
    PAGE_DEFAULT = 0

    # enable compatibility of utf-8
    JSON_AS_ASCII = False
