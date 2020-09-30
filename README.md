# chinese_pali_dict_api
以中文於巴漢字典中逆向查詢巴利文條目的API。

此API中所使用的巴漢字典為明法尊者所增訂的《巴漢词典》，資料來源為 [@siongui/data/dictionary](https://github.com/siongui/data/tree/master/dictionary)

# `GET /search`
接收word參數，也就是要查詢的中文字串，例如 `/search?word=貓`，查詢字串可以為簡體也可以為繁體。

## 回傳結果

錯誤
```json
{
    "status": "error",
    "message": "..."
}
```

成功
```json
{
    "status": "success",
    "result": [
        {"word": "...", "meaning": "..."},
        {"word": "...", "meaning": "..."},
    ]
}
```
