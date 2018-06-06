# -*- coding: utf-8 -*-
{
    "name": """Kosovo - base location data""",
    "summary": """Adds Kosovo cities""",
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
        "base_location",
    ],
    "external_dependencies": {
        "python": [],
        "bin": []
    },
    "data": [
        "data/res_country_state_data.xml",
        "data/res.better.zip.csv",
    ],
    "qweb": [],
    "demo": [],

    "auto_install": False,
    "installable": True,
}

