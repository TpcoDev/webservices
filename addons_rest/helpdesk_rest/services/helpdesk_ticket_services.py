# -*- coding: utf-8 -*-

import base64
from odoo.addons.base_rest import restapi
from odoo.addons.base_rest.components.service import to_bool, to_int
from odoo.addons.component.core import Component


class HelpdeskTicketService(Component):
    _inherit = "base.rest.service"
    _name = "helpdesk.ticket.service"
    _usage = "ticket"
    _collection = "helpdesk.rest.private.services"
    _description = """
            Helpdesk Ticket Services
            Access to the ticket services is only allowed to authenticated users.
            If you are not authenticated go to <a href='/web/login'>Login</a>
        """
    
    def get(self, _id):
        """
        Get ticket's informations
        """
        return self._to_json(self._get(_id))
    
    def search(self, name):
        """
        Searh ticket by name
        """
        tickets = self.env["helpdesk.ticket"].name_search(name)
        tickets = self.env["helpdesk.ticket"].browse([i[0] for i in tickets])
        rows = []
        res = {"count": len(tickets), "rows": rows}
        for ticket in tickets:
            rows.append(self._to_json(ticket))
        return res
    
    def create(self, **params):
        """
        Create a new ticket
        """
        response = {
            "idTicket": 0,
            "RespCode": 404,
            "RespMessage": 'Mensaje de error',
        }
        
        try:
            ticket = self.env["helpdesk.ticket"].create(self._prepare_params(params))
            
            if ticket:
                if params.get('archivo_adjunto', False):
                    attachment_id = self.env['ir.attachment'].create({
                        'name': 'Archivo adjunto',
                        'type': 'binary',
                        'datas': base64.b64decode(params['archivo_adjunto']),
                        'res_model': ticket._name,
                        'res_id': ticket.id
                    })
                
                response.update({
                    "idTicket": ticket.id,
                    "RespCode": 0,
                    "RespMessage": "Ticket se insertó correctamente.",
                })
        except Exception as ex:
            response['RespCode'] = int(ex.pgcode)
            response['RespMessage'] = ex.pgerror
        
        return response
    
    def update(self, _id, **params):
        """
        Update ticket informations
        """
        ticket = self._get(_id)
        ticket.write(self._prepare_params(params))
        return self._to_json(ticket)
    
    # The following method are 'private' and should be never never NEVER call
    # from the controller.
    
    def _get(self, _id):
        return self.env["helpdesk.ticket"].browse(_id)
    
    def _prepare_params(self, params):
        vals = {}
        partner = None
        user = None
        ticket_type = None
        Partner_obj = self.env['res.partner']
        Users_obj = self.env['res.users']
        Tickettype_obj = self.env['helpdesk.ticket.type']
        email_cc = []
        
        if params.get('id_usercore', False) and not partner:
            partner = Partner_obj.search([('id', '=', params['id_usercore'])])
        
        if params.get('rut', False) and not partner:
            partner = Partner_obj.search([('vat', '=', params['rut'])])
        
        if params.get('id_usercore_tecnico', False):
            user = Users_obj.search([('id', '=', params['id_usercore_tecnico'])])
        
        if params.get('tipoticket', False):
            ticket_type = Tickettype_obj.search([('name', '=', params['tipoticket'])])
        
        if not partner:
            Sucursal = self.env['helpdesk.branch.office'].search([('name', '=', params.get('sucursal'))])
            Empresa = self.env['helpdesk.company'].search([('name', '=', params.get('empresa'))])
            partner = Partner_obj.create({
                'name': params.get('nombre', ""),
                'vat': params.get('rut', ""),
                'function': params.get('cargo', ""),
                'email': params.get('correo', ""),
                'mobile': params.get('celular' ""),
                'center_cost': params.get('centro_costo', ""),
                'helpdesk_branch_office_id': Sucursal.id,
                'helpdesk_company_id': Empresa.id,
                'street': params.get('direccion_completa', ""),
            })
        
        if params.get('email_users_cc', False):
            emails = params['email_users_cc'].split(',')
            for email in emails:
                e = self.env['helpdesk.email.cc'].create({'name': email})
                email_cc.append(e.id)
        
        if params.get('asunto', False):
            vals['name'] = params['asunto']
        if params.get('descripcion', False):
            vals['description'] = params['descripcion']
        if params.get('numticket_UserCore', False):
            vals['numticket_UserCore'] = params['numticket_UserCore']
        
        if params.get('prioridad', False):
            vals['priority'] = str(params['prioridad'])
        if user:
            vals['user_id'] = user.id
        if partner:
            vals['partner_id'] = partner.id
        if ticket_type:
            vals['ticket_type_id'] = ticket_type.id
        if len(email_cc):
            vals['email_cc_ids'] = [(6, 0, email_cc)]
        
        return vals
    
    # Validator
    def _validator_return_get(self):
        res = self._validator_create()
        res.update({
            "idTicket": {"type": "integer", "required": True, "empty": False},
            "RespCode": {"type": "integer", "required": True, "empty": False},
            "RespMessage": {"type": "string", "required": True, "empty": False},
        })
        return res
    
    def _validator_search(self):
        return {"name": {"type": "string", "nullable": False, "required": True}}
    
    def _validator_create(self):
        res = {
            "name": {"type": "string", "required": False, "empty": False},
            "description": {"type": "string", "required": False, "empty": False},
            "priority": {"type": "string", "required": False, "empty": False},
            "id_usercore": {"type": "integer", "required": False, "empty": False},
            "rut": {"type": "string", "required": False, "empty": False},
            "nombre": {"type": "string", "required": False, "empty": False},
            "cargo": {"type": "string", "required": False, "empty": False},
            "correo": {"type": "string", "required": False, "empty": False},
            "celular": {"type": "string", "required": False, "empty": False},
            "id_usercore_tecnico": {"type": "integer", "required": False, "empty": False},
            "prioridad": {"type": "integer", "required": False, "empty": False},
            "tipoticket": {"type": "string", "required": False, "empty": False},
            "sucursal": {"type": "string", "required": False, "empty": False},
            "empresa": {"type": "string", "required": False, "empty": False},
            "asunto": {"type": "string", "required": False, "empty": False},
            "descripcion": {"type": "string", "required": False, "empty": False},
            "archivo_adjunto": {"type": "string", "required": False, "empty": False},
            "email_users_cc": {"type": "string", "required": False, "empty": False},
            "direccion_completa": {"type": "string", "required": False, "empty": False},
            "centro_costo": {"type": "string", "required": False, "empty": False},
            "numticket_UserCore": {"type": "integer", "required": False, "empty": False},
        }
        return res
    
    def _to_json(self, ticket):
        res = {
            "id": ticket.id,
            "nombre": ticket.name,
            "descripcion": ticket.description
        }
        
        return res
    
    def to_openapi(self):
        root = super(HelpdeskTicketService, self).to_openapi()
        root.update(
            {
                "components":
                    {
                        "securitySchemes": {
                            "BearerAuth": {
                                "type": "http",
                                "scheme": "bearer",
                                "bearerFormat": "JWT"
                            },
                            "ApiKeyAuth": {
                                "type": "apiKey",
                                "in": "header",
                                "name": "api_key",
                            },
                            "basicAuth": {
                                "type": "http",
                                "scheme": "basic",
                            }
                        }
                    },
                "security": [{
                    "BearerAuth": [],
                    "ApiKeyAuth": [],
                    "basicAuth": []
                }]
            })
        return root
