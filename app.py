#import operating system
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
