# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutCourse(models.Model):

    # region Private attributes
    _name = 'iut.course'
    # endregion

    # region Declaration fields
    name = fields.Char('Name Course')
    schedule_ids = fields.One2many(
        string='Schedules',
        comodel_name='iut.schedule',
        inverse_name='course_id'
    )
    # endregion
