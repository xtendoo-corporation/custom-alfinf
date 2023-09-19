# Copyright 2023 Jaime Millán <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProjectTaskLine(models.Model):
    _inherit = 'project.task.line'

    date_time_finish = fields.Datetime(
        string='Date Time Finish',
        readonly=False,
    )
