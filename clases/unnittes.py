import unittest
import requests
import json


class TestFakeStore(unittest.TestCase):
    
    def setUp(self):
        self.BASE_URL = 'https://fakestoreapi.com'
        self.headers =   {'Content-Type': 'application/json'}

    
    def test_post_fake_api(self) -> None:
        post_product = '/products'
        data = {
                'id': 1,
                'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
                'price': 109.95, 'description': 'Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday',
                'category': "men's clothing", 'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg',
                'rating': {'rate': 3.9, 'count': 120}
                }
        res = requests.post(url=f'{self.BASE_URL}{post_product}', headers=self.headers, data=json.dumps(data, indent=4))
        # Assert
        print(res.status_code)
        print(res.json())
        self.assertEqual(res.status_code, 200)
        # probar que el articulo existe

        id = '/1'
        new_product = self.test_specific_product(id)
        print(new_product)
        self.assertEqual(data, new_product)
    
    def test_get_all_products(self) -> None:
        get_product = '/products'
        res = requests.get(url=f'{self.BASE_URL}{get_product}', headers=self.headers)
        #print(res.status_code, res.json())
        self.assertEqual(res.status_code, 200)
    
    def test_specific_product(self, id='/1') -> dict:
        get_product = '/products'
        res = requests.get(url=f'{self.BASE_URL}{get_product}{id}', headers=self.headers)
        self.assertEqual(res.status_code, 200)
        return res.json()


if __name__ == '__main__':
    unittest.main()

        
        
        

