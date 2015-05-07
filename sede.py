from openerp import models, fields, api

class sede(models.Model):
    _name = 'cmstats.sede'

    name = fields.Char(string='Nombre Corto', required=True)
    largename = fields.Char(string='Nombre')
    description = fields.Text()


