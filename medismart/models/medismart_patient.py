import re
from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class medismartPatient(models.Model):
    _name = "medismart.patient"
    _description = "medismart patient model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    phone_regex = re.compile(r"^[0-9]{10}$")
    email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    name = fields.Char(required=True, string="Name", tracking=True)
    patient_tag_ids = fields.Many2many(
        "medismart.patient.tag", string="Medical Condition", tracking=True
    )
    image = fields.Binary()
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
    notes = fields.Text(string="Additonal Notes", tracking=True)
    patient_appointment_ids = fields.One2many(
        "medismart.appointment", "patient_id", string=" "
    )

    @api.constrains("email")
    def _check_email_format(self):
        for doctor in self:
            if doctor.email and not re.match(doctor.email_regex, doctor.email):
                raise ValidationError("Invalid email address format.")

    @api.constrains("phone")  # Only doctor should access this
    def _check_phone_number(self):
        for doctor in self:
            if doctor.phone and not doctor.phone_regex.match(doctor.phone):
                raise ValidationError("Phone number must be exactly 10 digits.")
