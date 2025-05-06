from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    pdf_reordered = fields.Boolean(
        string="Reorder PDF with Attachments",
        help="Enable to generate the PDF in reordered format with attachments.",
    )

