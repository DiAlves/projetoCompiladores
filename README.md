# ProjetoCompiladores

Projeto realizado para a cadeira de Compiladores. O projeto em questão trata-se de uma DSL (Domain Specific Language) capaz de gerar uma 
imagem contendo a rede de petri (onde os lugares é especificado por letra e os eventos por número) informada na entrada pelo usuário. Este projeto foi feito nas linguagens de programação JAVA (usada na
etapa em que é feito a avaliação e a compilação da expressão informada pelo usuário) e Python (usada para gerar a imagem da rede da petri,
de acordo com a expressão compilada).


<h1>Exemplo de execução</h1>

- Entrada do usuário:
      <p><i>A liga B se 1; B liga 2; 2 liga C;</i></p>

- Expressão compilada:
    <p><i> A->1->B<br />
           B->2<br />
           2->C </i></p>
           
- Imagem gerada: ![imgResult](https://user-images.githubusercontent.com/39803350/72008174-02814000-3232-11ea-8226-edd0bfdca679.png)
