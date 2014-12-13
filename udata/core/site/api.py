# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from udata.api import api, API, fields

from .views import current_site

site_fields = api.model('Site', {
    'id': fields.String(description='The Site unique identifier', required=True),
    'title': fields.String(description='The site display title', required=True),
    'configs': fields.Raw(description='The associated configurations', default={}),
    'metrics': fields.Raw(description='The associated metrics', default={}),
})


@api.route('/site/', endpoint='site')
class SiteAPI(API):
    @api.doc(id='get_site')
    @api.marshal_list_with(site_fields)
    def get(self):
        '''List all scheduled jobs'''
        return current_site