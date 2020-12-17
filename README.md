# Polinômio de Lagrange :abacus:

![](https://i.imgur.com/nh52VSj.png)

## Rodando o programa :keyboard::computer_mouse:

Para rodar o programa em sua máquina, clone o repositório do git por meio do `git clone <url>` ou simplesmente baixe o arquivo zip no botão abaixo do cabeçalho da página. Escolhido o repositório,
certifique-se que alguma versão do python esteja instalada, de preferência a versão 3.

### Sympy :thinking:

A lib `sympy` foi importada para permitir o uso de símbolos e a manipulação de expressões algébricas. Supondo que o seu diretório seja semelhante a isso

```
Microsoft Windows [versão 10.0.19041.685]
(c) 2020 Microsoft Corporation. Todos os direitos reservados.

C:\Users\username>
```

para incorporar o projeto na área de trabalho, digite

```
$ cd desktop & md project & cd project
```

Se fizer o download do arquivo zip e extraí-lo na pasta project é provável que outra pasta seja criada dentro dela. Se sim, acesse a pasta do projeto e rode

```python
$ pip install sympy
```

### Matplotlib :panda_face:

De forma análoga, no mesmo diretório, vá no prompt digite o comando abaixo e dê `<enter>`

```python
$ pip install matplotlib
```

Feito isso, as dependências devem ter sido satisfeitas e o programa está apto de ser executado. Para isso copie a linha abaixo e dê `<enter>` novamente

```python
$ python main.py
```

Caso o programa não rodar devidamente acesse via prompt o diretório onde o executável do python se encontra, porém como admnistrador. O prompt abrirá apresentando essa forma

```
Microsoft Windows [versão 10.0.19041.685]
(c) 2020 Microsoft Corporation. Todos os direitos reservados.

C:\WINDOWS\system32>
```

Vá para a raiz do disco `C:` digitando `cd.. + <enter>` duas vezes como segue

```
Microsoft Windows [versão 10.0.19041.685]
(c) 2020 Microsoft Corporation. Todos os direitos reservados.

C:\WINDOWS\system32>cd..

C:\Windows>cd..

C:\>
```

Na barra de pesquisa, aperte a tecla `Win` e pesquise por python. Feito isso, localize o arquivo `Python 3.<n>` e clique com o direito do mouse para abrir o local do arquivo. Copie o local do arquivo e atualize o gerenciador de pacotes do python por meio da linha

```python
$ python -m pip install –upgrade pip
```

Concluido o processo, acesse a pasta Scripts por meio do

```python
$ cd Scripts
```

e rode os comandos vistos anteriormente

```python
$ pip install matplotlib
$ pip install sympy
```

Aguarde a instalação e volte ao diretório do projeto onde se encontra o arquivo `main.py`. Novamente rode o comando

```python
$ python main.py
```

## :relaxed: Executando :computer:
Algo semelhante a isso deve aparecer

```python
C:\Users\renan\Desktop\ms211>python main.py
Coordenadas (Duplo <enter> finaliza o input)
x y
```

Para cada linha coloque uma coordenada com as posições x e y separadas somente pelo caractere espaço. A cada nova coordenada deve ser dado `<enter>` após passar a posição de y. O uso do duplo `<enter>` faz o programa avançar para a próxima etapa da entrada, onde será fornecido o grau do polinômio a ser interpolado. Nesse caso, para abranger os oito pontos da entrada optou-se pelo grau equivalente para que todos os pontos compusessem a curva ajustada como segue

```python
Coordenadas (Duplo <enter> finaliza o input)
x y
-3 -1
-2 0
-1 .5
0 .2
1 .6
2 2
3 2.3
4 2.5
5 1.2

Grau (De 1 a 8): 8
```

Após dar `<enter>` é pedido o valor do `xk` para o qual será calculado o valor do polinômio ajustado a partir do conjunto de pontos passado. Aqui será passado o valor `1.2` por conveniência

```python
Coordenadas (Duplo <enter> finaliza o input)
x y
-3 -1
-2 0
-1 .5
0 .2
1 .6
2 2
3 2.3
4 2.5
5 1.2

Grau (De 1 a 8): 8
xk = 1.2
```

Ao dar `<enter>` temos como saída,

```python
Para xk = 1.2 => P(x) = 0.857091891199999 # P(x) com x = xk
P(x) = -0.000560515873015875*x**8 + 0.00321428571428568*x**7 + 0.0103472222222222*x**6 - 0.0625000000000002*x**5 - 0.0899652777777776*x**4 + 0.395*x**3 + 0.430178571428572*x**2 - 0.285714285714286*x + 0.2 # Polinômio interpolado pelo método de Lagrange
```

a imagem da curva interpolada e os pontos passados

<p align="center">
    <img width="50%" src="https://i.imgur.com/UoXcoQy.png" />
</p>

