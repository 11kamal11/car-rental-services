from odoo import models, fields

class CarRentalCar(models.Model):
    _name = 'car.rental.car'
    _description = 'Car Rental'

    name = fields.Char(string='Car Name', required=True)
    model = fields.Char(string='Model')
    price_per_day = fields.Float(string='Price per Day')
    is_available = fields.Boolean(string='Is Available', default=True)
