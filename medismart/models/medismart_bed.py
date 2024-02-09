from odoo import fields, models


class medismartBed(models.Model):
    _name = "medismart.bed"
    _description = "medismart bed model"

    
    # Want to give bed number or sequence like the one we have in Sales Orders
    age = fields.Integer(required=True, string='Age (in years)')
    notes = fields.Text(string='Special Notes')
    type_of_bed = fields.Selection(
        string='Type of Bed',
        selection=[('standard', 'Standard'), ('deluxe', 'Deluxe'), ('executive', 'Executive')],
        required=True,
        default='standard',
        copy=False)
    available = fields.Boolean(string='Available',default=True)
