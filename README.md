# Projeto IP: CroCIn Road

Inspirado em um dos maiores clássicos recentes da indústria de jogos *mobile*, o sistema interativo 'CroCIn Road' é uma releitura autoral, dotada de referências do cotidiano de estudantes do Centro de Informática da Universidade Federal de Pernambuco, cujo conceito reside em um jogo 2D, no estilo *arcade* e de perspectiva *top-down*, e desenvolvido como projeto de conclusão da disciplina de Introdução à Programação.

## Instruções de execução e jogabilidade

Para que seja possível a execução do jogo em seu sistema operacional, são necessários:

1. Instalação prévia do [Python](https://www.python.org/downloads/);
2. Instalação da biblioteca PyGame (executando o comando `pip install pygame` no terminal/prompt de comando da sua máquina);
3. Download e extração do .zip associado à branch 'main' do repositório desta página; e
4. Execução do arquivo *main.py*, no prompt de comando ou em seu editor de preferência.

Com o jogo em execução, é possível controlar a movimentação do personagem de duas maneiras: 

- Utilizando as setas ( ↑ ↓ ← → ); ou
- Usando o controle **WASD**.

É importante notar que o movimento do jogador é **linear** (por **toque**), ou seja, o personagem move-se apenas uma unidade de deslocamento por tecla pressionada.

## Integrantes da equipe e sua participação

- [Filipe Moreira (fmc)](https://github.com/filipecml) - Redação do *README.md*, implementação dos coletáveis, correção de bugs e ajustes de jogabilidade.
- [Getúlio Junqueira (gjql)](https://github.com/getuliojql) - 
- [João Guilherme Cavalcanti (jgrbc)](https://github.com/joaoguirbc) - Implementação e correções pontuais do cenário.
- [Kleberson Araújo (kab2)](https://github.com/KleberAraujoo) - 
- [Leonardo Brahim (lbt)](https://github.com/leonardobrahim) - 

## Organização do código

- *main.py* - Consiste no núcleo de toda a estruturação do sistema interativo, onde ocorrem a definição de variáveis de inicialização do programa, o instanciamento do módulo PyGame e de suas funções, bem como o controle do laço de repetição principal - responsável pelo processamento de eventos associados a objetos, cenário e personagem, e a continuidade ou quebra da execução do jogo.
- *settings.py* - Armazena constantes relativas às configurações da tela de display do jogo, da frequência de surgimento de carros, do tamanho e da posição inicial do personagem jogável no cenário.
- *personagem.py* - Contém a classe *Personagem*, que, por sua vez, engloba todos os atributos (velocidade, posição, vidas disponíveis, coletáveis recolhidos, etc.) e ações (movimento, desenho na tela e tratamento de eventos) do jogador.
- *cenario.py* - Envolve a classe *Cenário*, que instancia os sprites utilizados no ambiente ao fundo, e possui como única função o comportamento associado ao desenho das superfícies na tela.
- *car.py* - Contém a superclasse relativa ao tipo de objeto *Carro*, a qual estabelece relações de herança com as classes de cada tipo de carro, e instancia seus atributos (tamanho, variação de posição no eixo X, sprite) e comportamentos (desenho na tela, movimentação, verificação de colisão e de limites).
- *coletaveis.py* - Armazena também o tipo de objeto *Coletável*, seus atributos (posição, hitbox e sprite) e funções (desenho na tela e verificação de colisão).
- *imagens* - Pasta responsável por guardar todos os sprites desenvolvidos e utilizados durante o jogo.

## Bibliotecas e ferramentas utilizadas

De maneira evidente, [PyGame](https://www.pygame.org/) constituiu a principal biblioteca em Python usada no desenvolvimento desse sistema interativo, uma vez que ela nos permitiu uma implementação relativamente simplificada de diversas *features* de jogabilidade - registro das teclas pressionadas pelo usuário, criação da tela de display e das caixas de texto, desenho de objetos, verificação de *hitbox* e processamento de sprites. Além disso, utilizaram-se, ainda, algumas funções associadas às bibliotecas [Sys](https://docs.python.org/3/library/sys.html), [Os](https://docs.python.org/3/library/os.html) e [Random](https://docs.python.org/3/library/random.html), responsáveis pelo controle da execução do programa no sistema operacional, indicação de direcionamento de arquivos (carregamento dos sprites necessários) e geração de inteiros aleatórios (controle de fenômenos e eventos de natureza randômica), respectivamente.

Como ferramenta externa, nos valemos também da plataforma online [Piskel](https://www.piskelapp.com/), através da qual foram criados os sprites dos coletáveis, personagem, cenário e alguns dos demais objetos utilizados no jogo.
