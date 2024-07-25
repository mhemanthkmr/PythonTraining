from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

@app.route('/')
def helloworld():
    print(os.getenv("AI_KEY"))
    return "HelloWorld"

if __name__ == '__main__':
    app.run(debug=True, port=8080)