# -*- coding: utf-8 -*-
import hashlib
import random
import string
from datetime import datetime, timedelta

def generate_hash(tamanho=15):
    # Defina o tamanho do hash
    hash_size = tamanho
    # Crie uma string com todos os caracteres possíveis
    characters = string.ascii_lowercase + string.digits
    # Inicialize a variável hash
    hash_str = ""
    # Loop para gerar cada caractere do hash
    for _ in range(hash_size):
        # Escolha um caractere aleatório
        char = random.choice(characters)
        # Adicione o caractere ao hash
        hash_str += char
    return hash_str




def tres_horas_antes():
    # Obtém a data e hora atuais
    datahora_atual = datetime.now()

    # Subtrai 3 horas
    nova_datahora = datahora_atual - timedelta(hours=3)
    return nova_datahora
