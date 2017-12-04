from flask import Flask, render_template, jsonify
from flask import request
import data_model as dm

app = Flask(__name__)

@app.route('/')
@app.route('/labelme')
def review():
    # if db is empty is not handled
    (object_id, url, words, rating) = dm.get_review_words()
    return render_template('index.html', words = words, object_id=object_id, url = url, rating=rating)


@app.route('/alwr')
def alwr():
    return render_template('alwr.html')


@app.route('/save',methods=['POST'])
def save():
    data = request.get_json(force=True)
    dm.save(data)
    print("Rationals saved = ", data)
    return jsonify({"ok":"saved"})


@app.route('/thankyou/')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1527, debug=True)
