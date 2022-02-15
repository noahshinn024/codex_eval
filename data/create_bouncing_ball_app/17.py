def create_bouncing_ball_app():
  """
  create a website that takes an input and displays the length of the input
  on a blue bouncing ball that is bounded by the dimensions of the window;
  run the website on port 5000
  """
  
  
  # create a web app
  app = Flask(__name__)
  
  # create the routes
  @app.route("/")
  @app.route("/<int:ball_radius>")
  @app.route("/<int:ball_radius>/<color>")
  
"""
"""