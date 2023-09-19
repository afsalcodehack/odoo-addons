from odoo import api, fields, models, _, tools

class HospitalPatient(models.Model):
    # this will create new table 'hospital_patient' dot will replace
    # with underscore
    _name = "hospital.patient"
    _description = "patient records"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is child ?")
    notes = fields.Text(string="Notes")
    doc_remark = fields.Text(string="Doctor Remark")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender")
