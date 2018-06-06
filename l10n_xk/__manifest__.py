# -*- coding: utf-8 -*-

{
    'name': 'Kosovo - Accounting',
    'version': '10.0.0.0.0',
    'category': 'Localization',
    'description': """
This is the base COA for Kosovo
===============================

- basic COA
- taxes
- Fiscal positions

    """,
    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_xk_coa_chart_data.xml',
        'data/account_account_template.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position.xml',
        'data/account_chart_template_data.yml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'website': 'www.dajmi5.com',
}
