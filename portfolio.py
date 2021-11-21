from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__,
    static_folder="assets", 
    static_url_path="/assets")

@app.route("/<string:page>")
def main(page="index.html"):
    intro="""
        I'm Raphael Ferreira Python Developer
    """
    return render_template(page, intro=intro)

@app.route("/contact", methods=['POST'])
def contact():
    print(request.form.to_dict())
    message="Sua mensagem foi enviada com sucesso. Aguarde nosso contato"
    return render_template("contact.html", message=message)


