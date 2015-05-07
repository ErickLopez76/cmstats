from openerp import models, fields, api

class det(models.Model):
    _name       = 'cmstats.det'

    institucion = fields.Many2one('cmstats.institucion')
    servicios   = fields.Integer()
    stat     = fields.Many2one('cmstats.statistic')

    #statistic = fields.Many2one('cmstatistic.statistic', required=True)

