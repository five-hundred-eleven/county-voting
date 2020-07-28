#!/usr/bin/env python3

import dash_html_components as html
import dash_core_components as dcc

from flask import Flask
from dash import Dash

APP = Flask(__name__)
DASH = Dash(
    __name__,
    server=APP,
)


