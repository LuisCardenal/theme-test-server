# -*- coding: utf-8 -*-


from odoo import _, api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"


    create_mrp_order = fields.Boolean("Crear orden MRP", help="Permite crear una orden de producción MRP", default=True)
    is_done = fields.Boolean("Estado Hecho Orden MRP", help="Permite dejar la orden en estado 'hecho' ", default=True)