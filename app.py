from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def front_page():
    message = None
    if request.method == 'POST':
        # Replace this with whatever logic you want to run on START click
        # For now, just a confirmation message:
        message = "START button clicked — place your logic here!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
