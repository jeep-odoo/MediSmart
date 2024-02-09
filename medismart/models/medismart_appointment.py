from odoo import fields, models


class medismartAppointment(models.Model):
    _name = "medismart.appointment"
    _description = "medismart appointment model"

    #link with a patient
    #link with a doctor
    date = fields.Datetime(default=fields.Datetime.now(), string='Date')
    purpose = fields.Selection(
        string='Purpose',
        selection=[
            ('general_checkup', 'General Checkup'),
            ('accident', 'Accident'), 
            ('post_surgery_visit', 'Post Surgery Visit'), 
            ('pre_surgery_visit', 'Pre Surgery Visit'),
            ('surgery', 'Surgery')
        ],
        required=True,
        default='general_checkup'
    )
    status = fields.Selection(
        string='Status',
        selection=[
            ('upcoming', 'Upcoming'), 
            ('ongoing', 'Ongoing'), 
            ('completed', 'Completed'), 
            ('cancelled', 'Cancelled')
        ],
        required=True,
        default='upcoming'
    )
