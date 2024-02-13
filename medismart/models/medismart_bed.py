from odoo import fields, models


class medismartBed(models.Model):
    _name = "medismart.bed"
    _description = "medismart bed model"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Want to give bed number or sequence like the one we have in Sales Orders
    age = fields.Integer(required=True, string="Age (in years)", tracking=True)
    notes = fields.Text(string="Special Notes", tracking=True)
    type_of_bed = fields.Selection(
        string="Type of Bed",
        selection=[
            ("standard", "Standard"),
            ("deluxe", "Deluxe"),
            ("executive", "Executive"),
        ],
        required=True,
        default="standard",
        copy=False,
        tracking=True,
    )
    available = fields.Boolean(string="Available", default=True, tracking=True)
