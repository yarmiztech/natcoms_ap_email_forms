from odoo import fields, models, api, _
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang, format_date, get_lang

from uuid import uuid4
import qrcode
import base64
import logging
from odoo.addons import decimal_precision as dp

from lxml import etree

from odoo import fields, models
import requests
import json
from datetime import datetime, date
import convert_numbers

import ast
import base64
import datetime
import logging
import psycopg2
import smtplib
import threading
import re

from collections import defaultdict

from odoo import _, api, fields, models
from odoo import tools
from odoo.addons.base.models.ir_mail_server import MailDeliveryException

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    so_number = fields.Char(string='SO Number')
    customer_po = fields.Char(string='Customer PO Number')
    contact = fields.Char(string='Contact Eng')
    contact_address = fields.Char(string='Contact Address')
    datetime_field = fields.Datetime(string="Create Date", default=lambda self: fields.Datetime.now())
    decoded_data = fields.Char('Decoded Data')
    ubl_preview = fields.Integer(string="Test")
    debit_note = fields.Boolean(default=False)
    credit_note = fields.Boolean(default=False)
    qr_image = fields.Binary(string="QR Image")
    uuid = fields.Char('UUID', size=50, index=True, default=lambda self: str(uuid4()), copy=False)
    a_total_amount = fields.Char(string="A Total Value")
    a_net_amount = fields.Char(string="A Net Value")
    a_vat_value = fields.Char(string="A VAT Value")
    a_net_with_value = fields.Char(string="A NET WITH Value")