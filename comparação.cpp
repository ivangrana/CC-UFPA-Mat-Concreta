#include <iostream>
#include <vector>
using namespace std;

void comp_sequencias(vector<int> A,vector<int> B,int cont = 0){ //Função que compara dois vetores
    for(int j = 0; j < A.size();j++){
        if(A.size() != B.size()){
            cout << "as sequências não são iguais\n"; 
            break;   
        }
        if(A[j] == B[j]) cont++;
        else{
            cout << "as sequências não são iguais\n"; 
            break;
        }
        }
    if(cont == A.size()) cout << "As sequências são iguais" << endl; 
    }

int main(){
    vector<int> A = {1,2,3,4,5}, B = {1,2,3,4,5};
    int cont = 0;
    comp_sequencias(A,B,cont);
    
    return 0;
}
