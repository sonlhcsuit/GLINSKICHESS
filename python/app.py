from flask import Flask, request, jsonify
from algorithm import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    # print(request.get_json())
    return jsonify({"result": "WELCOME TO GLINSKI CHESS!"})


@app.route("/minimax", methods=['POST'])
def minimax_function():
    try:
        t0 = time.process_time()
        print(f"Start time: {t0:.10f}")

        body = request.get_json()
        notation = body["notation"]
        board = Board.from_notation(notation)
        value, move = minimax_prunning(board, -10000000, 100000000, 3, False)
        result = {
            "move": [int(move[0]), int(move[1])]
        }
        print(result)
        t1 = time.process_time()
        print(f"Elapse time: {t1 - t0:.10f}")
        print("------------------------------------------------------------------------------------------")
        return jsonify(result), 200
    except Exception as e:
        print(e)
        return {"error": f"Internal server error, {e}"}, 500


if __name__ == '__main__':
    app.run(debug=True)
