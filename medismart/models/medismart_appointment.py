from odoo import api, fields, models
from datetime import timedelta


class medismartAppointment(models.Model):
    _name = "medismart.appointment"
    _description = "medismart appointment model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "start_time desc"

    sequence = fields.Char(
        "Appointment Reference",
        required=True,
        index=True,
        copy=False,
        readonly=True,
        default="New",
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
    start_time = fields.Datetime(
        default=fields.Datetime.now(), string="Start Time", tracking=True
    )
    end_time = fields.Datetime(
        string="End Time",
        compute="_compute_end_time",
        inverse="_set_appointment_period",
        store=True,
    )
    appointment_period = fields.Integer(
        string="Appointment Period",
        default=20,
        store=True,
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
            ("cancel", "Cancelled"),
        ],
        required=True,
        default="draft",
        tracking=True,
        group_expand="_read_group_appointment_ids",
    )
    appointment_note = fields.Text(string="Note")

    # constraints
    _sql_constraints = [
        (
            "check_appointment_period",
            "CHECK(appointment_period<=60 AND appointment_period>0 )",
            "An appointment can not be set for less than 1 minute or more than 60 minutes",
        )
    ]

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

    @api.depends("start_time", "appointment_period")
    def _compute_end_time(self):
        for record in self:
            if record.start_time:
                record.end_time = record.start_time + timedelta(
                    minutes=record.appointment_period
                )
            else:
                record.end_time = False

    @api.depends("start_time", "end_time")
    def _set_appointment_period(self):
        for record in self:
            if record.start_time and record.end_time:
                record.appointment_period = (
                    record.end_time - record.start_time
                ).total_seconds() / 60

    @api.model
    def create(self, vals):
        vals["sequence"] = self.env["ir.sequence"].next_by_code(
            "medismart.appointment.sequence"
        )
        return super().create(vals)
