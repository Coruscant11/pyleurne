from app import create_app, socket_io

app = create_app(False)

if __name__ == "__main__":
    socket_io.run(app)

