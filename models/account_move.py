from odoo import fields, models ,api

class accountmove(models.Model):
    _inherit = 'account.move'


    def action_do_something(self):
        print(self,"sdklfjsdklfmsjdfghjklsfdgj")
        