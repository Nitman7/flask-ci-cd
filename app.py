from flask import flask
app = Flask(_name_)

@app.route("/")
def hello():
       return "Deployed Via AWS CodePipeline and GitHub!"

if _name_ == "_main_":
     app.run()


