from flask import Flask
from flask import render_template, request
from datetime import date
from monthdelta import monthdelta
import json
# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/", methods=['GET', 'POST'])
def hello():
    dt = json.loads(json.load(open('date.json')))['date']

    if request.method == 'POST':
        if request.form['reset'] == 'RESET THE COUNTER':
            dt = date.today().strftime("%Y, %m, %d")
            dt = dt.split(', ')
            dt[1] = str(int(dt[1])-1)
            dt = ', '.join(dt)
            with open('date.json', 'w') as f:
                json.dump(json.dumps({"date": dt}), f)
            return render_template('pyindex.html', incident_date=dt)
    return render_template('pyindex.html', incident_date=dt)

# run the application
if __name__ == "__main__":
    app.run(debug=True)
