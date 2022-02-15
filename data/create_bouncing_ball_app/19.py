def create_bouncing_ball_app():
  """
  create a website that takes an input and displays the length of the input
  on a blue bouncing ball that is bounded by the dimensions of the window;
  run the website on port 5000
  """
  
  # Create app
  app = Flask(__name__)

  # Setup app
  app.config['SECRET_KEY'] = 'secret!'
  app.config['DEBUG'] = True
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

  @app.route('/')
  
"""
"""