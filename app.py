from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')