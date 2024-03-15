# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Dhira',
    'version': '1',
    'category': 'Sales and Purchase Order',
    'summary': 'Technical Test Odoo PT. SAS Kreasindo',
    'description': """
    """,
    'depends': ['sale','purchase'],
    'data': ['views/sale_order_views.xml',
             'wizard/import_so_lines.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application':True,
    'auto_install': False,
    'license': 'LGPL-3',
}
