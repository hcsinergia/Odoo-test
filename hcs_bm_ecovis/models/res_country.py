from odoo import models, fields


class BM_Res_Country(models.Model):
    _inherit = "res.country"

    code_number = fields.Integer()


class BM_Res_Country_Location(models.Model):
    _name = "res.country.location"

    name = fields.Char(string='Nombre de la Localidad', required=True)
    code = fields.Char(string='Código de la Localidad', required=True)
    state_id = fields.Many2one(
        string='Departamento', comodel_name='res.country.state', required=True)

    _sql_constraints = [
        ('state_id_code_uniq', 'unique(state_id, code)',
         'El código del Localidad debe ser único por Departamento !')
    ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} ({})".format(
                record.name, record.state_id.country_id.code)))
        return result


class BM_Res_Country_Neighborhood(models.Model):
    _name = "res.country.neighborhood"

    name = fields.Char(string='Nombre del barrio', required=True)
    code = fields.Char(string='Código de barrio', required=True)
    location_id = fields.Many2one(
        string='Localidad', comodel_name='res.country.location', required=True)

    _sql_constraints = [
        ('location_id_code_uniq', 'unique (location_id, code)',
         'El código del barrio debe ser único por Localidad !')
    ]
