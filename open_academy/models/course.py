# -*- coding: utf-8 -*-

from odoo import models, fields

class openAcademyCourse(models.Model):
	_name = 'academy.course'
	_description = 'Open Academy Model for Course'

	name = fields.Char() # Integer()