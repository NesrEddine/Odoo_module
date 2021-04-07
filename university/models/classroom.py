# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityClassroom(models.Model):
     _name = 'university.classroom'

     classrroom_name = fields.Char(string='name')
     code = fields.Char()

     student_ids = fields.One2many(comodel_name='university.student', inverse_name='classrroom_id')

     professor_ids = fields.Many2many(comodel_name='university.profesor',
                                      relation='class_prof_rel',
                                      column1='name',
                                      column2='f_name')

     subject_ids = fields.Many2many(comodel_name='university.subject',
                                      relation='class_subject_rel',
                                      column1='classrroom_name',
                                      column2='name')

     num_prof = fields.Integer(string='Number of prof', compute='comp_prof')
     num_student = fields.Integer(string='Number of student', compute='comp_st')
     num_subject = fields.Integer(string='Number of subject', compute='comp_sub')

     def comp_prof(self):
         self.num_prof = len(self.professor_ids)

     def comp_st(self):
         self.num_student = len(self.student_ids)

     def comp_sub(self):
         self.num_subject = len(self.subject_ids)

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100