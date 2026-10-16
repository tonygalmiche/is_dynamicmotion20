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

        # Applications utilisées en v16, à installer pour la reprise des données
        # (hors périmètre : feuilles de temps, présences, congés)
        'purchase_mrp',                 # achats (purchase, purchase_stock) liés à la fabrication
        'sale_purchase_stock',          # achats liés aux ventes
        'mrp_subcontracting_purchase',  # sous-traitance (1 nomenclature)
        'sale_crm',                     # CRM (128 pistes)
        'project_mrp',                  # projets (46) liés à la fabrication
        'project_purchase',             # projets liés aux achats
        'mrp_repair',                   # réparations (26)
        'stock_delivery',               # méthodes de livraison (5, sur 3 commandes)
        'hr',                           # employés (ordres de travail et temps passés des OF)
    ],
    'data' : [
        "security/res.groups.xml",
        "views/sale_order_view.xml",
        "views/stock_picking_view.xml",
        "views/mrp_view.xml",
        "views/menu.xml",
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

