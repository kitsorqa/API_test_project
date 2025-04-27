import json
import logging
from typing import Optional

import pytest
import requests
from pydantic import ValidationError

from services.Store.endpoints import StoreEndpoints
from services.Store.models.model_Store import InventoryItemModel, CreatedOrderModel, DeletedOrderModel
from services.Store.payloads import StorePayloads

class ApiStore:
    def __init__(self):
        self._endpoints = StoreEndpoints()

    def get_info_about_inventory(self):
        response = requests.get(
            url=self._endpoints._get_inventory
        )
        assert response.status_code == 200, response.json()

    def get_info_about_item_by_valid_id(self, item_id: int):
        url = f"{self._endpoints._get_order_by_id}/{item_id}"
        response = requests.get(
            url=url
        )
        logging.info(response.text)
        assert response.status_code == 200, response.json()

    def get_info_about_item_by_invalid_id(self, item_id: str):
        url = f"{self._endpoints._get_order_by_id}/{item_id}"
        response = requests.get(
            url=url
        )
        with pytest.raises(ValidationError):
            model = InventoryItemModel(**response.json())
            pytest.fail("ValidationError не было вызвано, тест упал")

    def create_order_valid(self):
        payload = StorePayloads.create_order
        url = self._endpoints._create_order
        response = requests.post(
            url=url,
            json=payload
        )
        logging.info(response.text)
        model = CreatedOrderModel(**response.json())
        return model

    def create_order_empty_response_body(self):
        url = self._endpoints._create_order
        response = requests.post(
            url=url,
            json={}
        )
        model = CreatedOrderModel(**response.json())
        return model

    def create_order_absent_response_body(self):
        url = self._endpoints._create_order
        response = requests.post(
            url=url
        )
        with pytest.raises(ValidationError):
            model = CreatedOrderModel(**response.json())
            pytest.fail("ValidationError не сработал")

    def delete_order_valid(self):
        id = json.loads(self.create_order_valid().json())["id"]
        self.get_info_about_item_by_valid_id(id)
        url = f"{self._endpoints._delete_order_by_id}/{id}"
        response = requests.delete(
            url=url
        )
        self.get_info_about_inventory()
        model = DeletedOrderModel(**response.json())
        logging.info(response.text)
        assert response.status_code == 200, response.json()
        return model




api_store = ApiStore()
