# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2019-TODAY OPeru.
#    Author      :  Grupo Odoo S.A.C. (<http://www.operu.pe>)
#
#    This program is copyright property of the author mentioned above.
#    You can`t redistribute it and/or modify it.
#
###############################################################################

from . import models
from . import wizard

from odoo import api, SUPERUSER_ID

def _create_shop(cr, registry):
    """ This hook is used to add a shop on existing companies
    when module l10n_pe is installed.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    company_ids = env['res.company'].search([])
    company_with_shop = env['einvoice.shop'].search([]).mapped('company_id')
    company_without_shop = company_ids - company_with_shop
    for company in company_without_shop:
        shop_id = env['l10n_pe_edi.shop'].create({
            'name': '%s %s' % (company.name, company.id),
            'code': '0000',
            'company_id': company.id,
            'partner_id': company.partner_id.id,
        })
    