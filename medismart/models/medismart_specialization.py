from odoo import fields, models


class medismartSpecialization(models.Model):
    _name = "medismart.specialization"
    _description = "medismart specialization model"
    _order = "name"

    name = fields.Char(required=True, string="Specialization")
    doctor_ids = fields.One2many(
        "medismart.doctor", "specialization_id", string="Doctors"
    )

    _sql_constraints = [("name_unique", "unique(name)", "Patient Tag must be unique")]
