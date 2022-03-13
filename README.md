# Computer Security - Vigenere Cipher

Trabalho 1 do Curso de Segurança Computacional com cifrador/decifrador de cifra de Vigenère

## 🚧 STATUS DO PROJETO
- [x] Cifrador
- [x] Decifrador com chave
- [x] Decifrador sem chave
- [x] Relatório

## ⚙️ Primeiros Passos

Para executar o projeto é interessante ter python instalado:

- [VSCode: Ambiente recomendado para executar o projeto em Python](https://code.visualstudio.com/download)
- [Download versão mais recente Python](https://www.python.org/downloads/)

## 🚀 Sobre o projeto
### Parte I - cifrador/decifrador: 
O cifrador recebe uma senha e uma mensagem que é cifrada segundo a cifra de Vigenère,
gerando um criptograma, enquanto o decifrador recebe uma senha e um criptograma que é
decifrado segundo a cifra de Vigenère, recuperando uma mensagem.

### Parte II - ataque de recuperação de senha por análise de frequência: 
Serão fornecidas duas mensagens cifradas (uma em português e outra em inglês) com senhas
diferentes. Cada uma das mensagens deve ser utilizada para recuperar a senha geradora do
keystream usado na cifração e então decifradas.

Para as frequências das letras foram usadas: https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras 


## 🛠 Instruções para execução do projeto

### Cifragem de mensagem (-cif)
- -msg='[mensagem]' (Mensagem a ser cifrada)
- -key='[chave]' (Chave utilizada para cifrar a mensagem)

Exemplo:
```
python3 trab1.py -cif -msg='mensagemplaintext' -key'chave123'
``` 

### Decifragem de mensagem (-decif)
- -msg='[mensagem]' (Mensagem a ser decifrada)
- -key='[chave]' (Chave utilizada para decifrar a mensagem criptografada)

Exemplo:
```
python3 trab1.py -decif -msg='mensagemcifrada' -key'chave123'
```

### Quebra de cifra (-quebra)

- -msg='[mensagem]' (Mensagem cifrada com uma chave desconhecida)
- -lang='[us|br]' (br - Frequências relativas à língua portuguesa)
                  (us - Frequências relativas à língua inglesa)
Exemplo :
```
python3 trab1.py -quebra -msg='mensagemcifrada' -lang='br'
```

#### OBSERVAÇÕES
- Os algoritmos implementados no trabalho só funcionam considerando mensagens que apresentam caracteres no intervalo a-z (alfabeto minúsculo).

## 💜 Algoritmos
### Cifragem
- Recebe uma mensagem ```plain text``` e a chave que deve ser utilizada para a cifragem.
- Aplica o algoritmo da cifra de Vigenère:
    - Para cada letra da mensagem, é aplicado a cifragem de césar considerando a letra correspondente da chave, ou seja, 
      
      ```c_i = p_i + k_i (mod 26)```.

### Decifragem
- Recebe uma mensagem cifrada e a chave que deve ser utilizada para a decifragem.
- Aplica o algoritmo de decifram de Vigenère:
    - Para cada letra da mensagem, é aplicado a decifragem de césar considerando a letra correspondente da chave, ou seja, 
      
      ```p_i = c_i - k_i + 26 (mod 26)```.

### Quebra de chave
- Recebe uma mensagem cifrada e a informação sobre o "idioma" da mensagem ```plain text```.
- Aplica o algoritmo de quebra de cifra:
    - Primeiramente, aplica o método de índice de coincidência em diferentes tamanhos de chave (2 a 20) para encontrar o possível candidato de melhor tamanho (tamanho N). O "melhor tamanho" é escolhido considerando aquele que apresenta o índice de coincidência mais próximo do índice referente à frequência do alfabeto do idioma fornecido (br ou us).
    - Considerando o melhor candidato possível para o tamanho da chave (tamanho N), é aplicado do método X² em N pedaços da mensagem cifrada para se obter cada letra da possível chave. O método X² consiste em, para cada um dos 26 deslocamentos ('shift') do pedaço da mensagem, é calculado o valor X² de cada deslocamento. Para o menor valor de X² encontrado, pega a letra correspondente ao deslocamento em questão. 
    - Decifra a mensagem utilizando a possível chave encontrada.

## 💡 Testes
???
