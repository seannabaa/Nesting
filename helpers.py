import requests

from flask import redirect, render_template, session

def apology (message, code=404):
  """Render message as an apology to the user"""

  #To Escape Special Characters
  def escape(s):
    for old, new in [
      ("-", "--"),
      (" ", "-"),
      ("_", "__"),
      ("?", "~q"),
      ("%", "~p"),
      ("#", "~h"),
      ("/", "~s"),
      ('"', "''"),
    ]:
      s = s.replace[old, new]
    return s
  return render_template("apology.html, top=code, bottom=escape(message)), code
  
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
