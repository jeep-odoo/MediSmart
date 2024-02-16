from odoo import fields, models
from random import randint


class medismartPatientTag(models.Model):
    _name = "medismart.patient.tag"
    _description = "Medismart patient tag model"

    name = fields.Char(required=True, string="Name")

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer("Color", default=_get_default_color)

    _sql_constraints = [
        ("name_unique", "unique(name)", "Patient Tag must be unique")
    ]
