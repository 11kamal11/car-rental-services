{
    'name': 'Car Rental',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Simple Car Rental Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
