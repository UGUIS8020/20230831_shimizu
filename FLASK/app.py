from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    user_name = "SHIBUYA!"
    return render_template('index.html',user_name=user_name)

@app.route('/product')
def product():
    product_list = ["computer1","computer2","computer3"]
    product_dict = {"product_name":"computer1", "product_ptice":"4300","productmaker":"maker1"}
    return render_template('product.html',products=product_list,product_dict=product_dict)

@app.route('/test')
def test():
    return '<h1>Hello Test Page!</h1>'

@app.route('/user/<user_id>')
def userid(user_id):
    return '<h1>Your User Id is {0} {1} {2}</h1>'.format(user_id[0],user_id[1],user_id[2],)

@app.errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'),404

if __name__ == '__main__':
    app.run(debug=True)