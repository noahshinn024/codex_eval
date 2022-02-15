def create_bouncing_ball_app():
  """
  create a website that takes an input and displays the length of the input
  on a blue bouncing ball that is bounded by the dimensions of the window;
  run the website on port 5000
  """
  
  # create the app
  app = Flask(__name__)

  # use the decorator pattern to
  # link the view function to a url
  @app.route("/")
  @app.route("/index")
  
"""
"""