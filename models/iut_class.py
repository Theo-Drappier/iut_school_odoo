# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutClass(models.Model):

    # region Private fields
    _name = 'iut.class'
    # endregion

    # region Public fields
    name = fields.Char(string='Class Name')
    level = fields.Selection(
        string='Level',
        selection=[
            ('seconde', '2nde'),
            ('premiere', '1ere'),
            ('terminale', 'Term')
        ]
    )

    teacher_id = fields.Many2one(
        string='Teacher',
        comodel_name='iut.teacher'
    )

    student_ids = fields.One2many(
        string='Students',
        comodel_name='iut.student',
        inverse_name='class_id'
    )

    student_nb = fields.Integer(
        string='Number of students',
        compute='_compute_nb_students'
    )
    # endregion

    # region Methods
    @api.depends('student_ids')
    def _compute_nb_students(self):
        self.student_nb = len(self.student_ids)
    # endregion
