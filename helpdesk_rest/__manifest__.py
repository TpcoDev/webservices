# -*- coding: utf-8 -*-
{
    'name': "Helpdesk Rest",
    
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    
    'author': "EDDAI",
    'website': "http://www.yourcompany.com",
    "maintainers": ["adruban"],
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Helpdesk',
    'version': '12.0.0.1',
    
    # any module necessary for this one to work correctly
    'depends': ['contacts', 'helpdesk', 'base_rest', "base_rest_datamodel", "component"],
    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/helpdesk_ticket_type_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
    ],
    
}
