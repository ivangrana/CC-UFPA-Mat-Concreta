#include <iostream>
#include <iomanip> 
#include <cstdlib>
#include "triangulo.c"
using namespace std;


int main(){

int v_final;
cout << "Insira o indice final:\n";
cin >> v_final;
system("cls||clear");
cout << setw(53) << "--TRIANGULO DE PASCAL--\n\n";
for(int j = 0;j < v_final;j++){
    print_line(j);
    cout << endl;
}
}