from products import products
from abc import abstractmethod


# Strategy Pattern
class SortingStrategy():
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

    # 이름 오름차순 정렬
    def name_ascending(self):
        return NameAscendingStrategy(self.products).sort()

    # 이름 내림차순 정렬
    def name_descending(self):
        return NameDescendingStrategy(self.products).sort()

    # 가격 오름차순 정렬
    def price_ascending(self):
        return PriceAscendingStrategy(self.products).sort()

    # 가격 내림차순 정렬
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
            return list(filter(lambda x: x["category"] == filter_value, self.products))
        elif filter_key == "season":
            return list(filter(lambda x: filter_value in x["season"], self.products))
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

def main():
    filter_strategy = ProductFilter(products)
    sort_key_list = ["name_asc", "name_desc", "price_asc", "price_desc"]

    while True:
        print("상품 정렬 방식을 선택하세요:")
        print("0. 종료")
        print("1. 이름 오름차순")
        print("2. 이름 내림차순")
        print("3. 가격 오름차순")
        print("4. 가격 내림차순")
        print("5. 카테고리 별로 선택하기")
        print("6. 시즌 별로 선택하기")

        choice = int(input("선택: "))

        if choice == 0:
            print("----- 쇼핑몰 서비스를 종료합니다 -----")
            break
        
        sort_key, filter_key, filter_value = None, None, None
        
        if choice <= 4:
            sort_key = sort_key_list[choice - 1]
            
        elif choice == 5:
            filter_key = "category"
            filter_value = input("카테고리를 선택하세요 (상의, 하의, 아우터): ")
            print("카테고리 내에서 정렬 방식을 선택하세요:")
            print("1. 이름 오름차순")
            print("2. 이름 내림차순")
            print("3. 가격 오름차순")
            print("4. 가격 내림차순")
            sub_choice = int(input("선택: "))
            sort_key = sort_key_list[sub_choice-1]

        elif choice == 6:
            filter_key = "season"
            filter_value = input("시즌을 선택하세요 (봄, 여름, 가을, 겨울): ")
            print("시즌 내에서 정렬 방식을 선택하세요:")
            print("1. 이름 오름차순")
            print("2. 이름 내림차순")
            print("3. 가격 오름차순")
            print("4. 가격 내림차순")
            sub_choice = int(input("선택: "))
            sort_key = sort_key_list[sub_choice-1]

        sorted_products = filter_strategy.filter_and_sort(filter_key, filter_value, sort_key)

        print("정렬된 상품 목록:")
        for product in sorted_products:
            print(f"상품명: {product['name']}, 가격: {product['price']}, 카테고리: {product['category']}, 계절:  {', '.join(product['season'])}")

if __name__ == "__main__":
    main()
