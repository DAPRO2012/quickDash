from flask import Flask, render_template, session
import os
import shutil

class DashBoard:
    def __init__(self, importName, name="Dashboard", indexName="Index", secretKey: bytes = "--unsecure-secretkey--", **kwargs):
        self._app = Flask(importName, static_folder="templateFiles/static", template_folder="templateFiles/templates")
        self._app.secret_key = secretKey
        self.kwargs = kwargs
        @self._app.route("/")
        def index():
            return render_template("dashMainPage.html", name=name+" | "+indexName, theme=session.get("theme", "light"))
        
        def addPage(route: str, pageName: str):
            #@self._app.route(route)
            #def createPage():
            pass

    def run(self, host: str=None, port: int=None, debug: bool=None):
        if not self.kwargs.get("staticFolder", "static") in os.listdir(os.getcwd()):
            os.makedirs(os.path.join(os.getcwd(), self.kwargs.get("staticFolder", "static")))
        if not self.kwargs.get("staticFolder", "static")+"/css" in os.listdir(os.getcwd()+"/static"):
            shutil.copyfile(__file__+"/../templateFiles/static/style.css", os.path.join(os.getcwd(), self.kwargs.get("staticFolder", "static"), "css", "style.css"))
        self._app.run(host, port, debug)