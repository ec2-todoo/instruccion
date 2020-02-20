# -*- coding: utf-8 -*-
# from odoo import http


# class Clase1(http.Controller):
#     @http.route('/clase1/clase1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clase1/clase1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clase1.listing', {
#             'root': '/clase1/clase1',
#             'objects': http.request.env['clase1.clase1'].search([]),
#         })

#     @http.route('/clase1/clase1/objects/<model("clase1.clase1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clase1.object', {
#             'object': obj
#         })
