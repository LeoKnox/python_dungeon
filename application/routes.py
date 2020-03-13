from application import app

@app.route("/")
@app.route("/index")
def index():
    return "<h1>start building</h1>"