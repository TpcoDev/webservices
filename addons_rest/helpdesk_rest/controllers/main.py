# -*- coding: utf-8 -*-

from odoo.addons.base_rest.controllers import main


class PrivateApiController(main.RestController):
    _root_path = "/helpdesk_rest/private/"
    _collection_name = "helpdesk.rest.private.services"
    _default_auth = "user"
