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
    
# Adapter pattern
class ProductsAdapter:
    def __init__(self, products):
        self.products = products

    def apply_sorting_strategy(self, strategy):
        return strategy.sort()
    
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

def main():
    builder = ProductsBuilder(products)

    while True:
        print("상품 정렬 방식을 선택하세요:")
        print("0. 종료")
        print("1. 이름 오름차순")
        print("2. 이름 내림차순")
        print("3. 카테고리 별로 선택하기")
        print("4. 시즌 별로 선택하기")
        print("5. 가격 오름차순")
        print("6. 가격 내림차순")
        choice = int(input("선택: "))

        if choice == 0:
            print("----- 쇼핑몰 서비스를 종료합니다 -----")
            break
        
        elif choice in [1, 2, 5, 6]:
            sorted_products = builder.name_ascending() if choice == 1 else \
                              builder.name_descending() if choice == 2 else \
                              builder.price_ascending() if choice == 5 else \
                              builder.price_descending()
        elif choice == 3:
            category = input("카테고리를 선택하세요 (상의, 하의, 아우터): ")
            picked_products = list(filter(lambda x: x["main-category"] == category, products))
            category_builder = ProductsBuilder(picked_products)
            print("카테고리 내에서 정렬 방식을 선택하세요:")
            print("1. 이름 오름차순")
            print("2. 이름 내림차순")
            print("3. 가격 오름차순")
            print("4. 가격 내림차순")
            sub_choice = int(input("선택: "))
            sorted_products = category_builder.name_ascending() if sub_choice == 1 else \
                              category_builder.name_descending() if sub_choice == 2 else \
                              category_builder.price_ascending() if sub_choice == 3 else \
                              category_builder.price_descending()
        elif choice == 4:
            season = input("시즌을 선택하세요 (봄, 여름, 가을, 겨울): ")
            picked_products = list(filter(lambda x: season in x["season"], products))
            season_builder = ProductsBuilder(picked_products)
            print("시즌 내에서 정렬 방식을 선택하세요:")
            print("1. 이름 오름차순")
            print("2. 이름 내림차순")
            print("3. 가격 오름차순")
            print("4. 가격 내림차순")
            sub_choice = int(input("선택: "))
            sorted_products = season_builder.name_ascending() if sub_choice == 1 else \
                              season_builder.name_descending() if sub_choice == 2 else \
                              season_builder.price_ascending() if sub_choice == 3 else \
                              season_builder.price_descending()

        print("정렬된 상품 목록:")
        for product in sorted_products:
            print(product)

if __name__ == "__main__":
    main()
