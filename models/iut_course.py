# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutCourse(models.Model):

    # region Private fields
    _name = 'iut.course'
    # endregion

    # region Public fields
    name = fields.Char('Name Course')
    # endregion
