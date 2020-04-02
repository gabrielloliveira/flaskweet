from flask import Flask


app = Flask("core")

@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
