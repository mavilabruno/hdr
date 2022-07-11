# -*- coding: utf-8 -*-
{
    'name': "elearning private youtube video",

    'summary': """elearning private youtube video
    """,

    'description': """
       elearning private youtube video
    """,

    'author': 'David Montero Crespo',
    'license': 'AGPL-3',
    'category': 'Website',
    'version': '13.0',
'website': "https://softwareescarlata.com/",
    # any module necessary for this one to work correctly
    'depends': ['base','website_slides'],
    'images': ['static/description/imagen.jpg'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',



    ],
    "assets": {
        "web.assets_frontend": [
            "elearning_private_youtube_video/static/scss/style.scss",
            "elearning_private_youtube_video/static/js/slides_course_fullscreen_player_video.js",
            ],

    },

    'currency': 'EUR',
    'price': 25,
    # only loaded in demonstration mode

}