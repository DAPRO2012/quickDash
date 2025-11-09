from flask import Flask, render_template, session
from collections.abc import Callable
import os

class Dashboard():
    def __init__(self, module_name, title="Dashboard") -> None:
        self.app = Flask(module_name)
        self.title = title
        self.theme = "light"
        self.run = self.app.run
    

class Page():
    def __init__(self, dashboard: Dashboard, url: str, title: str) -> None:
        self.dashboard = dashboard
        self.title = title
        self.content = ""
        def mkPage():
            return render_template("master.html", title=f"{self.dashboard.title} | {self.title}", content = self.content, theme = self.dashboard.theme)
        mkPage.__name__ = self.title
        self.dashboard.app.add_url_rule(url, self.title, mkPage)

    def add_html(self, html: str):
        self.content += html

import data_representation
dash = Dashboard(__name__)
page1 = Page(dash, "/", "page1")
testData = data_representation.data("Test", [1, 3, 4, 2])
page1.add_html(testData.to_bar_chart(width=100))

dash.run(debug=True)