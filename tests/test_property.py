from odoo import fields
from odoo.tests.common import TransactionCase


class TestProperty(TransactionCase):
    def setUp(self):
        super().setUp()
        self.property_01_record = self.env["property"].create(
            {
                "name": "property 1000",
                "description": "property 1000 description",
                "postcode": "1010",
                "date_available": fields.Date.today(),
                "bedrooms": 10,
                "expected_price": 10000,
            }
        )

    def test_01_property_values(self):
        self.assertRecordValues(
            self.property_01_record,
            [
                {
                    "name": "property 1000",
                    "description": "property 1000 description",
                    "postcode": "1010",
                    "date_available": fields.Date.today(),
                    "bedrooms": 10,
                    "expected_price": 10000,
                }
            ],
        )



