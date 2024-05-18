from products import products

def sort_products(products, key):
    if key == 1:
        sorted_products = sorted(products, key=lambda x: x["name"])  # 이름 오름차순
    elif key == 2:
        sorted_products = sorted(products, key=lambda x: x["name"], reverse=True)  # 이름 내림차순
    elif key == 3:
        category = input("카테고리를 선택하세요 (상의, 하의, 아우터): ")
        sorted_products = sorted(filter(lambda x: x["main-category"] == category, products), key=lambda x: x["name"])
    elif key == 4:
        season = input("시즌을 선택하세요 (봄, 여름, 가을, 겨울): ")
        sorted_products = sorted(filter(lambda x: season in x["season"], products), key=lambda x: x["name"])
    elif key == 5:
        sorted_products = sorted(products, key=lambda x: x["price"])  # 가격 오름차순
    elif key == 6:
        sorted_products = sorted(products, key=lambda x: x["price"], reverse=True)
        
    return sorted_products

def main():
    while True:
        print("정렬 방식을 선택하세요:")
        print("1. 이름 오름차순")
        print("2. 이름 내림차순")
        print("3. 카테고리 별로 선택하기")
        print("4. 시즌 별로 선택하기")
        print("5. 가격 오름차순")
        print("6. 가격 내림차순")
        print("0. 종료")
        choice = int(input("선택: "))

        if choice == 0:
            break
        else:
            sorted_products = sort_products(products, choice)

        print("정렬된 상품 목록:")
        for product in sorted_products:
            print(product)

if __name__ == "__main__":
    main()
