# -*- coding: utf-8 -*-

from odoo import fields, models, api


class EmailCC(models.Model):
    _name = 'helpdesk.email.cc'
    
    name = fields.Char(string='Email')


class HeldeskTicketType(models.Model):
    _inherit = 'helpdesk.ticket.type'
    
    helpdesk_category_id = fields.Many2one(
        comodel_name='helpdesk.category',
        string='Helpdesk Category',
        required=False)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    
    helpdesk_branch_office_id = fields.Many2one(
        related='partner_id.helpdesk_branch_office_id',
        comodel_name='helpdesk.branch.office',
        string='Helpdesk Branch Office',
        required=False)
    
    helpdesk_company_id = fields.Many2one(
        related='partner_id.helpdesk_company_id',
        comodel_name='helpdesk.company',
        string='Helpdesk Company',
        required=False)
    
    helpdesk_category_id = fields.Many2one(
        related='ticket_type_id.helpdesk_category_id',
        comodel_name='helpdesk.category',
        string='Helpdesk Category',
        required=False)
    
    ticket_type_id = fields.Many2one('helpdesk.ticket.type', string="Ticket Type",
                                     domain="[('helpdesk_category_id', '=', helpdesk_category_id)]")
    numticket_UserCore = fields.Integer()
    center_cost = fields.Char(related='partner_id.center_cost')
    anexo = fields.Char(related='partner_id.anexo')
    email_cc_ids = fields.Many2many(comodel_name='helpdesk.email.cc')
