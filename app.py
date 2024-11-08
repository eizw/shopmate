import flask

app = flask.Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def main():
    return flask.render_template("index.html")

@app.route('/items')
def item_list():
    return flask.render_template("item_list.html")

if __name__ == '__main__':
    app.run(debug=True)