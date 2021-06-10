from src.data import cities
import copy


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


def get_city_name_by_node_id(node_id):
    return cities[node_id]


def print_path(node_list):
    if len(node_list) == 0:
        return ""

    temp_list = copy.deepcopy(node_list)
    path_str = get_city_name_by_node_id(temp_list.pop(0))

    while len(temp_list) > 0:
        path_str = path_str + " -> " + get_city_name_by_node_id(temp_list.pop(0))

    return path_str
