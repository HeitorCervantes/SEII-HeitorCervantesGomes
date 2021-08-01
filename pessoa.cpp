#include <iostream>
#include "pessoa.h"

using namespace std;

 void pessoa::setPessoa(string Nome, int age, string Cpf, string Nacionalidade)
 {
         nome = Nome;
         idade = age;
         CPF = Cpf;
         nacionalidade = Nacionalidade;
 }

 void pessoa::getPessoa()
 {
         cout << "Nome: " << nome << "\n" << endl;
         cout << "Idade: " << idade << "\n" << endl;
         cout << "CPF: " << CPF << "\n" << endl;
         cout << "Nacionalidade: " << nacionalidade << "\n\n" << endl;

 }
