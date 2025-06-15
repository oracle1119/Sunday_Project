# def list_type(lst):
#     match lst:
#         case [x, y]:
#             return f"List with two elements: {x} and {y}"
#         case [x, *rest]:
#             return f"List starts with {x}, followed by {rest}"
#         case []:
#             return "Empty list"
#         case _:
#             return "Other list"
#
# print(list_type([1, 2]))        # List with two elements: 1 and 2
# print(list_type([1, 2, 3, 4]))  # List starts with 1, followed by [2, 3, 4]
# print(list_type([]))            # Empty list



# 람다 함수를 활용한 간단한 연산

price_after_discount = lambda price: price * 0.9
tax_calculator = lambda amount, rate=0.1: amount * (1 + rate)
print(price_after_discount(10000))
print(tax_calculator(100))

# 리스트 연산
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(squared)
print(filtered)

# 딕셔너리 연산 원라이너
data = [('a', 1), ('b', 2), ('c', 3)]
dict_from_tuples = dict(data)
reversed_dict = {v: k for k, v in dict_from_tuples.items()}
print(reversed_dict)

# 리스트 플래트닝
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)


# 조건부 딕셔너리 생성
user_data = {'name': 'John', 'age': None, 'email': 'john@example.com'}
clean_data = {k: v for k, v in user_data.items() if v is not None}
print(clean_data)

# 복잡한 데이터 변환
sales_data = [{'product': 'A', 'quantity': 10, 'price': 100},
             {'product': 'B', 'quantity': 5, 'price': 200}]
total_revenue = sum(item['quantity'] * item['price'] for item in sales_data)
print(total_revenue)

# 문자열 처리 원라이너
text = "Hello World Python Programming"
word_lengths = {word: len(word) for word in text.split()}
vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
print(word_lengths)
print(vowel_count)


# 리스트 중복 제거 (순서 유지)
items_with_duplicates = [1, 2, 2, 3, 1, 4, 3]
unique_items = list(dict.fromkeys(items_with_duplicates))
print(unique_items)

