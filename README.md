# Computer Security - Vigenere Cipher

Trabalho 1 do Curso de Segurança Computacional com cifrador/decifrador de cifra de Vigenère

## 🚧 STATUS DO PROJETO
- [x] Cifrador
- [x] Decifrador com chave
- [x] Decifrador sem chave
- [ ] Relatório

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

### Comando de registro (-r)
- '-user' [username]
- '-pswd' [password]
- '-email' [email]

Exemplo (projeto):
```
dotnet run -- -r -user MateusCavalcanti -email mat.fcavalcanti@gmail.com -pswd m1a2t3c4a5v6
``` 

### Comando de job (-j)
- '-user' [username]
- '-pswd' [password]

Exemplo (projeto):
```
dotnet run -- -j -user MateusCavalcanti -pswd m1a2t3c4a5v6
```

#### OBSERVAÇÕES
- As flags de tipo de execução (-r e -j) devem ser passadas como primeiro argumento
- As flags de parâmetro (-usr, -pasw e -email) podem ser passadas em qualquer ordem, mas seguidas pelos respectivos argumentos

Exemplo (projeto):
```
dotnet run -- -j -user MateusCavalcanti -pswd m1a2t3c4a5v6 
```
ou
```
dotnet run -- -j -pswd m1a2t3c4a5v6 -user MateusCavalcanti
```
 

## 💜 ???
```
???
```

## 💡 Testes
???
