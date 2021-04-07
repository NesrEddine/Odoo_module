# -*- coding: utf-8 -*-
{
    'name': "University",

    'summary': """
        University system information""",

    'description': """
        University system information 
    """,

    'author': "Nasreddine Boudene",
    'website': "http://www.nesreddineboudene.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/subject_view.xml',
        'views/profesor_view.xml',
        'views/departement_view.xml',
        'views/classrroom_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'aplication':True,
    'auto_install':False,
}
