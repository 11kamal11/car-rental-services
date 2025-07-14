{
    'name': 'Car Rental Services',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Manage car rentals including customers and bookings',
    'description': 'A comprehensive module to manage car rentals, customers, and bookings',
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
