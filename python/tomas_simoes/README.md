Vão precisar de criar uma base de dados local em mysql / mariadb para o programa funcionar.
Garantam que têm mysql / mariadb instalado, depois podem seguir estes comandos para criar a base de dados / tabela:

CREATE DATABASE logininfo;
CREATE TABLE credentials(number VARCHAR(9), hash VARCHAR(200), created DATE, salt VARCHAR(60), iterations VARCHAR(60));

Deverá haver um utilizador *root* com password *root* com acesso à database correspondente para o programa funcionar.

O programa depende também de uma api chamada [Twilio](https://www.twilio.com/docs/usage/api). Precisarão de uma conta para testar.
No ficheiro `main_login.py` existem duas variáveis que precisam de ser preenchidas com o SID e o token respetivamente.

O entry-point do projeto é `main_login.py` e basta correr:
`python3 main_login.py`


O programa provavelmente não funciona em darwin / win, porque importo `sys` e uso argv.

PS: O número é mesmo número de telemóvel. Formato 9XXXXXXXX (sem código de país, presume-se +351)

:)
