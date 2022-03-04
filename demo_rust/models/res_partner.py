from odoo import models
from odoo.exceptions import UserError
import string_sum


class ResPartner(models.Model):
    _inherit = "res.partner"


    def test_string_sum_rust(self):
        sum_string = string_sum.sum_as_string(5, 25)
        raise UserError(f"The sum of 5 and 25 is {sum_string}")

