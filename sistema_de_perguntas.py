print()
print('Sistema desenvolvido para fazer um questionario!')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Pergunta 1? ',
        'respostas': {
            'a': 'Noruega',
            'b': 'Guatemala',
            'c': 'África do Sul',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Pergunta 2?',
        'respostas': {
            'a': 'Acho que Não',
            'b': 'Não Tenho Certeza',
            'c': 'Com certeza',
            'd': 'Sei lá'
        },
        'resposta_certa': 'd',
    
    },
    'Pergunta 3': {
        'pergunta': 'Pergunta 3? ',
        'respostas': {
            'a': 'Chuck Norris',
            'b': 'Marlon Brandon',
            'c': 'Marilyn Manson',
            'd': 'Anthony Hopkins'
        },
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Pergunta 4? ',
        'respostas': {
            'a': 'Não',
            'b': 'Certeza',
            'c': 'Com certeza',
            'd': 'Nenhuma das alternativas'
        },
        'resposta_certa': 'c',
    },
     'Pergunta 5': {
        'pergunta': 'Outra Pergunta? ',
        'respostas': {
            'a': 'A',
            'b': 'B',
            'c': 'C',
            'd': 'D'
        },
        'resposta_certa': 'd',
    }
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Parabéns!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('Tente Outra vez!!! Você ERROU!!!!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')
