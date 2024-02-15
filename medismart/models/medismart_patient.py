from odoo import fields, models
from dateutil.relativedelta import relativedelta


class medismartPatient(models.Model):
    _name = "medismart.patient"
    _description = "medismart patient model"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, string="Name", tracking=True)
    age = fields.Integer(required=True, string="Age (in years)", tracking=True)
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        copy=False,
        tracking=True,
    )
    address = fields.Char(string="Address", copy=False, tracking=True)
    phone = fields.Char(string="Phone", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    notes = fields.Text(
        string="Additonal Notes", tracking=True
    )  # Only doctor should access this
    patient_appointment_ids = fields.One2many("medismart.appointment","patient_id", string=" " )
