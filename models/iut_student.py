# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutStudent(models.Model):

    # region Private fields
    _name = 'iut.student'
    # endregion

    # region Public fields
    firstname = fields.Char(string='Firstname')

    lastname = fields.Char(string='Lastname')

    birthdate = fields.Date(string='Birth date')

    age = fields.Integer(string='Age', compute='_compute_age')

    class_id = fields.Many2one(string='Class', comodel_name='iut.class')
    # endregion
