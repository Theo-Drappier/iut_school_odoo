# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutSchedule(models.Model):

    # region Private attributes
    _name = 'iut.schedule'
    # endregion

    # region Declaration fields
    date_start = fields.Datetime(string='Date start')

    date_end = fields.Datetime(string='Date end')

    room = fields.Char(string='Class room')

    class_id = fields.Many2one(string='Class', comodel_name='iut.class')

    course_id = fields.Many2one(string='Course', comodel_name='iut.course')
    # endregion
