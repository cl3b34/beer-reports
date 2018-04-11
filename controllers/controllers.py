# -*- coding: utf-8 -*-
from odoo import http

# class Fin-beer-reports(http.Controller):
#     @http.route('/fin-beer-reports/fin-beer-reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fin-beer-reports/fin-beer-reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fin-beer-reports.listing', {
#             'root': '/fin-beer-reports/fin-beer-reports',
#             'objects': http.request.env['fin-beer-reports.fin-beer-reports'].search([]),
#         })

#     @http.route('/fin-beer-reports/fin-beer-reports/objects/<model("fin-beer-reports.fin-beer-reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fin-beer-reports.object', {
#             'object': obj
#         })