class Building:
    className = 'Здание'  
    objectsCount = 0

    def __init__(self, area, cost_per_sqm, residents_count):
        self._area = area  
        self._cost_per_sqm = cost_per_sqm  
        self._residents_count = residents_count  
        Building.objectsCount += 1

    # Метод 1: Рассчитать общую стоимость
    def calculate_total_cost(self):
        total_cost = self._area * self._cost_per_sqm
        print(f'Общая стоимость {self.className.lower()}: {total_cost:.2f} руб.')


class CountryHouse(Building):
    className = 'Деревенский дом'

    def __init__(self, area, cost_per_sqm, residents_count, garden_area):
        super().__init__(area, cost_per_sqm, residents_count)
        self._garden_area = garden_area  

    # Метод 2: Соотношение стоимости к числу проживающих
    def cost_to_residents_ratio(self):
        total_cost = self._area * self._cost_per_sqm
        if self._residents_count > 0:
            ratio = total_cost / self._residents_count
            print(f'Соотношение стоимости {self.className.lower()} к числу проживающих: {ratio:.2f} руб./чел.')
        else:
            print('Число проживающих должно быть больше нуля!')


class ApartmentBuilding(Building):
    className = 'Многоквартирный городской дом'

    def __init__(self, area, cost_per_sqm, residents_count, apartments_count):
        super().__init__(area, cost_per_sqm, residents_count)
        self._apartments_count = apartments_count  

    # Метод 2: Соотношение стоимости к числу проживающих
    def cost_to_residents_ratio(self):
        total_cost = self._area * self._cost_per_sqm
        if self._residents_count > 0:
            ratio = total_cost / self._residents_count
            print(f'Соотношение стоимости {self.className.lower()} к числу проживающих: {ratio:.2f} руб./чел.')
        else:
            print('Число проживающих должно быть больше нуля!')



country_house = CountryHouse(200, 30000, 5, 100)
country_house.calculate_total_cost()
country_house.cost_to_residents_ratio()

apartment_building = ApartmentBuilding(1000, 70000, 100, 50)
apartment_building.calculate_total_cost()
apartment_building.cost_to_residents_ratio()