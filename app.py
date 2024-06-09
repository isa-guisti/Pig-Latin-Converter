from flask import Flask, request, render_template
from pig_latin_converter import convert_to_pig_latin

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        sentence = request.form['sentence']
        result = convert_to_pig_latin(sentence)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)