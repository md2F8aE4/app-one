from odoo import http
from odoo.http import request

class TestApi(http.Controller):
    @http.route("/api/test", type="http", auth="public", methods=["GET"], csrf=False)
    def test_endpoint(self, **kwargs):
        return request.make_json_response(
            {"message": "test endpoint is working"},
            status=200,
        )
