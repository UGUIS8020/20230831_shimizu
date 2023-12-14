from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Prosuct Page</h1>"

@app.route("/product/<product_id>")
def productid(<product_id):
    return "<h1>Product Name:</h1>"


          product_list = [
        ["1", "ノートパソコンA", "Core i5", "￥68,500"],
        ["2", "ノートパソコンB", "AMD Ryzen 5", "￥81,300"],
        ["3", "ノートパソコンC", "CeleronN4020", "￥64,300"]
    ]
    for product in product_list:

if __name__ == "__main__":
    app.run(debug=True)




