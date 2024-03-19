import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f'''...................／＞　 フ.....................<br/>
　　　　　| 　_　 _|<br/>
　 　　　／`ミ _x 彡<br/>
　　 　 /　　　 　 |<br/>
　　　 /　 ヽ　　 ﾉ<br/>
　／￣|　　 |　|　|<br/>
　| (￣ヽ＿_ヽ_)_)<br/>
　＼二つ'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)