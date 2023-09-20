# Copyright 2023 Jaime Millán <manuelcalero@xtendoo.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    def _message_get_suggested_recipients(self):
        recipients = super(HelpdeskTicket, self)._message_get_suggested_recipients()
        try:
            for ticket in self:
                if ticket.partner_id:
                    ticket._message_add_suggested_recipient(recipients, ticket.partner_id.email, ticket.partner_id.id)

                    if ticket.partner_id.parent_id:
                        ticket._message_add_suggested_recipient(
                            recipients, ticket.partner_id.parent_id.email, ticket.partner_id.parent_id.id)
        except:
            pass
        return recipients
