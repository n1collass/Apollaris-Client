
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home():
    return render_template('some_page.html')