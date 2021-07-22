# -*- coding: utf-8 -*-

from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class BaseInfo(Datamodel):
    _name = "base.info"
    
    id = fields.Integer(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
