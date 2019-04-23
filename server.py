from flask import Flask, render_template
app = Flask(__name__)

files = [
    {
        'name': '/path/to/file0',
    },
    {
        'name': '/path/to/file1',
    }
]


@app.route('/')
def hello_world():
    return render_template('files.html', files=files)


if __name__ == '__main__':
    app.run(debug=True)
