# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversitySubject(models.Model):
     _name = 'university.subject'

     name = fields.Char()
     code = fields.Char()

     departement_id = fields.Many2one(comodel_name='university.departement')

     professor_ids = fields.Many2many(comodel_name='university.profesor',
                                      relation='sub_prof_rel',
                                      column1='name',
                                      column2='f_name')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100