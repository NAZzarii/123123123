# Завдання 1
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

sum_numbers = a + b + c
product_numbers = a * b * c

print("Сума чисел:", sum_numbers)
print("Добуток чисел:", product_numbers)

# Завдання 2
d1 = float(input("Введіть довжину першої діагоналі ромба: "))
d2 = float(input("Введіть довжину другої діагоналі ромба: "))

area = (d1 * d2) / 2

print("Площа ромба:", area)

# Завдання 3
salary = float(input("Введіть зарплату за місяць: "))
credit = float(input("Введіть суму місячного платежу за кредитом у банку: "))
utilities = float(input("Введіть заборгованість за комунальні послуги: "))

remaining = salary - credit - utilities
print("Сума, що залишиться після всіх виплат:", remaining)

# Завдання 4
distance = float(input("Введіть відстань у кілометрах: "))
fuel_consumption = float(input("Введіть витрату палива на 100 км: "))
fuel_price = float(input("Введіть ціну за літр бензину: "))

trip_cost = (distance / 100) * fuel_consumption * fuel_price
print("Вартість поїздки:", trip_cost)

# Завдання 5
res_cost = float(input("Введіть вартість рахунку: "))
people_count = int(input("Введіть кількість людей: "))
tea_cost = res_cost * 0.15
total_cost = res_cost + tea_cost
cost = total_cost / people_count
print("Кожен має заплатити:", cost)
# Завдання 6
rent_per_day = float(input("Введіть вартість оренди за день: "))
days = int(input("Введіть кількість днів оренди: "))
deposit = float(input("Введіть суму застави: "))

total_rent = rent_per_day * days
total_payment = total_rent + deposit
print("Загальна вартість оренди (з урахуванням застави):", total_payment)

amount_after_return = total_payment - deposit
print("Сума до сплати після повернення автомобіля (з урахуванням повернення застави):", amount_after_return)

rent_per_day_actual = total_rent / days
print("Вартість оренди за один день:", rent_per_day_actual)
