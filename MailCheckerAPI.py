import markdown
import markdown.extensions.fenced_code
from flask import Flask,jsonify,request
from app import MailChecker
from pygments.formatters import HtmlFormatter
import os

app = Flask(__name__)

@app.route('/')
def index():
    path = os.getcwd()+'/'+'README.md'
    readme_file = open(path, "r",encoding="utf8")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template


@app.route('/alldata/<string:email>',methods = ['GET', 'POST'])
def getdata(email : str):
    inst = MailChecker()
    data = inst.data_gath(email)
    return jsonify(data)



@app.route('/istemp/<string:email>',methods = ['GET', 'POST'])
def istemp(email : str):

    inst = MailChecker()
    data = inst.is_blacklisted(email)
    return jsonify(data)



@app.route('/isdelivrable/<string:email>',methods = ['GET', 'POST'])
def isdelivrable(email : str):

    inst = MailChecker()
    data = inst.is_delivrable(email)
    return jsonify(data)





if __name__ == '__main__':
    app.run()

