from flask import Flask, render_template
from Services.ServiceURL import ServiceURL


app = Flask(__name__)

@app.route('/index', methods=["GET"])
def index():
    pythonUrl = {'python': ['https://www.python.org/',
                                'https://www.python.org/about/help/',
                                'https://www.python.org/community/logos/']}
    ServiceURL.URL(pythonUrl)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)