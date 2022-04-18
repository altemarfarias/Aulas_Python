# Cores no terminal (ANSI escape sequence)
# \033[m
# \033[STYLE(comprtamento);TEXT(texto);BACK(background)m
# STYLE => 0 = (NANE) sem estilo nenhum;
# STYLE => 1 = (BOLD) negrito
# STYLE => 4 = (UNDERLINE) subliado
# STYLE => 7 = (NEGATIVA) inverte cores das letras e fundo
# TEXT - BACK  cor
# 30   - 30  = branco
# 31   - 31  = vermelho
# 32   - 32  = verde
# 33   - 33  = amarelo
# 34   - 34  = azul
# 35   - 35  = magenta
# 36   - 36  = ciano
# 37   - 37  = cinza
# Existe outra cores, para isso tem que usar outras biblioteca
print('\033[4;30;41mOlá Mundo\033[m!!!')
cores = {'branco_verde':'\33[30;32m', 'neutra':'\033[m'}
print('Altemar Carvalho de {}Farias{}.'
      .format(cores['branco_verde'], cores['neutra']))

