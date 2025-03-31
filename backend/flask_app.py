import sys

# Add your app's directory to the PYTHONPATH
path = 'O:/test_deploy/test_deploy'
if path not in sys.path:
    sys.path.append(path)

from backend.app import app as application
from flask import send_from_directory
import os

@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join('O:/test_deploy/test_deploy/build', path)):
        return send_from_directory('O:/test_deploy/test_deploy/build', path)
    else:
        return send_from_directory('O:/test_deploy/test_deploy/build', 'index.html')