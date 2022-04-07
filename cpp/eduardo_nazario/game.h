//
// Created by Eduardo Nazário.
//

#ifndef HS_TICTACTOE_GAME_H
#define HS_TICTACTOE_GAME_H

#include <iostream>
#include <vector>
#include <time.h>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

#define USERS "./userData.csv"
#define FILEDELIM ','
#define PASSWORDLEN 4

#define NOTFINISHED '\n'
#define DRAW '\t'
#define KEEPPLAYING '\v'

void TicTacToe_App();
void startMultiplayer();
void  startDumbCPU();

#endif //HS_TICTACTOE_GAME_H
