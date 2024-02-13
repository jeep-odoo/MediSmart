from odoo import fields, models


class medismartDoctor(models.Model):
    _name = "medismart.doctor"
    _description = "medismart doctor model"
    _inherit = ["mail.thread", "mail.activity.mixin"]

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
    specialization = fields.Selection(
        string="Specialization",
        selection=[
            ("general_practitioner", "General Practitioner"),
            ("internal_medicine", "Internal Medicine"),
            ("pediatrics", "Pediatrics"),
            ("obstetrics_gynecology", "Obstetrics and Gynecology"),
            ("cardiology", "Cardiology"),
            ("orthopedics", "Orthopedics"),
            ("dermatology", "Dermatology"),
            ("ophthalmology", "Ophthalmology"),
            ("neurology", "Neurology"),
            ("psychiatry", "Psychiatry"),
            ("surgery", "Surgery"),
            ("oncology", "Oncology"),
            ("endocrinology", "Endocrinology"),
            ("pulmonology", "Pulmonology"),
            ("urology", "Urology"),
        ],
        tracking=True,
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
