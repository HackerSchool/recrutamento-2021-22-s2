CXXFLAGS := $(shell root-config --cflags)
ROOTLIB := $(shell root-config --libs)
XXEIGEN := $(shell pkg-config --cflags eigen3)

OBJS := calculadora.cpp changepass.cpp options.cpp recrutamento.cpp start.cpp startFuncs.cpp MetodoGauss.cpp GaussJordan.cpp opstrings.cpp


%.exe : %.cpp $(OBJS)
	g++ $(CXXFLAGS) $^ $(ROOTLIB) $(XXEIGEN) -I/usr/include/eigen3 -o $@ 

clean : 
	rm -f *.o *.exe
