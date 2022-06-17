#include <iostream>
#include "triangulo.h"
using namespace std;

long factorial(int n){
  if ((n==0)||(n==1))
   return 1;
   else
   return n*factorial(n-1);
}

long comb(long n,long p){
    long res,sub;
    sub = factorial(p)*factorial(n-p);
    res = factorial(n)/sub;
    return res;
}

void print_line(long n){
    for(int k = 0;k <= n;k++) cout << comb(n,k) << " ";
}
