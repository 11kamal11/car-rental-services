{
    'name': 'Car Rental',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Simple Car Rental Management',
    'description': 'A simple module for managing car rentals',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
