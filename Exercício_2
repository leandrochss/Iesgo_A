// Exercício 02
// Sistema em C# em que o usuário insere o nome e a data de nascimento e o sistema retorna seu nome e idade.

using System;
using System.Text;

class Programa
{
    static void Main()
    {
        // Usando UTF-8 no console
        Console.OutputEncoding = Encoding.UTF8;

        // Solicitação do nome de usuário 
        Console.Write("Digite seu nome por gentileza: ");
        string name = Console.ReadLine();

        // Solicitação de data de nascimento
        Console.WriteLine("Agora, insira sua data de nascimento (DD/MM/AAAA): ");
        string data_NascInput = Console.ReadLine();
    
        // Converter a string data_Nasc para DateTime
        DateTime data_Nasc;
        if (DateTime.TryParseExact(data_NascInput, "dd/MM/yyyy", null, System.Globalization.DateTimeStyles.None, out data_Nasc))
        {
            // Calcular idade
            int idade = CalcularIdade(data_Nasc);

            // Respondendo usuário no console
            Console.WriteLine($"Olá, {name}! Você tem {idade} anos.");
        }
        else
        {
            // Mensagem de erro
            Console.WriteLine("Data de nascimento inválida. Insira uma data de nascimento válida.");
        }
    }

    static int CalcularIdade(DateTime data_Nasc)
    {
        // Data atual
        DateTime hoje = DateTime.Today;

        // Calcular idade
        int idade = hoje.Year - data_Nasc.Year;

        // Ajuste se a data de nascimento ainda não ocorreu este ano
        if (data_Nasc.Date > hoje.AddYears(-idade)) idade--;
        
        return idade;
    }
}
