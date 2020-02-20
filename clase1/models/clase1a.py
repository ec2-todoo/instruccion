# -*- coding: utf-8 -*-

from odoo import models, fields


class clase1a(models.Model):
     _name = 'clase1a.clase1a'
     _description = 'clase1a.clase1a'

     nombre = fields.Char()
     valor = fields.Integer()
     monto = fields.Float(compute="_value_pc", store=True)
     descripcion = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
