from odoo import api, fields, models


class medismartAppointment(models.Model):
    _name = "medismart.appointment"
    _description = "medismart appointment model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "appointment_date desc"

    sequence = fields.Char(
        'Appointment Reference',
        required=True,
        index=True,
        copy=False,
        readonly=True,
        default='New'
    )

    patient_id = fields.Many2one("medismart.patient", string="Patient", required=True)
    appointment_tag_ids = fields.Many2many(
        "medismart.appointment.tag", string="What's wrong?", tracking=True
    )
    patient_phone = fields.Char(
        related="patient_id.phone", string="Phone", readonly=True
    )
    specialization_id = fields.Many2one(
        "medismart.specialization", string="Specialization", required=True
    )
    doctor_id = fields.Many2one(
        "medismart.doctor",
        string="Doctor",
        required=True,
        domain="[('specialization_id', '=', specialization_id)]",
    )
    appointment_date = fields.Datetime(
        default=fields.Datetime.now(), string="Date", tracking=True
    )
    purpose = fields.Selection(
        string="Purpose",
        selection=[
            ("general_checkup", "General Checkup"),
            ("follow_up_visit", "Follow-up Visit"),
            ("surgical_consultation", "Surgical Consultation"),
            ("maternity_care", "Maternity Care"),
            ("emergency_care", "Emergency Care"),
        ],
        required=True,
        default="general_checkup",
        tracking=True,
    )
    status = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Confirmed"),
            ("done", "Done"),
            ("cancel", "Canceled"),
        ],
        required=True,
        default="draft",
        tracking=True,
        group_expand="_read_group_appointment_ids",
    )
    appointment_note = fields.Text(string="Note")

    def action_confirm(self):
        for record in self:
            if not record.status == "cancel":
                record.status = "confirm"
                return True

    def action_done(self):
        for record in self:
            if not record.status == "cancel":
                record.status = "done"
                return True

    def action_cancel(self):
        for record in self:
            if not record.status == "done":
                record.status = "cancel"
                return True

    # For sequencing of status in kanban view and keeping a stage open even when there is no record in it
    @api.model
    def _read_group_appointment_ids(self, stage, domain, order):
        return [key for key, val in type(self).status.selection]

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('medismart.appointment.sequence')
        return super().create(vals)
