from openerp import models, fields, api

class modulo(models.Model):
    _name = 'cmstats.modulo'

    name = fields.Char(string='Modulo', required=True)
    description = fields.Text()
#    institucion  = fields.One2Many('cmstatistic.institucion', 'Modulo')
