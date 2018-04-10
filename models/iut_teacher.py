# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IutTeacher(models.Model):

    # region Private attributes
    _name = 'iut.teacher'
    _inherit = 'res.partner'
    # endregion

    # region Declaration fields
    class_ids = fields.One2many(string='Class', comodel_name='iut.class', inverse_name='teacher_id')
    # endregion

    # region Methods
    @api.depends('is_company', 'parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        pass
    # endregion
