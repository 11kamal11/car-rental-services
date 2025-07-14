from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CarRentalCar(models.Model):
    _name = 'car.rental.car'
    _description = 'Car Rental'
    _rec_name = 'name'

    name = fields.Char(string='Car Name', required=True)
    model = fields.Char(string='Model')
    price_per_day = fields.Float(string='Price per Day')
    is_available = fields.Boolean(string='Is Available', default=True)
    image_1920 = fields.Image(string='Image')
    category_id = fields.Many2one('car.rental.category', string='Category')
    description = fields.Text(string='Description')
    license_plate = fields.Char(string='License Plate')
    color = fields.Char(string='Color')

class CarRentalCategory(models.Model):
    _name = 'car.rental.category'
    _description = 'Car Rental Category'
    _rec_name = 'name'

    name = fields.Char(string='Category Name', required=True)

class CarRentalBooking(models.Model):
    _name = 'car.rental.booking'
    _description = 'Car Rental Booking'
    _rec_name = 'name'

    name = fields.Char(string='Customer Name', required=True)
    car_id = fields.Many2one('car.rental.car', string='Car', required=True)
    customer_id = fields.Many2one('car.rental.customer', string='Customer')
    rental_date = fields.Date(string='Rental Date', required=True)
    return_date = fields.Date(string='Return Date')
    total_amount = fields.Float(string='Total Amount')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft', string='Status')

    @api.constrains('car_id', 'rental_date')
    def _check_availability(self):
        for booking in self:
            if booking.rental_date:
                conflicting_bookings = self.search([
                    ('car_id', '=', booking.car_id.id),
                    ('rental_date', '=', booking.rental_date),
                    ('id', '!=', booking.id),
                    ('state', '!=', 'cancelled'),
                ])
                if conflicting_bookings:
                    raise ValidationError("This car is already booked for the selected date.")

class CarRentalCustomer(models.Model):
    _name = 'car.rental.customer'
    _description = 'Car Rental Customer'
    _rec_name = 'name'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
