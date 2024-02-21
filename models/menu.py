# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations


if auth.user:
    response.menu = [
        (T('Usuarios'), False, URL('acs_usuario', 'index'), []),
        (T('Registros'), False, URL('acs_registro', 'index'), [])
    ]
else:
    response.menu = [
        (T('Home'), False, URL('default', 'index'), [])
    ]
