from odoo import fields, models
from dateutil.relativedelta import relativedelta


class medismartPatient(models.Model):
    _name = "medismart.patient"
    _description = "medismart patient model"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(required=True, string='Name')
    age = fields.Integer(required=True, string='Age (in years)')
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        required=True,
        copy=False
    )
    medical_history = fields.Text(string='')
    weight = fields.Float(string ='Height(in cm)')
    height = fields.Float(string='Weight(in kg)')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    admission_date = fields.Date(default=fields.Date.today(), string='Admission Date')
    discharge_date = fields.Date(default=fields.Date.today() + relativedelta(days=3), string='Discharge Date')
