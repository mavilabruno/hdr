# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import url_for
from werkzeug import urls
import logging



_logger = logging.getLogger(__name__)

class Slide(models.Model):
    _inherit = 'slide.slide'

    embed_code = fields.Html('Embed Code', readonly=True, compute='_compute_embed_code', sanitize=False)


    @api.depends('document_id', 'slide_type', 'mime_type')
    def _compute_embed_code(self):
        base_url = request and request.httprequest.url_root
        for record in self:
            if not base_url:
                base_url = record.get_base_url()
            if base_url[-1] == '/':
                base_url = base_url[:-1]
            if record.datas and (not record.document_id or record.slide_type in ['document', 'presentation']):
                slide_url = base_url + url_for('/slides/embed/%s?page=1' % record.id)
                record.embed_code = '<iframe src="%s" class="o_wslides_iframe_viewer" allowFullScreen="true" height="%s" width="%s" frameborder="0"></iframe>' % (slide_url, 315, 420)
            elif record.slide_type == 'video' and record.document_id:
                if not record.mime_type:
                    query = urls.url_parse(record.url).query
                    query = query + '&theme=light' if query else 'theme=light'
                    record.embed_code = '<iframe sandbox="allow-forms allow-scripts allow-pointer-lock allow-same-origin allow-top-navigation"  src="//www.youtube-nocookie.com/embed/%s?%s" allowFullScreen="true" frameborder="0"></iframe><div class="overlay"></div><div class="overlay4"></div><div class="overlay3"/></div>'% (record.document_id, query)
                else:
                    # embed google doc video
                    record.embed_code = '<iframe sandbox="allow-forms allow-scripts allow-pointer-lock allow-same-origin allow-top-navigation"  src="//drive.google.com/file/d/%s/preview" allowFullScreen="true" frameborder="0"></iframe><div class="overlay"></div><div class="overlay4"></div><div class="overlay3"></div>'% (record.document_id)
            else:
                record.embed_code = False