import unittest
from src import utils


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


if __name__ == '__main__':
    unittest.main()
