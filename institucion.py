from openerp import models, fields, api

class institucion(models.Model):
    _name = 'cmstats.institucion'

    name = fields.Char(string='Institucion', required=True)
    description =fields.Text()
    modulo = fields.Many2one('cmstats.modulo', required=True)

    @api.onchange('modulo')
    def _onchange_institucion(self):
        if not self.name:
            self.name = self.modulo.name
