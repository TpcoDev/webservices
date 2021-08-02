# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    id_usercore = fields.Char()
    
    helpdesk_branch_office_id = fields.Many2one(
        comodel_name='helpdesk.branch.office',
        string='Helpdesk Branch Office',
        required=False)
    
    helpdesk_company_id = fields.Many2one(
        comodel_name='helpdesk.company',
        string='Helpdesk Company',
        required=False)
    
    center_cost = fields.Char()
    anexo = fields.Char()
