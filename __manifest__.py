# -*- coding: utf-8 -*-
{
    'name': "Manage College",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Théo DRAPPIER",
    'website': "http://www.theodrappier.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/iut_class_views.xml',
        'views/iut_schedule_views.xml',
        'views/iut_course_views.xml',
        'views/iut_student_views.xml',
        'views/iut_teacher_views.xml',
        'views/menu.xml'
        # 'security/tdsimodel_security.xml',
        # 'views/menu.xml',
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
