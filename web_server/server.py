from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import redirect
from t import solve
app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        mat = request.form.to_dict()
        r = [[int(mat[str(x)]) for x in range(j, j+9)]
             for j in range(1, 82, 9)]
        # print(r)
        r = solve(r)

        # for i in range(9):
        #     for j in range(9):
        #         print(r[i][j], end=" ")
        #     print()
        if r == 1:
            return render_template('err.html')
        else:
            return render_template('result.html', r=r)
    if request.method == "GET":
        return render_template('index.html')