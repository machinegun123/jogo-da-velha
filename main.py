from random import randint
#1-pedra/ 2-Papel/3-Tesoura

traducao = {
  '1':'Pedra',
  '2':'Papel',
  '3':'Tesoura'
}

tabelaVitoria = {
  'Pedra':'Tesoura',
  'Papel':'Pedra',
  'Tesoura':'Papel'
}

def inicio():
  print('===============================')
  print('=====Pedra Papel e Tesoura=====')
  print('===============================')

  print('\ndigite: \n[1] Jogar\n[0] Sair')

  escolha = input('')

  if escolha == '1':
    return jogo()
  else:
    return sair()
    

def jogo():
    print('\nDigite: \n[1] Pedra\n[2] Papel\n[3]Tesoura')

    escolhaJogador = input('')
    escolhaComputador = str(randint(1,3))

  #traducao de numero para pedra papel ou tesoura
    escolhaJogador = traducao[escolhaJogador]
    escolhaComputador = traducao[escolhaComputador]

  #teste de vitoria
    if escolhaJogador == escolhaComputador:
      print('Empate!')
    elif tabelaVitoria[escolhaJogador] == escolhaComputador:
      print('você venceu!')
    else:
      print('você perdeu!')

      print(f'voê escolheu{escolhaJogador}')
      print(f'O seu oponente escolheu {escolhaComputador}\n')
      return jogarNovamente()


def jogarNovamente():
      escolha= input('Deseja Jogar Novamente?(S/N)').upper()

  if escolha =='S':
       return jogo()
    else:
       return sair()


def sair():
  print('obrigado por jogar!')
  return
inicio()
