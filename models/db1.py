# -*- coding: utf-8 -*-

# Define a tabela 'usuario_empresa'
db.define_table('registro_atividade',
                Field('empresa','reference empresa', writable=False, readable=False, label='Empresa'),
                Field('usuario', 'reference auth_user', writable=False, readable=False, label='Usuário'),
                Field('cliente', 'string', label='Cliente', requires=IS_UPPER(), writable=True, readable=True),
                Field('fone', 'string', label='Whatsapp', writable=False, readable=False),
                Field('hash_acesso', 'string', label='Numero da Análise', writable=False, readable=True),
                Field('data_inicial', 'datetime',label='Hora Inicial', writable=False, requires = IS_DATETIME(format=('(%H:%M:%S) de %d/%m/%Y'))),
                Field('data_final', 'datetime', label='Hora Final', writable=False, readable=False,requires = IS_DATETIME(format=('(%H:%M:%S) de %d/%m/%Y'))),
                Field('status', 'string', label='Status', writable=False, default="Recebimento da amostra"),
                Field('laudo', 'upload', writable=False, readable=False, autodelete=True, label='PDF Laudo'),
                Field('observacao', 'text', label='Observação', writable=True, readable=True),
                auth.signature)

db.registro_atividade.status.requires = IS_IN_SET(['Recebimento da amostra','Inicio da analise','Fim da analise', 'Laudo emitido'])
db.registro_atividade.id.writable=False
db.registro_atividade.id.readable=False
