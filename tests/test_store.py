from services.Store.api_store import api_store


class TestStore:
    def test_get_inventory(self):
        api_store.get_info_about_inventory()

    def test_get_valid_item_inventory(self):
        api_store.get_info_about_item_by_valid_id(5)

    def test_get_invalid_item_inventory(self):
        api_store.get_info_about_item_by_invalid_id('str')

    def test_create_valid_order(self):
        api_store.create_order_valid()

    def test_create_order_with_empty_response_body(self):
        api_store.create_order_empty_response_body()

    def test_create_order_with_absent_response_body(self):
        api_store.create_order_absent_response_body()

    def test_delete_order(self):
        api_store.delete_order_valid()