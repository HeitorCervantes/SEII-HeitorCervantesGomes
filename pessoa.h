#include <cstdio>
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

class pessoa
{

 public:
        string nome;
        int idade;
        string CPF;
        string nacionalidade;

        void setPessoa(string Nome, int age, string Cpf, string Nacionalidade);
        void getPessoa();

};
