# -*- coding: utf-8 -*-
"""hw3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f7CxoEliUB3szBGdly3myaofl3_wImGN
"""

def calculate_price(rate, sale_price):
    return round(sale_price / (1 - rate / 100))

rate = int(input("할인율은? "))
price_a = int(input("A 상품의 할인된 가격은? "))
price_b = int(input("B 상품의 할인된 가격은? "))

original_a = calculate_price(rate, price_a)
original_b = calculate_price(rate, price_b)

print("A 상품의 정가는", original_a, "원")
print("B 상품의 정가는", original_b, "원")