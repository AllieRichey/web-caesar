from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto:
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <!-- TODO: create form here -->
        <form method = 'POST'>
        <label> Rotate by: <!--type=text-->
            <input name="rot" type="text" value="0" />
        </label>

        <br>

        <textarea name="text"></textarea>

        <br>

        <input type="submit" value="Submit" />
        
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])

    encrypted_string = rotate_string(text, rot)
    return '<h1>' + encrypted_string + '</h1>'


app.run()