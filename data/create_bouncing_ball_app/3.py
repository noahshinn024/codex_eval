def create_bouncing_ball_app():
  """
  create a website that takes an input and displays the length of the input
  on a blue bouncing ball that is bounded by the dimensions of the window;
  run the website on port 5000
  """
  
  # create a flask app object
  app = Flask(__name__)

  # use the route decorator to tell flask what url triggers the function
  # below
  @app.route('/')
  
"""
"""