import flask
from flask import jsonify,request
from flask_cors import CORS
import pandas as pd
from opencc import OpenCC
import json

cc = OpenCC("t2s")
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False
MAX_ROW = 200
pali_dict = pd.read_csv("巴漢字典_明法尊者.csv", header=None)

CORS(app)

@app.route('/search', methods=['GET'])
def home():
	word = request.args.get('word')
	if word is None:
		return jsonify({'status': 'error', 'message': '請提供word參數。'})
	print(word)
	simplified_word = cc.convert(word)

	df = pali_dict[pali_dict[2].str.contains(simplified_word)]

	# 檢查結果的總row數，太長就不要回傳
	if df.shape[0] > MAX_ROW:
		return jsonify({
		'status': 'error',
		'result': '查詢結果超過200筆，請限縮關鍵詞。'
	})

	result_df = df.iloc[:,[1, 2]]
	result_wordlist = list()

	for ind in result_df.index:
		word = result_df[1][ind]
		meaning = result_df[2][ind]
		result_wordlist.append({
			"word":word,
			"meaning": meaning
		})


	return jsonify({
		'status': 'success',
		'result': result_wordlist
	})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888")
