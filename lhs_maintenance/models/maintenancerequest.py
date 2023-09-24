from odoo import fields, models


class MaintenanceRequest(models.Model):
    _name = "maintenance.request"
    _description = "maintenance request"

    priority = fields.Selection([('low','Low'),('medium','Medium'),('urgent','Urgent')], string = "Priority")
    requestorName = fields.Char(string="Requestor Name", required=True)
    requestorMobile = fields.Char(string="Requestor Mobile", required=False)
    location = fields.Selection([('dafna','dafna'),('lusail','lusail'),('pearl','pearl')], string = "Location")
    typeOfWork = fields.Selection([('General', 'General'), ('electrical', 'electrical'), ('civil', 'civil')], string="Type Of Work")
    equipment = fields.Selection([('ac', 'ac'), ('chiller', 'chiller'), ('laptop', 'laptop')], string="Equipment")
    documents = fields.Binary(string="Attachment")

