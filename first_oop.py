# Создаем класс Bus
class Bus:

    # создаем атрибуты класса
    name = "Ikarus"
    make = "ZAZ"
    model = 1992

    # создаем методы класса
    def start(self):
        print ("Заводим двигатель")

    def stop(self):
        print ("Отключаем двигатель")

    def go_to_star(self):
        print("dyr dyr dyr dyr.....yuuuuuhu")


# Создаем объект класса Bus под названием bus_a
bus_a = Bus()

# Создаем объект класса Car под названием bus_b
bus_b = Bus()


print(bus_b.name)
