import flask
from typing import Callable
import os
import math

request = flask.request

class Dashboard():
    def __init__(self, module_name, title="Dashboard") -> None:
        self.app = flask.Flask(module_name)
        self.title = title
        self.theme = "light"
        self.run = self.app.run
    
    def route(self, rule: str, **kwargs):
        def decorator(f: Callable):
            def mkPage():
                request = flask.request
                return flask.render_template("master.html", title=f"{self.title} | "+f.__name__, content=f"<h1>{f.__name__}</h1>"+f(), theme=self.theme)
            self.app.add_url_rule(rule, f.__name__, mkPage, None, **kwargs)
            return f
        return decorator

from data_representation import data, color
import random

dash = Dashboard(__name__)

def area_of_circle(radius: int):
    return int(radius*radius*math.pi)
def volume_of_cone(radius: int, height: int):
    return int(radius*radius*height*math.pi/3)
def volume_of_cylinder(radius: int, height: int):
    return int(radius*radius*math.pi*height)

def areas_using_radius(radius: int = 2, height: int = 2):
    return [area_of_circle(radius), volume_of_cone(radius, height), volume_of_cylinder(radius, height)]

@dash.route("/", methods=["GET", "POST"])
def Index():
    html = ""
    bar_chart = data("Coffees Sold", [(64, "Jan"), (55, "Feb"), (42, "Mar"), (29, "Apr"), (38, "May"), (34, "Jun"), (74, "Jul"), (52, "Aug"), (54, "Sep"), (62, "Oct"), (75, "Nov"), (89, "Dec")])
    pie_chart = data("Earth's Atmosphere", [(78, "Nitrogen"), (21, "Oxygen"), (1, "Other")])

    html += bar_chart.to_bar_chart([color(0, 128, 0), color("#FE620B"), color("#1A7DF2")])
    html += pie_chart.to_pie_chart([color(0, 128, 0), color("#FE620B"), color("#1A7DF2")])
    return html

dash.run(debug=True)