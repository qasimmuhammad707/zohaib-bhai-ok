from flask import Flask, render_template

# Use current directory for templates so existing index.html works
app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Listen on all interfaces so container is reachable from outside
    app.run(host="0.0.0.0", port=5000, debug=False)
