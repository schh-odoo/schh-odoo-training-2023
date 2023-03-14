{
    'name': "Real Estate",
    'depends':['base'],
    'version': '1.0.0',
    'sequence': -100,
    'author': 'sankalp (schh)',
    'category': 'Management',
    'installable':True,
    'application':True,
    'license': 'LGPL-3',
    'summary': 'Application to manage your real estate business',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_offers_view.xml',
        'views/estate_property_type_view.xml',
        'views/res_users_views.xml',
        'views/estate_property_tags_view.xml',
        'views/estate_menus.xml',
        'data/master_data.xml'
    ],
    'demo':[
        'demo/demo_data.xml'
    ]
}