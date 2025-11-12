import flask
from typing import Callable
import os

class Dashboard():
    def __init__(self, module_name, title="Dashboard") -> None:
        self.app = flask.Flask(module_name)
        self.title = title
        self.theme = "light"
        self.run = self.app.run
    
    def route(self, rule: str, **kwargs):
        def decorator(f: Callable):
            def mkPage():
                return flask.render_template("master.html", title=f.__name__, content=f(), theme=self.theme)
            self.app.add_url_rule(rule, f.__name__, mkPage, None, **kwargs)
            return f
        return decorator

import data_representation
import random

dash = Dashboard(__name__)

@dash.route("/", methods=["GET", "POST"])
def Index():
    if flask.request.method == "POST":
        testdata = data_representation.data("Something", [int(flask.request.form.get("int1", "0")), int(flask.request.form.get("int2", "0"))])
    else:
        testdata = data_representation.data("Something", [1, 1])
    return data_representation.form("form1", int1=int, int2=int)+testdata.to_bar_chart()

dash.run(debug=True)