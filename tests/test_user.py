"""
    :copyright: © 2020 by the Lin team.
    :Copyright (c) 2021 Chen Yang, Siqi Zhu,Jeffrey Li,Minyi Lei
    :license: MIT, see LICENSE for more details.
"""


from . import app, fixtureFunc, get_token


def test_change_nickname(fixtureFunc):
    with app.test_client() as c:
        rv = c.put(
            "/cms/user",
            headers={"Authorization": "Bearer " + get_token()},
            json={"nickname": "tester"},
        )
        assert rv.status_code == 201
