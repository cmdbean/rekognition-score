from flask import Flask, render_template, request, redirect, url_for
from aws.s3 import *
from aws.rekognition import *
from datetime import datetime


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
        ext = img_file.filename.rsplit('.', 1)[1]
        ts = str(int(datetime.now().timestamp() * 100))
        file_path = dir_path + '/' + ts + f'.{ext}'
        binary = img_file.stream.read()
        upload(binary, file_path)

        return redirect(f'/?code={code}')


@app.route("/check")
def check():
    code = request.args.get('code')
    dir_path = params.get(code)

    if not dir_path:
        return '不正なコードです'

    files = get_file_list(dir_path)

    scores = {}
    target = dir_path.split('/')[0]
    for file in files:
        if target == 'object':
            label, score = get_label_score(file, 'Breakfast')
        elif target == 'face':
            label, score = get_emotion_score(file, 'HAPPY')
        elif target == 'person':
            label, score = get_celebrity_score(file, 'breakfast')

        scores[file.key] = score
        print(scores)

    return render_template('index.html', code=code, files=files, scores=scores)


if __name__ == "__main__":
    app.run(debug=True)
