from flask import Flask, render_template, request, send_file
from modules.generate_image import draw
from modules.transform import transform

app = Flask(__name__)

@app.get("/")
def main_menu():
    return render_template('index.html')

@app.post("/")
def submit():
    original = request.form['original']
    result = transform(original)
    if request.form['submit'] == "Generate Text":
        return {
            "original": original,
            "result": result
        }
    else:
        return send_file(draw(result), mimetype='image/jpeg')


if __name__ == "__main__":
    app.run(debug=True)