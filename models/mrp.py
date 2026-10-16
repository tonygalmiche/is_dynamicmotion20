# -*- coding: utf-8 -*-
import string
from odoo import models,fields,api  # type: ignore
import re
from datetime import timedelta

class mrp_production(models.Model):
    _inherit = "mrp.production"

    date_deadline     = fields.Datetime(string="Date limite", readonly=False) # Rendre le champ existant modifiable
    origin            = fields.Char(tracking=True)      # Ajout de la tracabilité
    is_sale_id        = fields.Many2one('sale.order', string="Commande", compute='_compute_is_sale_id', store=True, readonly=True)

    is_date_livraison = fields.Date("Date livraison") 
    is_date_planifiee = fields.Datetime("Date planifiée modifiable", compute='_compute_is_date_planifiee', store=True, readonly=False) 
    is_duree          = fields.Float(string='Durée', default=4)
    # Fin du calendrier : date_delay (durée) n'existe plus en v20, le calendrier n'accepte que date_stop
    is_date_fin       = fields.Datetime("Date de fin planifiée", compute='_compute_is_date_fin', inverse='_inverse_is_date_fin', store=True)


    @api.depends('date_start')
    def _compute_is_date_planifiee(self):
        for obj in self:
            obj.is_date_planifiee = obj.date_start


    @api.depends('is_date_planifiee', 'is_duree')
    def _compute_is_date_fin(self):
        for obj in self:
            date_fin = False
            if obj.is_date_planifiee:
                date_fin = obj.is_date_planifiee + timedelta(hours=obj.is_duree)
            obj.is_date_fin = date_fin


    def _inverse_is_date_fin(self):
        # Redimensionnement de l'OF dans le calendrier => nouvelle durée
        for obj in self:
            if obj.is_date_planifiee and obj.is_date_fin:
                obj.is_duree = (obj.is_date_fin - obj.is_date_planifiee).total_seconds() / 3600


    @api.depends('origin')
    def _compute_is_sale_id(self):
        for obj in self:
            #** Recherche de la commande à partir du champ 'origin' ***********
            sale_name = False
            origin = obj.origin
            if origin:
                # Suppression de l'espace entre PO et les chiffres
                chaine_sans_espace = re.sub(r'PO\s+(\d+)', r'PO\1', origin) 
                # Extraction de la chaîne commençant par PO et les chiffres
                match = re.search(r'PO\d+', chaine_sans_espace)
                if match:
                    sale_name = match.group()
            #******************************************************************

            #** Recherche de la commande **************************************
            sale_id = False
            if sale_name:
                sale = self.env['sale.order'].search([('name', '=', sale_name)], limit=1)
                sale_id = sale.id if sale else False
            obj.is_sale_id = sale_id
