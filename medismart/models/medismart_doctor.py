from odoo import fields, models


class medismartDoctor(models.Model):
    _name = "medismart.doctor"
    _description = "medismart doctor model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, string='Name', tracking=True)
    age = fields.Integer(required=True, string='Age (in years)',tracking=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        required=True,
        copy=False,
        tracking=True
    )
    experience = fields.Integer(string='Experience (in yrs)',tracking=True)
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email',tracking=True)
    specialization = fields.Char(string='Specialization',tracking=True)
