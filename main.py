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

def get_display_width(text):
    # 한글 글자는 2의 폭을 차지하므로, 각 글자를 검사하여 전체 폭을 계산
    return sum(2 if ord(char) > 127 else 1 for char in text)

def pad_to_fixed_width(text, width):
    # 원하는 고정 너비에 맞추기 위해 필요한 공백을 계산하고 추가
    text_width = get_display_width(text)
    if text_width < width:
        padding = ' ' * (width - text_width)
        return text + padding
    return text

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
        
        # 고정된 폭 설정
        name_width = 30
        price_width = 20
        category_width = 20
        season_width = 20

        # 출력 헤더
        header = f"{pad_to_fixed_width('상품명', name_width)}|{pad_to_fixed_width('가격', price_width)}|{pad_to_fixed_width('카테고리', category_width)}|{pad_to_fixed_width('계절', season_width)}"
        print("\n정렬된 상품 목록:")
        print(header)
        print("-" * (name_width + price_width + category_width + season_width + 3))  # 구분자 '|' 기호를 고려하여 길이 조정

        # 상품 목록 출력
        for product in sorted_products:
            name = pad_to_fixed_width(product['name'], name_width)
            price = pad_to_fixed_width(str(product['price']), price_width)
            category = pad_to_fixed_width(product['category'], category_width)
            season = pad_to_fixed_width('.'.join(product['season']), season_width)

            # 모든 항목을 포맷 문자열을 사용하여 고정된 너비로 출력
            print(f"{name}|{price}|{category}|{season}")

if __name__ == "__main__":
    main()
