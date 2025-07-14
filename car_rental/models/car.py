from odoo import models, fields

class CarRentalCar(models.Model):
    _name = 'car.rental.car'
    _description = 'Car Rental Vehicle'
    _rec_name = 'name'

    name = fields.Char(string='Car Name', required=True)
    brand = fields.Char(string='Brand')
    model = fields.Char(string='Model')
    year = fields.Integer(string='Year')
    price_per_day = fields.Float(string='Price per Day')
    available = fields.Boolean(string='Available', default=True)
