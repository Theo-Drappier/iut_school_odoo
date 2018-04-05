# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutTeacher(models.Model):

    # region Private attributes
    _name = 'iut.teacher'
    _inherit = 'res.partner'
    # endregion

    # region Public attributes
    class_id = fields.Many2one(string='Class', comodel_name='iut.class')
    # endregion
