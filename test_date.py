from flask import Flask
from flask import render_template
import json
# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    date = json.load(open('date.json'))['date']
    return render_template('index.html', incident_date=date)

# run the application
if __name__ == "__main__":
    app.run(debug=True)