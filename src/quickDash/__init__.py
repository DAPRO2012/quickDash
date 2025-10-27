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
        #If static folder doesnt exist then create
        if not self.kwargs.get("staticFolder", "static") in os.listdir(os.path.join(__file__, "..")):
            os.makedirs(os.path.join(__file__, "..", self.kwargs.get("staticFolder", "static")))
        #If css in static folder does not exist then create
        if not "css" in os.listdir(os.path.join(__file__, "..", self.kwargs.get("staticFolder", "static"))):
            os.mkdir(os.path.join(__file__, "..", self.kwargs.get("staticFolder", "static"), "css"))
        # if the main styling is not copied then copy
        if not "style.css" in os.listdir(os.path.join(__file__, "..", self.kwargs.get("staticFolder", "static"), "css")):
            shutil.copyfile(os.path.join(__file__, "..", "templateFiles", "static", "style.css"), os.path.join(os.getcwd(), self.kwargs.get("staticFolder", "static"), "css", "style.css"))
        if not self.kwargs.get("templatesFolder", "templates") in os.listdir(os.path.join(__file__, "..", self.kwargs.get("templatesFolder", "templates"))):
            shutil.copyfile(os.path.join(__file__, "..", "templateFiles", "static", "style.css"), os.path.join(os.getcwd(), self.kwargs.get("staticFolder", "static"), "css", "style.css"))
        self._app.run(host, port, debug)
        self._app.run(host, port, debug)