//Desenvolvido por: Pedro Cobianchi Borges Paiva
// 22/07/2020
#include <iostream>
#include <math.h>
#include <omp.h>
#include <time.h>
using namespace std;

double f(double x){
double return_val;
return_val = pow(x, 2) + sqrt(x); //insira sua função aqui
return return_val;
}
int main(int argc, char **argv){

double a, b, h;
double x = 0.0;
double total= 0.0;
long long int n;
long long int i;
clock_t t0, tf;
double tempo_gasto;

cout << "Entre com os valores de a, b, and n" << endl;
cin >> a >> b >> n;

h = (b-a)/n;
//regiao paralelizada
//irá dividir os intervalos onde cada thread irá atuar
//printf("Threads com h = %lf \n", h);
t0 = clock();

omp_set_num_threads(16);
#pragma omp parallel
{

int nThreads = omp_get_num_threads();
int tId = omp_get_thread_num();

//printf("\nThread numero %d de %d\n", tId, nThreads);

//isso significa quantos intervalos preciso percorrer para cada thread
int local_n = n/nThreads;
//printf("Thread %d com local_n = %d \n", tId, local_n);

double local_a = a + (tId*local_n*h);
//printf("Thread %d com local_a = %lf \n", tId, local_a);
double local_b = local_a + local_n*h;
//printf("Thread %d com local_b = %lf \n", tId, local_b);

double integral = (f(local_a) + f(local_b))/2.0;
//printf("Thread %d com integral inicial = %lf \n\n", tId, integral);
x = local_a;

//cada thread irá pegar e calcular a integral em seus respectivos intervalos
//executado em ordem sequencial
#pragma omp parallel for schedule (static, local_n) firstprivate(x) ordered
for (i = 1; i < local_n; i++) {
//também executado em ordem sequencial
#pragma omp ordered
{
x += h;
integral += f(x);
//printf("Thread %d f(x) = %lf e x = %lf\n",tId, f(x), x);
}
}
//pega as parciais de integral e soma-se em total
#pragma omp critical
{
//printf("Soma da integral da Thread %d que é igual a %lf \n",tId,integral);
total += integral;
}
}

total *= h;
//printf("Com n = %lld trapezóides, a estimativa \n", n);
//printf("da integral de %.1lf até %.1lf = %lf \n", a, b, total);
tf = clock();
tempo_gasto = ( (double) (tf - t0) ) / CLOCKS_PER_SEC;
//printf("Tempo gasto: %lf s\n", tempo_gasto);

return 0;
}
