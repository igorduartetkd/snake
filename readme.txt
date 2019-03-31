	Pré-requisitos para executar o jogo:

	- Python versão igual ou superior a 3.5
	- PyOpenGL

	Passos para executá-lo:
	1- Abra o terminal ou prompt de comandos no diretório raiz do jogo;
	2- Execute, com o python, o programa “play.py”. Exemplo: python3 play.py

	Jogabilidade:
	A cobra é movimentada pelas setas do teclado. A tecla de espaço coloca e retira o pause no jogo. Caso o jogador está na primeira tela, de apresentação, ou na tela de game over, a tecla espaço simboliza o clique no botão start ou restart que aparece na tela. A tecla ESC sai do jogo imediatamente quando pressionada.

	O jogo snake foi desenvolvido em python versão 3.5 utilizando os recursos da biblioteca PyOpenGL. O desenvolvimento foi orientado a objeto de acordo com o diagrama de classe desenvolvido com o nome “diagramaClasseSnake.pdf”.
O objeto Elemento foi criado para servir como estrutura elementar para a construção da cobra, do muro e da comida armazenando a cor, a posição, o lado do quadrado e a direção que está apontado para ser utilizado quando houver movimento.
	A classe Cobra armazena uma lista com os elementos que representam os gomos do corpo da cobra. A variável “comeu” é uma booleana apenas para indicar se a cobra comeu alguma comida no ciclo anterior. 
	A função de deslocamento não desloca cada gomo armazenado no corpo. Para resolver o problema de forma mais eficiente, a função deslocar() apenas cria um novo gomo que será a nova cabeça da cobra e, se a cobra não comeu no ciclo anterior, apaga  o primeiro gomo da lista, o qual representa o último gomo do rabo da cobra. Caso a cobra comeu  no ciclo anterior, então a variável “comeu” é zerada e não é deletado um gomo do rabo, fazendo com que a cobra cresça um gomo.
	Ainda na função deslocar, a criação da nova cabeça ocorre na direção da orientação da cabeça, que pode ser 0, 90, 180 ou 270 graus indicando, respectivamente, um deslocamento para a direita, cima, esquerda e baixo. Para converter o ângulo em direção, foi utilizado as funções seno e cosseno, em que seno do ângulo é a variação no eixo y e cosseno do ângulo a variação no eixo x. 
	A classe comida herda de Elemento e serve apenas para indicar onde haverá comida na tela.
	A classe muro possui uma lista de Elementos representando os tijolos do muro. Cada tijolo é um elemento e preenche toda a borda da tela. Na classe muro foi inserida a função checar_colisao(posição) que percorre os tijolos e verifica se existe tijolo naquela posição informada por parâmetro, retornando um booleano para indicar a colisão.
	E, por fim, a classe play que fica responsável por organizar todas as outras classes e realizar as operações com o PyOpenGL. A função clock() é a função principal que ficará em loop quando for realizado um glutPostRedisplay(). Ela consulta uma variável que armazena qual tela estará habilitada no momento, sendo 1 para representar a tela de início, 2 para representar a tela do jogo, 3 para representar a tela final de game over e 4 para representar a tela de pause.
	A função regras_jogo() implementa a ordem em que os testes ocorrem, primeiro testando a colisão com o próprio corpo, depois se deslocando e então testando a colisão com o muro e por fim testa se comeu algo e seta a taxa de atualização de acordo com o a pontuação do jogador armazenada em score.
