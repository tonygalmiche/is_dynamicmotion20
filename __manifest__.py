# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo 20 pour Dynamic Motion',
    'version'  : '20.0.0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',
    'description': """
InfoSaône - Module Odoo 20 pour Dynamic Motion
===================================================
Reprise d'is_dynamicmotion (Odoo 16).
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale_management',
        'sale_stock',   # sale_line_id sur stock.move
        'mrp',          # mrp.production
    ],
    'data' : [
        "views/sale_order_view.xml",
        "views/stock_picking_view.xml",
        "views/mrp_view.xml",
        # Migration v20 : rapports désactivés pour installer d'abord les modèles et les vues
        # "report/report_deliveryslip.xml",
        # "report/report_etiquette_colis.xml",
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
    'license': 'LGPL-3',
}

