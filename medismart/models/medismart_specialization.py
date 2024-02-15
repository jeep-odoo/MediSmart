from odoo import fields, models


class medismartSpecialization(models.Model):
    _name = "medismart.specialization"
    _description = "medismart specialization model"

    name = fields.Char(required=True, string="Specialization")
   