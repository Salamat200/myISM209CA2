from flask import Flask, render_template

app = Flask(__name__) # create a flask app named app


@app.route("/")
def home():
       return '''My name is Dauda Salamat. This is my CA2 work.
My GitHub URL is https://github.com/Salamat200'''
# In the return statement above, Use your own name and GitHub URL

@app.route("/thesite")
def site():
       return render_template("index.html")


if __name__ == "__main__": app.run(port=5005)