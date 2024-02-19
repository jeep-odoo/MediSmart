from odoo import fields, models
from random import randint


class medismartAppointmentTag(models.Model):
    _name = "medismart.appointment.tag"
    _description = "Medismart appointment tag model"
    _order = "name"


    name = fields.Char(required=True, string="Name")

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer("Color", default=_get_default_color)

    _sql_constraints = [
        ("name_unique", "unique(name)", "Tag must be unique")
    ]
