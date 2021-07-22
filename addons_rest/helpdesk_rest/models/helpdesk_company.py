# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskCompany(models.Model):
    _name = 'helpdesk.company'
    _description = 'HelpdeskCompany'
    
    name = fields.Char()
