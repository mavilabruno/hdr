# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SlidePartner(models.Model):
    _inherit = 'slide.slide.partner'

    slide_type = fields.Selection([
        ('infographic', 'Infographic'),
        ('webpage', 'Web Page'),
        ('presentation', 'Presentation'),
        ('document', 'Document'),
        ('video', 'Video'),
        ('quiz', "Quiz")],
        string='Type',  default='document',
        related='slide_id.slide_type',
        )




class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    slide_partner_ids_stadistic = fields.Many2many('slide.slide.partner', string='Student Data',compute='_compute_slide_partner_ids')
    completed_partner_statistics = fields.Boolean('Completed', compute='_compute_partner_statistics', compute_sudo=False)
    completion_partner_statistics = fields.Integer('Progress (%)', compute='_compute_partner_statistics', compute_sudo=False)

    def _compute_slide_partner_ids(self):
        active_ids = self.env.context.get('default_slide_partner_ids', False)
        if active_ids:
            self.slide_partner_ids_stadistic=self.env['slide.slide.partner'].sudo().search([('id', 'in',active_ids[0][2]),('channel_id','=',self.id)])
        else:
            self.slide_partner_ids_stadistic=False


    @api.depends('slide_partner_ids', 'total_slides')
    def _compute_partner_statistics(self):
        active_ids = self.env.context.get('default_partner_id', False)
        if active_ids:
            current_user_info = self.env['slide.channel.partner'].sudo().search(
                [('channel_id', 'in', self.ids), ('partner_id', '=', active_ids[0])]
            )
            mapped_data = dict((info.channel_id.id, (info.completed, info.completed_slides_count)) for info in current_user_info)
            for record in self:
                completed, completed_slides_count = mapped_data.get(record.id, (False, 0))
                record.completed_partner_statistics = completed
                record.completion_partner_statistics = 100.0 if completed else round(100.0 * completed_slides_count / (record.total_slides or 1))

