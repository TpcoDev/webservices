# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'
    
    id_usercore_tecnico = fields.Integer()
