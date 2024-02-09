from odoo import fields, models


class medismartDoctor(models.Model):
    _name = "medismart.doctor"
    _description = "medismart doctor model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, string='Name')
    age = fields.Integer(required=True, string='Age (in years)')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        required=True,
        copy=False
    )
    experience = fields.Integer(string='Experience (in yrs)')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    specialization = fields.Char(string='Specialization')
