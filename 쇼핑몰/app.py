from flask import Flask, render_template, request
from products import products
from abc import ABC, abstractmethod

app = Flask(__name__)

# Strategy Pattern
class SortingStrategy(ABC):
    def __init__(self, products):
        self.products = products

    @abstractmethod
    def sort(self):
        pass

# 이름 오름차순 정렬 전략
class NameAscendingStrategy(SortingStrategy):
    def sort(self):
        return sorted(self.products, key=lambda x: x["name"])

# 이름 내림차순 정렬 전략
class NameDescendingStrategy(SortingStrategy):
    def sort(self):
        return sorted(self.products, key=lambda x: x["name"], reverse=True)

# 가격 오름차순 정렬 전략
class PriceAscendingStrategy(SortingStrategy):
    def sort(self):
        return sorted(self.products, key=lambda x: x["price"])

# 가격 내림차순 정렬 전략
class PriceDescendingStrategy(SortingStrategy):
    def sort(self):
        return sorted(self.products, key=lambda x: x["price"], reverse=True)

# Builder Pattern
class ProductsBuilder:
    def __init__(self, products):
        self.products = products

    def name_ascending(self):
        return NameAscendingStrategy(self.products).sort()

    def name_descending(self):
        return NameDescendingStrategy(self.products).sort()

    def price_ascending(self):
        return PriceAscendingStrategy(self.products).sort()

    def price_descending(self):
        return PriceDescendingStrategy(self.products).sort()

# Template Method Pattern
class ProductFilter:
    def __init__(self, products):
        self.products = products

    def filter_and_sort(self, filter_key=None, filter_value=None, sort_key=None):
        filtered_products = self.filter_products(filter_key, filter_value)
        return self.sort_filtered_products(filtered_products, sort_key)

    def filter_products(self, filter_key, filter_value):
        if filter_key == "category":
            return [p for p in self.products if p["category"] == filter_value]
        elif filter_key == "season":
            return [p for p in self.products if filter_value in p["season"]]
        else:
            return self.products

    def sort_filtered_products(self, filtered_products, sort_key):
        builder = ProductsBuilder(filtered_products)
        if sort_key == "name_asc":
            return builder.name_ascending()
        elif sort_key == "name_desc":
            return builder.name_descending()
        elif sort_key == "price_asc":
            return builder.price_ascending()
        elif sort_key == "price_desc":
            return builder.price_descending()
        else:
            return filtered_products

@app.route('/')
def index():
    filter_key = request.args.get('filter_key')
    filter_value = request.args.get('filter_value')
    sort_key = request.args.get('sort_key')

    filter_strategy = ProductFilter(products)
    sorted_products = filter_strategy.filter_and_sort(filter_key, filter_value, sort_key)

    return render_template('index.html', products=sorted_products, filter_key=filter_key, filter_value=filter_value, sort_key=sort_key)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
