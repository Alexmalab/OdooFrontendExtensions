# Author: Alexandre Ma <a1exma@hotmail.com>
# Copyright 2024 Alexandre Ma <a1exma@hotmail.com>.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# Monkey Patching
from odoo.tools import mail
mail.safe_attrs = mail.safe_attrs | frozenset(['data-oe-action-id', 'data-oe-view-id'])
