# the compiler: gcc for C program, define as g++ for C++
  CC = g++
 
  # compiler flags:
  #  -g     - this flag adds debugging information to the executable file
  #  -Wall  - this flag is used to turn on most compiler warnings
  CFLAGS  = -g -Wall

  all: clean menus.o register.o login.o tictactoe.o main.o main
  normal: menus.o register.o login.o tictactoe.o main.o main
 
  main: login.o menus.o register.o main.o
	$(CC) $(CFLAGS) -o main main.o login.o menus.o register.o tictactoe.o
  

  menus.o: menus.h menus.cpp 
	$(CC) $(CFLAGS) -c menus.cpp

  register.o: register.h register.cpp 
	$(CC) $(CFLAGS) -c register.cpp
  
  login.o: login.h login.cpp 
	$(CC) $(CFLAGS) -c login.cpp

  tictactoe.o: tictactoe.h tictactoe.cpp 
	$(CC) $(CFLAGS) -c tictactoe.cpp
  
 
  main.o: register.h login.h menus.h main.cpp
	$(CC) $(CFLAGS) -c main.cpp

  clean:
	rm *.o main