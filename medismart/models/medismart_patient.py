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
        selection=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        required=True,
        copy=False,
        tracking=True,
    )
    medical_history = fields.Text(string="Medical History", tracking=True)
    weight = fields.Float(string="Height(in cm)", tracking=True)
    height = fields.Float(string="Weight(in kg)", tracking=True)
    phone = fields.Char(string="Phone", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    is_admitted = fields.Boolean(string="Is Admitted ?")
    admission_date = fields.Date(
        default=fields.Date.today(), string="Admission Date", tracking=True
    )
    discharge_date = fields.Date(
        default=fields.Date.today() + relativedelta(days=3),
        string="Discharge Date",
        tracking=True,
    )
    last_visit_date = fields.Date(
        string="Last Visit Date"
    )  # want this to be set from appointment model . the latest appointment to be automatically populated here
