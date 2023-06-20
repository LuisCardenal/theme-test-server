# -*- coding: utf-8 -*-
{
    'name': 'Crear orden de fabricación desde POS',
    'version': '16.0.0.1',
    'category': 'MRP/Point of Sale',
    'summary': 'Crear orden de fabricación y pasar a estado de hecho desde POS para automatizar inventario',
    'description': '''
                    Crear orden de fabricación y pasar a estado de hecho desde POS para automatizar inventario    ''',
    'author': 'Kevin Portillo - Rocketters SV',
    'website': 'rocketters.com',
    'depends': ['point_of_sale', 'mrp'],
    'data': ['views/pos_config_view.xml'],
    'assets': {
        'point_of_sale.assets': [
            'create_mrp_order_from_pos/static/src/js/custome.js',
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
    'external_dependencies': {
    },
}
