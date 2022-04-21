# -*- coding: utf-8 -*-
{
    'name': "NATCOM AUTO FORM APRIL",
    'author':
        'Enzapps',
    'summary': """
This module is for creating api for Invoices.
""",

    'description': """
        This module consist of track page of cargo which extend the website.
        It consist of 2 tabs Brief and History
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['web','sale','purchase','base','account','account_invoice_ubl','natcom_dec_last','natcomjson','natcom_jan_pdf','natcoms_customers_apis_new','ubl_mail','natcoms_jan_mou'],
    "images": ['static/description/icon.png'],
    'data': [
              # 'security/ir.model.access.csv',
              # 'data/mail_template_data.xml',
              # 'data/sequence.xml',
              # 'views/auto_form.xml',
              # 'reports/reports_header_new_view.xml',
              'views/asserts.xml',
              'reports/reports_no_new_view.xml',
              'reports/reports.xml',
    ],
    'demo': [
    ],
    'css': ['static/css/report_styles.css'],
    'installable': True,
    'application': True,
}
