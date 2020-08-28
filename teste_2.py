
#!/usr/bin/env python3

import json
import re
import requests

def consulta(cep):
    cep = cep.replace('-', '')
    url = f'https://viacep.com.br/ws/{cep}/json/'
    headers = {'User-Agent': 'Autociencia/1.0'}
    resposta = requests.request('GET', url, headers=headers)
    conteudo = resposta.content.decode('utf-8')
    resposta.close()
    endereco = json.loads(conteudo)

    return endereco


def cep_valido(cep):
    return True if re.search(r'^(\d{5}-\d{3}|\d{8})$', cep) else False


def main():
    cep = ''

    
    print('\n Para finalizar o programa digite sair \n')
    
    while cep != 'sair':
        
        cep = input('CEP:')

        if cep != 'sair' :
            if len(cep) != 8 :
                print('\nO CEP deve ter 8 digitos \n')


        if cep_valido(cep):
 
            endereco = consulta(cep)
                
            if not endereco.get('erro'):
                print('\nCidade: %s - %s' % (endereco['localidade'], endereco['uf']) )
                print('Bairro:', endereco['bairro'])
                print('Logradouro:', endereco['logradouro'])
                print('CEP:', endereco['cep'])
                print('\n')

            else :
                print('\nValor de CEP invalido\n')

if __name__ == '__main__':
    main()
