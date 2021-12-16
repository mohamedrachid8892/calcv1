from app.controllers.controller import ControllerBase
from flask import render_template


class LinksController(ControllerBase):
    @staticmethod
    def get():
        return render_template('links.html')
