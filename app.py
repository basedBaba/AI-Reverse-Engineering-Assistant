import os

from flask import Flask, jsonify, render_template, request

from utils.ai_explainer import explain_code, generate_summary
from utils.decompiler import decompile

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    c_code, asm_code = decompile(filepath)

    summary = generate_summary(c_code)

    return render_template(
        "index.html", asm_code=asm_code, c_code=c_code, summary=summary
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.json.get("code")
    explanation = explain_code(code)
    return jsonify({"explanation": explanation})


if __name__ == "__main__":
    app.run(debug=True)
