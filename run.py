from app import socket_io
from app import app

if __name__ == "__main__":
    socket_io.run(app, host='0.0.0.0')

