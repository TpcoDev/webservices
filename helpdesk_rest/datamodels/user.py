# -*- coding: utf-8 -*-

from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class UserInfo(Datamodel):
    _name = "user.info"
    _inherit = 'base.info'