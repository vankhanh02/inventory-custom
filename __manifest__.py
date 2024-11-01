{
    'name': 'Stock Approval',
    'version': '1.1',
    'summary': 'Manage your stock and logistics activities',
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['base','sale_management','product','purchase','stock','mrp'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/product_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
