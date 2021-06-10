import unittest
from src import utils, data


class UtilsTests(unittest.TestCase):
    def test_flatmap(self):
        arr = [[1, 2], [3, 4]]
        flattened = utils.flatmap(arr)
        self.assertSequenceEqual(flattened, [1, 2, 3, 4])

    def test_found_city(self):
        city_name = "Warszawa"
        index = utils.get_node_id_of_city_by_name(city_name)
        self.assertEqual(index, 9)

    def test_city_not_found(self):
        city_name = "Gdańsk"
        try:
            index = utils.get_node_id_of_city_by_name(city_name)
        except utils.CityNotFoundError:
            pass
        except:
            self.fail("Niewłaściwy wyjątek!")
        else:
            self.fail("Miasto nie powinno zostać znalezione!")

    def test_get_city_name_by_node_id(self):
        expected_city_name = "Warszawa"
        node_id = 9

        result = utils.get_city_name_by_node_id(node_id)

        self.assertEqual(result, expected_city_name)

    def test_get_city_name_by_node_id_fail_if_bad_id(self):
        node_id = len(data.cities)
        try:
            result = utils.get_city_name_by_node_id(node_id)
        except IndexError:
            pass
        except:
            self.fail("Niewłaściwy wyjątek!")
        else:
            self.fail("Miasto nie powinno zostać znalezione!")

    def test_print_path(self):
        expected_string = "{0} -> {1} -> {2}".format(
            data.cities[0],
            data.cities[1],
            data.cities[2]
        )
        path = [0, 1, 2]

        result = utils.print_path(path)

        self.assertEqual(result, expected_string)

    def test_print_empty_path(self):
        expected_string = ""
        path = []

        result = utils.print_path(path)

        self.assertEqual(result, expected_string)


if __name__ == '__main__':
    unittest.main()
