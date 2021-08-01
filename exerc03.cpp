#include <iostream>
#include <unistd.h>
#include <string>
#include <stdlib.h>
#include "pessoa.h"

using namespace std;
using std::cout;
using std::endl;

int main()
{
        pessoa pessoas[100];
        int i = 0, j, age;
        int opcao, rm;
        string name, cpf, nac;


while (opcao != 4)
{
        cout << "\n\n---------- Menu de Opção ---------- \n" << endl;
        cout << "Opção 1: Fazer cadastro. \n" << endl;
        cout << "Opção 2: Remover cadastro. \n" << endl;
        cout << "Opção 3: Listar cadastros. \n" << endl;
        cout << "Opção 4: Sair do Menu. \n" << endl;
        cout << "----------------------------------- \n" << endl;
        cout << "Digite sua opção: ";
        cin >> opcao;
        cout << endl;


        switch (opcao)
        {
                case 1:
                        cout << "Pessoa " << i+1 << "\n" << endl;

                        cout << "Nome: "; getline(cin, name); getline(cin, name); cout << endl;

                        cout << "Idade: "; cin >> age; cout << endl;

                        cout << "CPF: "; getline(cin, cpf); getline(cin, cpf); cout << endl;

                        cout << "Nacionalidade: "; getline(cin, nac); cout << endl;

                        pessoas[i].setPessoa(name,age,cpf,nac);
                        i++;

                        if (i >= 100)
                        {
                                cout << "Limite de Cadastro.\nO programa sera fechado." << endl;
                                usleep(1000*1000);
                                opcao = 4;
                        }
                        system("clear");
                        break;

                case 2:
		 while(rm!=3)
		  {
                        system("clear");
                        cout << "\n\n---------- Remover CADASTRO ---------- \n" << endl;
                        cout << "Opção 1: por Nome. \n" << endl;
                        cout << "Opção 2: por CPF. \n" << endl;
                        cout << "Opção 3: Sair do Menu -  Remover CADASTRO. \n" << endl;
                        cout << "----------------------------------- \n" << endl;
                        cout << "Digite sua opção: ";
                        cin >> rm;
                        cout << endl;
                        usleep(1000*1000);

                        switch (rm)
                        {
                                case 1:
                                        cout << "Nome a remover: "; getline(cin, name); getline(cin, name); cout << endl;
                                        cout << "Pesquisando..." << endl;
                                        usleep(1000*1000);
                                        j = 0;
                                        for(j; j<i; j++)
                                        {
                                                if(name == pessoas[j].nome)
                                                {

                                                        cout << pessoas[j].nome << "\tRemovida com sucesso!" << endl;
                                                        usleep(1000*1000);

                                                        if(j==0)
                                                        {
                                                                pessoas[j].setPessoa(" ", 0, " ", " ");
                                                        }

                                                        int x=j;
                                                        for(x; x<i; x++)
                                                        {
                                                                pessoas[x].setPessoa(pessoas[x+1].nome, pessoas[x+1].idade, pessoas[x+1].CPF, pessoas[x+1].nacionalidade);
                                                        }
                                                        i--;

                                                        break;

                                                }
                                                else if(j+1 == i)
                                                {
                                                        cout << "Nome não encontrado" << endl;
                                                        usleep(1000*1000);
                                                }
                                        }
                                        system("clear");
                                        break;

                                case 2:
                                        cout << "CPF a remover: "; getline(cin, cpf); getline(cin, cpf); cout << endl;
                                        cout << "Pesquisando..." << endl;
                                        usleep(1000*1000);
                                        j = 0;
                                        for(j; j<i; j++)
                                        {
                                                if(cpf == pessoas[j].CPF)
                                                {

                                                        cout << pessoas[j].nome << "\tRemovida com sucesso!" << endl;
                                                        usleep(1000*1000);

                                                        if(j==0)
                                                        {
                                                                pessoas[j].setPessoa(" ", 0, " ", " ");
                                                        }


                                                        int x=j;
                                                        for(x; x<i; x++)
                                                        {
                                                                pessoas[x].setPessoa(pessoas[x+1].nome, pessoas[x+1].idade, pessoas[x+1].CPF, pessoas[x+1].nacionalidade);
                                                        }
                                                        i--;

                                                        break;

                                                }
                                                else if(j+1 == i)
                                                {
                                                        cout << "CPF não encontrado" << endl;
                                                        usleep(3000*1000);
                                                }
                                        }
                                        system("clear");
                                        break;

                                case 3:
                                        cout << "Saindo... \n" << endl;
                                        usleep(1000*1000);
		                        system("clear");
                                        break;

                                default:
                                        cout << "Opção inválida" << endl;
                                        usleep(1000*1000);
                                        system("clear");

                        }
	   	 }
               	 break;

                case 3:
                        j = 0;
                        cout << "\n\n\t -----INICIO DA LISTA----- \n\n" << endl;
                        for (j; j < i; j++)
                        {
                                pessoas[j].getPessoa();
                        }
                        cout << "\t -----FIM DA LISTA----- \n\n" << endl;

                        usleep(1000*1000);
                        break;

                case 4:
                        cout << "Saindo do programa... \n" << endl;
                        usleep(1000*1000);
                        system("clear");
                        break;

                default:
                        cout << "\nOpção inválida" << endl;
                        usleep(1000*1000);
                        system("clear");
        }

}

        usleep(1000*1000);
        return 0;
}

