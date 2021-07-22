# -*- coding: utf-8 -*-

from odoo import fields, models, api


class HelpdeskCategory(models.Model):
    _name = 'helpdesk.category'
    _description = 'HelpdeskCategory'
    
    name = fields.Char()
