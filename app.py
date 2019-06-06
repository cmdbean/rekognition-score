from flask import Flask, render_template, request, redirect, url_for
from aws.s3 import *
from aws.rekognition import *


app = Flask(__name__)

params = {
    '73321': 'object/a',
    '32324': 'object/b',
    '39474': 'object/c',
    '93111': 'face/a',
    '42223': 'face/b',
    '00433': 'face/c',
    '00223': 'person/a',
    '78923': 'person/b',
    '62340': 'person/c',
}


@app.route("/")
def index():
    code = request.args.get('code')
    dir_path = params.get(code)

    if not dir_path:
        return '不正なコードです'

    files = get_file_list(dir_path)

    return render_template('index.html', code=code, files=files)


@app.route('/send', methods=['GET', 'POST'])
def send():
    code = request.args.get('code')
    dir_path = params.get(code)

    if not dir_path:
        return '不正なコードです'
    if request.method == 'POST':
        img_file = request.files['img_file']
        binary = img_file.stream.read()
        upload(binary, 'object/a/test.jpg')

        return redirect('index')


@app.route("/check")
def check():
    code = request.args.get('code')
    dir_path = params.get(code)

    if not dir_path:
        return '不正なコードです'

    files = get_file_list(dir_path)

    target = dir_path.split('/')[0]
    if target == 'object':
        for file in files:
            score = get_label_score()


if __name__ == "__main__":
    app.run(debug=True)
