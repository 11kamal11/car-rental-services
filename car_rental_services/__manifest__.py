{
    'name': 'Car Rental Services',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Simple car rental management',
    'description': 'A simple module to manage car rentals',
    'author': 'Your Name',
    'website': 'https://github.com/11kamal11/car-rental-services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
