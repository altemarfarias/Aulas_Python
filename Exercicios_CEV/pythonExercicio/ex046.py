import emoji
from time import sleep
print('Começando agora a contagem regressiva!')
for cont in range(10, 0, -1):
    print('{}'.format(cont))
    sleep(1)
print(emoji.emojize('Agora! :boom:',  language='alias'))


