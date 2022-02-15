def create_bouncing_ball_app():
  """
  create a website that takes an input and displays the length of the input
  on a blue bouncing ball that is bounded by the dimensions of the window;
  run the website on port 5000
  """
  
  # create a socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # bind the socket to the host and port
  server_socket.bind(('', 5000))
  # listen for an incoming connection
  server_socket.listen(1)
  # accept an incoming connection
  client_socket, client_address = server_socket.accept()
  # get the response from the client
  response = client_socket.recv(1024).decode()
  # get the dimensions of the window
  window_dimensions = (int(response.split(',')[0]), int(response.split(',')[1]))
  # create a canvas
  canvas = Canvas(window_dimensions)
  # create a pattern
  pattern = Pattern(canvas)
  # create a ball
  ball = Ball(window_dimensions, canvas, pattern)
  # create a bouncing ball animation
  bouncing_ball_animation = Animation(window_dimensions, ball)
  # create a flow of balls
  flow_of_balls_animation = Animation(window_dimensions, pattern)
  # create a bouncing ball application
  bouncing_ball_app = Application(window_dimensions, bouncing_ball_animation, flow_of_balls_animation)
  # create a website that displays the bouncing ball application
  website = Website(bouncing_ball_app)
  # create a website server
  website_server = WebsiteServer(website, client_socket)
  # run the website server
  website_server.run()
  # close the socket
  client_socket.close()
  server_socket.close()


"""
"""