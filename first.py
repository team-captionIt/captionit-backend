from flask import Flask, request, jsonify, url_for, render_template


app = Flask(__name__)

#@app.route("/")

#def display():
#    return render_template()

@app.route("/") #, methods=['GET', 'POST'])

def show():
    return jsonify({"hello": [1, 2, 3, 4]})

if __name__ == '__main__':
    app.run(debug=True)
    