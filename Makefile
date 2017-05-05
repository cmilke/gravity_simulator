all: simulation_engine.cpp
	clang++ -shared -fPIC -o simulation_engine.so simulation_engine.cpp

fast: simulation_engine.cpp
	clang++ -O3 -shared -fPIC -o simulation_engine.so simulation_engine.cpp

clean:
	-rm simulation_engine.so 2&>/dev/null || true

tutorial: tutorial.c
	clang -shared -fPIC -o tutorial.so tutorial.c
