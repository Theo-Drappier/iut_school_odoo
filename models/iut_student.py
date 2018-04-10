# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class IutStudent(models.Model):

    # region Private attributes
    _name = 'iut.student'
    # endregion

    # region Declaration fields
    firstname = fields.Char(string='Firstname')

    lastname = fields.Char(string='Lastname')

    birthdate = fields.Date(string='Birth date')

    age = fields.Integer(string='Age', compute='_compute_age')

    class_id = fields.Many2one(string='Class', comodel_name='iut.class')
    # endregion

    # region Declaration Methods
    @api.depends('birthdate')
    def _compute_age(self):
        if self.birthdate:
            today = datetime.today()
            self.age = relativedelta(today, datetime.strptime(self.birthdate, '%Y-%m-%d')).years
    # endregion
