from locust import FastHttpUser, task, TaskSet
from load_tests.common_utils.csv_reader import CSVReader
import random
import logging


class TestData:
    test_data = None


class InventoryAPI(TaskSet):

    def on_start(self):
        data = CSVReader.read_csv('/Users/riki.mondal/Desktop/Falcon/load_tests/inventory/inventory_test_data.csv', 'records')
        TestData.test_data = data


    @task
    def test_product_by_id(self):
        product_id = random.choice(TestData.test_data)
        response = self.client.get('/product/{id}'.format(id=product_id['product_id']), name="/product/{id}")
        logging.info("URL: {}, Status Code: {}".format(response.url, response.status_code))


class InventoryLoadTest(FastHttpUser):
    tasks = [InventoryAPI]