# -*- coding: utf-8 -*-
from docutils.nodes import field
from odoo import models, fields, api


class UniversityProfesor(models.Model):
     _name = 'university.profesor'

     f_name = fields.Char('First Name')
     l_name = fields.Char('Second Name')
     sexe = fields.Selection([('male','Male'), ('female', 'Female')])
     identity_cards = fields.Char('Identity Card')
     adress = fields.Text('Adress')
     birth_day = fields.Date('Birthday')
     start_date = fields.Datetime('Date of start')
     mail = fields.Char()
     phone = fields.Char()

     departement_id = fields.Many2one(comodel_name='university.departement')
     subject_id = fields.Many2one(comodel_name='university.subject')

     classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                      relation='prof_class_rel',
                                      column1='f_name',
                                      column2='name')


    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100