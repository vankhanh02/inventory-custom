{
    'name': 'Stock Approval',
    'version': '1.1',
    'author': 'odoo user',
    'summary': 'Manage your stock and logistics activities',
    'website': 'https://www.odoo.com/app/inventory',
    'depends': ['base','sale_management','product','purchase','stock','mrp'],
    'data': [
        'security/security.xml',
        'views/product_views.xml',
        'views/sale_order_form_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}
