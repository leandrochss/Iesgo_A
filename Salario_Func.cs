using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Digite o nome do funcionário");
        string Nome_f = Console.ReadLine();
        Console.WriteLine("Digite as horas trabalhadas");
        int horas_trab = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Digite a sua taxa de pagamento por hora");
        double tax_pag = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Digite o valor das suas comissões semanais");
        decimal comissoes_sem = Convert.ToDecimaç(Console.ReadLine());


        decimal salario_brute = (decimal)(horas_trab * tax_pag) + comissoes_sem; 
        

        Console.WriteLine($"O nome do funcionário é {Nome_f}");
        Console.WriteLine($"O solário do funcionário é {salario_brute}");  
    }
}


