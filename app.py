from flask import Flask, render_template, request

app = Flask(__name__)

def transform(text):
    var = text
    lower = True
    for i in range(len(text)):
        if var[i].isalpha():
            edit = var[i].lower() if lower == True else var[i].upper()
            pre = "" if i == 0 else var[:i]
            post = "" if i == len(text) else var[i+1:]
            var = pre + edit + post
            lower = ~lower
    return var

@app.get("/")
def main_menu():
    return render_template('index.html')

@app.post("/")
def case_method():
    original = request.form['original']
    result = transform(original)
    return {
        "original": original,
        "result": result
    }

if __name__ == "__main__":
    app.run()