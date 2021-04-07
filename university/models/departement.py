# -*- coding: utf-8 -*-
from docutils.nodes import field_name
from odoo import models, fields, api


class UniversityDepartement(models.Model):
    _name = 'university.departement'

    name = fields.Char()
    code = fields.Char()

    professor_ids = fields.One2many(comodel_name='university.profesor', inverse_name='departement_id')
    subject_ids = fields.One2many(comodel_name='university.subject', inverse_name='departement_id')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100