from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000, "emoji": "💻"},
    {"id": 2, "name": "Mobile", "price": 20000, "emoji": "📱"},
    {"id": 3, "name": "Headphones", "price": 3000, "emoji": "🎧"},
    {"id": 4, "name": "Smart Watch", "price": 5000, "emoji": "⌚"},
    {"id": 5, "name": "Keyboard", "price": 1500, "emoji": "⌨️"},
    {"id": 6, "name": "Mouse", "price": 800, "emoji": "🖱️"}
]

cart = []

@app.route("/")
def home():
    total = sum(item["price"] for item in cart)

    return render_template(
        "index.html",
        products=products,
        cart=cart,
        cart_count=len(cart),
        total=total
    )

@app.route("/add/<int:id>")
def add(id):
    for product in products:
        if product["id"] == id:
            cart.append(product)
            break

    return redirect(url_for("home"))

@app.route("/buy/<int:id>")
def buy(id):
    for product in products:
        if product["id"] == id:
            return render_template("order.html", product=product)

@app.route("/clear")
def clear():
    cart.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
