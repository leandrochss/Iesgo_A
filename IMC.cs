using System;

class Program
{
    static void Main(string[] args)
    {
        // Solicitação de peso e altura do usuário
        Console.Write("Digite seu peso em (kg): ");
        double peso = Convert.ToDouble(Console.ReadLine());

        Console.Write("Digite sua altura em (m): ");
        double altura = Convert.ToDouble(Console.ReadLine());

        // Calculando o IMC
        double imc = peso / (altura * altura);

        // Exibição do valor do IMC
        Console.WriteLine($"\nSeu IMC é: {imc:F2}");

        // Classificação do IMC de acordo com o resultado e mostrando colocação
        if (imc >= 20 && imc < 25)
        {
            Console.WriteLine("Você está com o peso normal.");
        }
        else if (imc >= 25 && imc < 30)
        {
            Console.WriteLine("Você está com excesso de peso.");
        }
        else if (imc >= 30 && imc <= 35)
        {
            Console.WriteLine("Você está com obesidade.");
        }
        else if (imc > 35)
        {
            Console.WriteLine("Você está com super obesidade.");
        }
        else
        {
            Console.WriteLine("Você está abaixo do peso.");
        }
    }
}
