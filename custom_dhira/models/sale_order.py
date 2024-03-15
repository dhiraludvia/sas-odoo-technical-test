# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    request_vendor = fields.Many2one('res.partner', string='Request Vendor')
    no_kontrak = fields.Char(string='NO Kontrak')
    with_po = fields.Boolean(string='With PO')
    purchase_ids = fields.One2many('purchase.order', 'partner_id', string='Purchase Order Lines')
    
    @api.onchange('purchase_ids')
    def create_po(self):
        vals = {
            'partner_id':self.request_vendor.id
        }
        self.env['purchase.order'].create(vals)
    
    def action_confirm(self):
        if self.env['no_kontrak'].search([('id','=',record.id)]):
            raise Warning("You can't have the same No Kontrak!")
        
