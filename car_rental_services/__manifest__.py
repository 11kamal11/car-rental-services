{
    'name': 'Car Rental Services',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Manage car rentals including customers and bookings',
    'description': 'A comprehensive module to manage car rentals, customers, and bookings',
    'author': 'Your Name',
    'website': 'https://github.com/11kamal11/car-rental-services',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
        'views/customer_views.xml',
        'views/rental_views.xml',
        'views/menu.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'car_rental_services/static/src/css/website_car_rental.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
