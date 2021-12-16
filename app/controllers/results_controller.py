from app.controllers.controller import ControllerBase
from flask import render_template


class ResultsController(ControllerBase):
    @staticmethod
    def get():
        return render_template('results.html')
