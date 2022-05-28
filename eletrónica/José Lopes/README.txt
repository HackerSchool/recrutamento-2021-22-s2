Boas, daqui José Lopes
Antes de mais espero que esteja tudo bem convosco.


Bem vindos ao meu projeto eletrónica.
O cerne do projeto é um ecrã no qual dou display de vários estados que podem ser controlados por 2 botões.
Para avançar de estado clicar nos dois botões ao mesmo tempo.
(Botão 1 - Esquerda; Botão 2 - Direita)

1- Time main:
  Bt1 - cycle:
    Horas e minutos;
    Segundos;
    Dia e Mês;
    Ano;
  Bt2 - regressar às Horas e minutos

2 - Time Setup:
  Vai esperar que o programa em processing envie os dados horários corretos.

3 - StopWatch:
  Bt1 - start/Stop
  Bt2 - Reset

3 - Sensor de Distância:
  Mostra a distância no ecrã, em centimetros.

4 - Instrumento Musical:
  Mostra um inteiro correspondente a uma nota, sendo 1 = A(440Hz), 12 = A(880Hz) (e todas as outras no meio);
  O intervalo entre notas é 4 cm.

Para o Futuro:

  - Mudar o timbre do Instrumento com um botão;
  - Play/stop o Instrumento com um botão;
  - Corrigir bug no StopWatch que faz com que o time inicial nao dê reset;
