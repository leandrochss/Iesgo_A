using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Digite o primeiro número");
        int num = Convert.ToInt32(Console.ReadLine());

        if (num % 2 ==0)
        {
            Console.WriteLine("O número é par");
        } 
        else 
        {
            Console.WriteLine("O número é impar");
        }
    }
}
