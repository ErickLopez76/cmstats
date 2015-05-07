from openerp import models, fields, api

class stat(models.Model):
    _name        = 'cmstats.stat'

    name         = fields.Date(default=fields.Date.today)
    sede         = fields.Many2one('cmstats.sede', required=True)
    nota         = fields.Text()
    nuevas       = fields.Integer(string='Nuevas')
    subsecuentes = fields.Integer(string='Subsecuentes')
    det          = fields.One2many('cmstats.det','stat')

#    statd   = fields.One2many('cmstatistic.servicios2', 'statistic')
