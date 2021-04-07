# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityStudent(models.Model):
     _name = 'university.student'

     f_name = fields.Char('First Name')
     l_name = fields.Char('Second Name')
     sexe = fields.Selection([('male','Male'), ('female', 'Female')])
     identity_cards = fields.Char('Identity Card')
     adress = fields.Text('Adress')
     birth_day = fields.Date('Birthday')
     inscription_date = fields.Datetime('Date of inscription')
     mail = fields.Char()
     phone = fields.Char()

     departement_id = fields.Many2one(comodel_name='university.departement')
     classrroom_id = fields.Many2one(comodel_name='university.classroom')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100