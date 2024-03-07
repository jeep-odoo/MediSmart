from odoo import api, fields, models


class medismartDoctor(models.Model):
    _name = "medismart.doctor"
    _description = "medismart doctor model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(required=True, string="Name", tracking=True, copy=False)
    age = fields.Integer(required=True, string="Age (in years)", tracking=True)
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female"), ("other", "Other")],
        required=True,
        copy=False,
        tracking=True,
    )
    experience = fields.Integer(string="Experience (in yrs)", tracking=True)
    image = fields.Binary()
    phone = fields.Char(
        string="Phone",
        tracking=True,
        required=True,
    )
    email = fields.Char(
        string="Email",
        tracking=True,
        required=True,
    )
    specialization_id = fields.Many2one(
        "medismart.specialization", string="Specialization", tracking=True
    )
    consultation_fee = fields.Float(string="Consultation Fee", tracking=True)
    availability = fields.Selection(
        string="Availability",
        selection=[
            ("full_time", "Full Time"),
            ("part_time", "Part Time"),
            ("on_call", "On Call"),
        ],
        default="full_time",
        required=True,
        tracking=True,
    )
    joining_date = fields.Date(string="Joining Date", tracking=True)
    appointment_ids = fields.One2many(
        "medismart.appointment",
        "doctor_id",
        string="Appointments",
        domain=[("status", "=", "confirm")],
    )
    patient_ids = fields.Many2many(
        "medismart.patient",
        string="Patients",
        compute="_compute_patient_ids",
        store=True,
    )

    @api.depends("appointment_ids.patient_id")
    def _compute_patient_ids(self):
        for doctor in self:
            doctor.patient_ids = doctor.appointment_ids.mapped("patient_id")
