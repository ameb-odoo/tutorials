{
    "name": "Estate Management",
    "version": "1.0",
    "category": "Real Estate",
    "summary": "Manage Estate Properties, Leases, and More",
    "author": "Odoo",
    "website": "www.odoo.com",
    "license": "OEEL-1",
    "data": [
        # Views and menus
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        # Security
        "security/ir.model.access.csv",
    ],
    "images": ["static/description/icon.png"],
    "application": True,  # Whether this module is an application (will show on the main screen)
}
