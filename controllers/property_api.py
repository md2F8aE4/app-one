import json
from odoo import http
from odoo.http import request


class PropertyApi(http.Controller):

    def _create_property(self):
        try:
            vals = json.loads(request.httprequest.data.decode() or "{}")
        except json.JSONDecodeError:
            return request.make_json_response(
                {"message": "Invalid JSON body"}, status=400,
            )

        if not vals.get("name"):
            return request.make_json_response(
                {"message": "name is required"}, status=400,
            )

        try:
            res = request.env["property"].sudo().create(vals)
            return request.make_json_response(
                {
                    "message": "property has been created successfully",
                    "id": res.id,
                    "name": res.name,
                },
                status=201,
            )
        except Exception as error:
            return request.make_json_response({"message": str(error)}, status=400)

    @http.route("/v1/property", methods=["POST"], type="http", auth="none", csrf=False)
    def post_property(self):
        return self._create_property()

    @http.route("/v1/property/json", methods=["POST"], type="http", auth="none", csrf=False)
    def post_property_json(self):
        return self._create_property()

    @http.route("/v1/property/<int:property_id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def update_property(self, property_id):
        try:
            prop = request.env["property"].sudo().search([("id", "=", property_id)], limit=1)
            if not prop:
                return request.make_json_response(
                    {"message": "id does not exist"},
                    status=404,
                )
            vals = json.loads(request.httprequest.data.decode() or "{}")
            prop.write(vals)
            return request.make_json_response(
                {
                    "message": "property has been updated successfully",
                    "id": prop.id,
                    "name": prop.name,
                },
                status=200,
            )
        except Exception as error:
            return request.make_json_response({"message": str(error)}, status=400)

    @http.route("/v1/property/<int:property_id>", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property(self, property_id):
        try:
            prop = request.env["property"].sudo().search([("id", "=", property_id)], limit=1)
            if not prop:
                return request.make_json_response(
                    {"message": "there is no property matching this id"}, status=404,
                )
            return request.make_json_response(
                {"id": prop.id, "name": prop.name, "ref": prop.ref}, status=200
            )
        except Exception as error:
            return request.make_json_response({"message": str(error)}, status=400)

    @http.route("/v1/property/<int:property_id>", methods=["DELETE"], type="http", auth="none", csrf=False)
    def delete_property(self, property_id):
        try:
            prop = request.env["property"].sudo().search([("id", "=", property_id)], limit=1)
            if not prop:
                return request.make_json_response(
                    {"error": "id not exist"}, status=404
                )
            prop.unlink()
            return request.make_json_response(
                {"message": "property has been deleted successfully"}, status=200
            )
        except Exception as error:
            return request.make_json_response({"error": str(error)}, status=400)

    @http.route("/v1/properties", methods=["GET"], type="http", auth="none", csrf=False)
    def get_property_list(self):
        try:
            property_ids = request.env["property"].sudo().search([])
            data = [{"id": prop.id, "name": prop.name, "ref": prop.ref} for prop in property_ids]
            return request.make_json_response(data, status=200)
        except Exception as error:
            return request.make_json_response({"message": str(error)}, status=400)
