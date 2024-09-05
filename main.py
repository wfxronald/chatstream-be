import time

from flask import Flask, request, Response, stream_with_context, make_response


app = Flask(__name__)


@app.route('/chat', methods=['POST','OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Headers', 'POST')
        return response

    def generate():
        user_message = request.json.get('message')
        fake_response = f"Hi user, you have input: {user_message}"
        for character in fake_response:
            time.sleep(0.1)  # pretend to slow down
            yield character

    resp = Response(stream_with_context(generate()), content_type='text/event-stream')
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
