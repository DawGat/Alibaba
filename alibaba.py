import switches
from web_server import app

# Initiate GPIO switches
switches.initiate_switches()
# Starting web server
app.run('0.0.0.0', 5000, False)
