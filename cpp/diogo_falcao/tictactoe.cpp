#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;

//FUNCOES AUX
int jogo_multiplayer();
int jogo_computador();
void desenha_tab();
void inicia_tab();
int * obtem_linha(int l);
int * obtem_coluna(int c);
int * obtem_diagonal(int d);
int verifica_ganhador();
int eh_pos(int pos);
int eh_pos_livre(int pos);
int marcar_pos(int j, int pos);
int canto_oposto(int j);
int AI_estrategia(int j);
int vitoria(int j);
int escolher_pos_jogador(int j);

//VARS GLOBAIS
int tabuleiro[3][3];
list<int> pos_livres;

//Jogo Player1 Vs Player 2
int jogo_multiplayer(){
    int jogador1, jogador2, turno;
    cout << "Bem vindo ao Tic Tac Toe Player1 Vs Player2!\nPlayer 1: 1)Cruz -1)Bola \n"; 
    cin >> jogador1;
    while(jogador1 != -1 && jogador1 != 1){
        cout << "Escolha errada." << endl;
        cout << "Escolha: 1)Cruz -1)Bola " << endl;
        cin >> jogador1;
    }
    jogador2 = -1*jogador1;
    cout << "Player 1 escolhe jogar em primeiro ou em segundo?\nEscolha: 1)Primeiro 2)Segundo\n";
    cin >> turno;
    while(turno != 1 && turno != 2){
        cout << "Escolha errada." << endl;
        cout << "Escolha: 1)Primeiro 2)Segundo" << endl;
        cin >> turno;
    }
    inicia_tab();
        cout << "VAMOS COMEÇAR O JOGO! Nota: Escolha sempre uma posição de 1-9\n";
        while(verifica_ganhador() == 0 || pos_livres.size() != 0 ){
            if(turno == 1)
                marcar_pos(jogador1,escolher_pos_jogador(jogador1));
            else 
                marcar_pos(jogador2,escolher_pos_jogador(jogador2));
            desenha_tab();
            int ver = verifica_ganhador();
            if(ver == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(ver == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && ver == 0){
                cout << "Empate" << endl;
                return 0;
            }
            if(turno == 1)
                marcar_pos(jogador2,escolher_pos_jogador(jogador2));
            else 
                marcar_pos(jogador1,escolher_pos_jogador(jogador1));
            desenha_tab();
            ver = verifica_ganhador();
            if(ver == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(ver == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && ver == 0){
                cout << "Empate" << endl;
                return 0;
            }
        }
    return 0;
}

//Jogo Player Vs Computer
int jogo_computador(){
    int jogador, computador, turno;
    cout << "Bem vindo ao Tic Tac Toe Player Vs Computer!\nEscolha: 1)Cruz -1)Bola \n";
    cin >> jogador;
    while(jogador != -1 && jogador != 1){
        cout << "Escolha errada." << endl;
        cout << "Escolha: 1)Cruz -1)Bola " << endl;
        cin >> jogador;
    }
    cout << "Escolhe jogar em primeiro ou em segundo?\nEscolha: 1)Primeiro 2)Segundo\n";
    cin >> turno;
    while(turno != 1 && turno != 2){
        cout << "Escolha errada." << endl;
        cout << "Escolha: 1)Primeiro 2)Segundo" << endl;
        cin >> turno;
    }
    inicia_tab();
    if(turno == 1){
        cout << "VAMOS COMEÇAR O JOGO! Nota: Escolha sempre uma posição de 1-9\n";
        while(verifica_ganhador() == 0 || pos_livres.size() != 0 ){
            marcar_pos(jogador,escolher_pos_jogador(jogador));
            desenha_tab();
            int ver = verifica_ganhador();
            if(ver == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(ver == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && ver == 0){
                cout << "Empate" << endl;
                return 0;
            }
            cout << "Turno do computador\n";
            printf("pos comp: %d\n",AI_estrategia(-1*jogador));
            marcar_pos(-1*jogador,AI_estrategia(-1*jogador));
            desenha_tab();
            ver = verifica_ganhador();
            if(ver == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(ver == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && ver == 0){
                cout << "Empate" << endl;
                return 0;
            }
        }

    }
    else{
        cout << "VAMOS COMEÇAR O JOGO!\n";
        while(verifica_ganhador() == 0 || pos_livres.size() != 0 ){
            cout << "Turno do computador\n";
            marcar_pos(-1*jogador,AI_estrategia(-1*jogador));
            desenha_tab();
            if(verifica_ganhador() == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(verifica_ganhador() == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && verifica_ganhador() == 0){
                cout << "Empate" << endl;
                return 0;
            }
            marcar_pos(jogador,escolher_pos_jogador(jogador));
            desenha_tab();
            if(verifica_ganhador() == 1){
                cout << "Ganharam as X" << endl;
                return 0;
            }
            if(verifica_ganhador() == -1){
                cout << "Ganharam as O" << endl;
                return 0;
            }
            if(pos_livres.size() == 0 && verifica_ganhador() == 0){
                cout << "Empate" << endl;
                return 0;
            }
        }
    }
    return 0;
}

//Desenha o tabuleiro
void desenha_tab(){
    for(int i = 1; i < 10; i++){
        int coluna = (i-1) % 3;
        int linha = (i-1) / 3;
        if(coluna == 2){
            if(tabuleiro[linha][coluna] == 1)
                printf(" X \n");
            else if(tabuleiro[linha][coluna] == -1)
                printf(" O \n");
            else printf("   \n");
        }
        if(coluna == 2 && linha != 2)
            printf("-----------\n");
        if(coluna == 0 | coluna == 1){
            if(tabuleiro[linha][coluna] == 1)
                printf(" X |");
            else if(tabuleiro[linha][coluna] == -1)
                printf(" O |");
            else printf("   |");
        }
    }
}

//Retorna uma linha
int * obtem_linha(int l){
    if(l > 0 && l < 4){
        return tabuleiro[l-1];
    }
    return 0;
}

//Retorna uma coluna
int * obtem_coluna(int c){
    if(c > 0 && c < 4){
        int* col = new int[3];
        col[0] = tabuleiro[0][c-1];
        col[1] = tabuleiro[1][c-1];
        col[2] = tabuleiro[2][c-1];
        return col;
    }
    return 0;
}

//Retorna uma das duas diagonais
int * obtem_diagonal(int d){
    int* diag = new int[3];
    if(d == 1){
        diag[0] = tabuleiro[0][0];
        diag[1] = tabuleiro[1][1];
        diag[2] = tabuleiro[2][2];
        return diag;
    }
    if(d == 2){
        diag[0] = tabuleiro[0][2];
        diag[1] = tabuleiro[1][1];
        diag[2] = tabuleiro[2][0];
        return diag;
    }
    return 0;
}

//Verifica se no tabuleiro atual existe algum jogador vencedor 
int verifica_ganhador(){
    int pontos;
    int* aux;
    for(int i = 1; i != 4; i++){
        pontos = 0;
        aux = obtem_linha(i);
        for(int j = 0; j < 3; j++){
            pontos += aux[j];
        }
        if(pontos == 3) 
            return 1;
        if(pontos == -3) 
            return -1;
    }
    for(int i = 1; i < 4; i++){
        pontos = 0;
        aux = obtem_coluna(i);
        for(int j = 0; j < 3; j++){
            pontos += aux[j];
        }
        if(pontos == 3) 
            return 1;
        if(pontos == -3) 
            return -1;
    }
    for(int i = 1; i < 3; i++){
        pontos = 0;
        aux = obtem_diagonal(i);
        for(int j = 0; j < 3; j++){
            pontos += aux[j];
        }
        if(pontos == 3) 
            return 1;
        if(pontos == -3) 
            return -1;
    }
    return 0;
}

//Inicia o tabuleiro
void inicia_tab(){
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++)
            tabuleiro[i][j] = 0;
    }
    for(int i = 1; i < 10; i++){
        pos_livres.push_back(i);
    }
}

//Verifica se é uma posição
int eh_pos(int pos){
    if(pos > 0 && pos <= 9)
        return 1;
    else
        return 0;
}

//Verifica se é uma posição livre
int eh_pos_livre(int pos){
    if(eh_pos(pos)){
        int coluna = (pos-1) % 3;
        int linha = (pos-1) / 3;
        if(tabuleiro[linha][coluna] == 0)
            return 1;
        else
            return 0;
    }
    return 0;
}

//Marca uma posição no tabuleiro
int marcar_pos(int j, int pos){
    if(eh_pos(pos)){
        int coluna = (pos-1) % 3;
        int linha = (pos-1) / 3;
        tabuleiro[linha][coluna] = j;
        pos_livres.remove(pos);
        return 1;
    }
    return 0;
}

//Escolhe a posição do jogador
int escolher_pos_jogador(int j){
    int pos;
    printf("Turno do jogador %d. Escolha uma posicao: ", j);
    cin >> pos;

    if(eh_pos_livre(pos) && eh_pos(pos))
        return pos;
    else{
        while((eh_pos_livre(pos) && eh_pos(pos)) == 0){
            cout << "Posicao nao disponivel. Tente novamente." << endl;
            cout << "Turno do jogar. Escolha uma posicao: ";
            cin >> pos;
        }
        return pos;
    }
    return 0;
}

// AI que empata ou ganha (tentativa)
int AI_estrategia(int j){
    int cantos[4] = {1,3,7,9};
    int laterais[4] = {2,4,6,8};
    if(vitoria(j) != 0)
        return vitoria(j);
    //Bloquear uma posível jogada de vitória do oponente
    else if(vitoria(-1*j) != 0)
        return vitoria(-1*j);
    
    else if(eh_pos_livre(5) != 0){
        return 5;}
    
    else if(canto_oposto(j) != 0)
        return canto_oposto(j);
    //Escolher canto livre e só depois uma lateral
    else{
        for(int i = 0; i < 4; i++){
            if(eh_pos_livre(cantos[i]) == 1)
                return cantos[i];
        }
        for(int i = 0; i < 4; i++){
        if(eh_pos_livre(laterais[i]) == 1)
            return laterais[i];
        }
    }
    return 0;
}

//Marca na posição que dá a vitória ao jogador jog
int vitoria(int jog){
    int soma,pos,pos1;
    int diag1[3] = {1,5,9};
    int diag2[3] = {3,5,7};
    int *aux1;
    for(int i = 1; i < 4; i++){
        soma = 0;
        pos = 0;
        pos1 = 0;
        aux1 = obtem_coluna(i);
        for(int j = 0; j < 3; j++){
            pos = i+(j*3);  
            if(eh_pos_livre(pos) == 1){
                pos1 = i+(j*3);   
            }
            soma += aux1[j];
        }
        if (soma == jog*2){
            return pos1;
            }
    }
    for(int i = 1; i < 4; i++){
        soma = 0;
        pos = 0;
        aux1 = obtem_linha(i);
        for(int j = 0; j < 3; j++){
            if(aux1[j] == 0){
                pos = ((i-1)*3)+(j+1);
            }
            soma += aux1[j];
        }
        if (soma == jog*2)
            return pos;
    }
    for(int i = 1; i < 3; i++){
        soma = 0;
        pos = 0;
        aux1 = obtem_diagonal(i);
        for(int k = 0; k < 3; k++){
        }
        if(i == 1){
            for(int j = 0; j < 3; j++){
                if(aux1[j] == 0){
                    pos = diag1[j]; 
                }
                soma += aux1[j];
            }
            if (soma == jog*2)
                return pos;
        }
        else if(i == 2){
            for(int j = 0; j < 3; j++){
                if(aux1[j] == 0){
                    pos = diag2[j];
                }
                soma += aux1[j];
            }
            if (soma == jog*2){
                return pos;
            }
        }
    }
    return 0;
}
//Joga num canto oposto livre
int canto_oposto(int j){
    if(obtem_diagonal(1)[2] == -j){
        if(eh_pos_livre(1) == 1)
            return 1;
    }
    else if(obtem_diagonal(2)[0] == -j){
        if(eh_pos_livre(3) == 1)
            return 3;
    }
    else if(obtem_diagonal(2)[2] == -j){
        if(eh_pos_livre(7) == 1)
            return 7;
    }
    else if(obtem_diagonal(1)[0] == -j){
        if(eh_pos_livre(9) == 1)
            return 9;
    }
    return 0;
}
