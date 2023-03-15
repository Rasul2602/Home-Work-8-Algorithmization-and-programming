#1

countries = {
    "Россия": {"столица": "Москва", "часть света": "Европа", "население": 144.5, "площадь": 17125},
    "Франция": {"столица": "Париж", "часть света": "Европа", "население": 66.99, "площадь": 643},
    "Германия": {"столица": "Берлин", "часть света": "Европа", "население": 83.1, "площадь": 357},
    "Индия": {"столица": "Нью-Дели", "часть света": "Азия", "население": 1380, "площадь": 3287},
    "Китай": {"столица": "Пекин", "часть света": "Азия", "население": 1393, "площадь": 9597},
    "Япония": {"столица": "Токио", "часть света": "Азия", "население": 126.8, "площадь": 377},
}




country = input("Введите название государства: ")
if country in countries:
    capital = countries[country]["столица"]
    print(f"Столица государства {country} - {capital}")
else:
    print("Государство не найдено в базе данных.")

    
#2


capital = input("Введите название столицы: ")

for country in countries:
    if countries[country]["столица"] == capital:
        print("Столица", country)
        break
else:
    print("Столица не найдена.")
    
    
#3


country = input("Введите название государства: ")
if country in countries:
    print("Столица:", countries[country]["столица"])
    print("Часть света:", countries[country]["часть света"])
    print("Население (млн чел.):", countries[country]["население"])
    print("Площадь территории (тыс. кв. км):", countries[country]["площадь"])
else:
    print("Государство не найдено.")
    
#4


region = input("Введите часть света: ")


countries_in_region = []


for country, data in countries.items():
    if data["часть света"] == region:
        countries_in_region.append(country)


print(countries_in_region)

#5


for country, data in countries.items():
    density = data["население"] / data["площадь"] * 1000
    print(f"Плотность населения в {country}: {density:.2f} тыс. чел. на 1 кв. км")
    
#6
def count_countries_by_continent(countries, continent):
    count = 0
    for country in countries:
        if countries[country]["часть света"] == continent:
            count += 1
    return count

region = input("Введите часть света: ")
print(count_countries_by_continent(countries, region))

