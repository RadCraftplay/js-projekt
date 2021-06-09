from src.data import cities


class CityNotFoundError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Nie znaleziono miasta o nazwie " + self.name


def flatmap(array):
    ret_val = []

    for top_element in array:
        for lower_element in top_element:
            ret_val.append(lower_element)

    return ret_val


def get_node_id_of_city_by_name(city_name):
    for index, name in enumerate(cities):
        if name == city_name:
            return index
    raise CityNotFoundError(city_name)