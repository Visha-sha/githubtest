#pip install flask
#pip install pandas

from flask import Flask, jsonify, render_template
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Id":456, "type":"string","report":"All good"})


@app.route("/tablepage", methods=['GET'])
def table():
    data_dic = {
        'id': [100, 101, 102],
        'color': ['red', 'blue', 'red']}
    columns = ['id', 'color']

    df = pd.DataFrame(data_dic, columns=columns)
    table = df.to_html(index=False)

    return render_template(
        "table.html",
        table=table)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)