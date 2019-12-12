from flask import Flask, render_template
from preprocessing import func

app = Flask(__name__)
URL = 'https://s3.amazonaws.com/open-to-cors/assignment.json'


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
    # return 'Hello World'


@app.route('/base', methods=['POST', 'GET'])
def base():
    json_data = func(URL)
    return render_template('base.html', tables=[json_data.to_html(classes='data')], titles=json_data.columns.values)


if __name__ == '__main__':
    app.run()
