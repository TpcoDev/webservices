# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskBranchOffice(models.Model):
    _name = 'helpdesk.branch.office'
    _description = 'HelpdeskBranchOffice'
    
    name = fields.Char()
