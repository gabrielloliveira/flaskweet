from flask import Flask

app = Flask(__name__)

app.config.update(
    ENV="development",
    DEBUG=True,
)

from .controllers import urls
