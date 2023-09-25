from . import app


@app.route("/")
def hello_world():
    return "<p>Successful healthcheck!</p>"

@app.route("/healthcheck")
def healthcheck():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')