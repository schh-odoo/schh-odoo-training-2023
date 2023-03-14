from odoo import fields,models

class EstateProperty(models.Model):
    _inherit="estate.property"

    def action_set_sold(self):
        vals={
            'partner_id':self.buyer.id,
            'name':self.name,
            'task_ids':[
                fields.Command.create({
                    "name":"Maintainence"
                })
            ]
        }
        self.env['project.project'].create(vals)
        return super(EstateProperty,self).action_set_sold()