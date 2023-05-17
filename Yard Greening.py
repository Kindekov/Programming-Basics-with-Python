square_meters_for_greening = float(input())
price = 7.61 * square_meters_for_greening
discount = price * 0.18
final_price = price - discount
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')
