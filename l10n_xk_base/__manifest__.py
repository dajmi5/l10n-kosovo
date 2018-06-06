# -*- coding: utf-8 -*-
{
    "name": """Kosovo - base data""",
    "summary": """Adds Kosovo base data""",
    "category": "Localisation",
    "images": [],
    "version": "1.0.0",
    "application": False,

    "author": "DAJ MI 5!",
    "support": "support@odoo-hrvatska.org",
    "website": "http://odoo-hrvatska.org",
    "licence": "LGPL-3",
    #"price" : 20.00,   #-> only if module if sold!
    #"currency": "EUR",

    "depends": [
        "base",
        "base_iban"
    ],
    "external_dependencies": {
        "python": [],
        "bin": []
    },
    "data": [
        "data/res_bank_data.xml",
        "views/res_company_view.xml",
        "views/res_partner_view.xml",
    ],
    "qweb": [],
    "demo": [],

    "auto_install": False,
    "installable": True,
}

