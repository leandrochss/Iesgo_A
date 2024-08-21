using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Digite o primeiro número");
        int num1 = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Digite o Segundo número");
        int num2 = Convert.ToInt32(Console.ReadLine());

        int soma = num1 + num2;
        Console.WriteLine("A Soma dos números é: " + soma);

    }
}
