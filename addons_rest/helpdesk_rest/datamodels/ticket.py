from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
from odoo.addons.datamodel.fields import NestedModel


class TicketInfo(Datamodel):
    _name = "helpdesk.ticket.info"
    _inherit = "base.info"
    
    description = fields.String(required=True, allow_none=False)
    user_id = NestedModel("user.info")
    partner_id = NestedModel("partner.info")
