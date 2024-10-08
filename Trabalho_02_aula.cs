using System;
using System.Collections.Generic;
using System.IO;

interface IDrawing
{
    string GetDrawing();
    string Name { get; }
}

class Dog : IDrawing
{
    public string Name => "Cachorro";

    public string GetDrawing()
    {
        return @"
   / \__
  (    •  )
  /   .  . \
 /  |  • |  \
/_ |_  _| _\_";
    }
}

class Horse : IDrawing
{
    public string Name => "Cavalo";

    public string GetDrawing()
    {
        return @"
   ,--.
   \\__\
   (oo)
   _\=/_ 
  /     \  
 //|/.\|\\ 
 ||  |  ||
 ||  |  ||
 //  |  \\
\|  |  |/ 
 `-()--()--";
    }
}

class Shark : IDrawing
{
    public string Name => "Tubarão";

    public string GetDrawing()
    {
        return @"
                    /|  
  _______| |________________________________________  
<|________| |________________________________________>  
                    \|";
    }
}

class Elephant : IDrawing
{
    public string Name => "Elefante";

    public string GetDrawing()
    {
        return @"
      /\\  ___  /\\
     (  o   o  )
    /     *     \
   / _____        \
  /_/     \____/";
    }
}

class Program
{
    static List<IDrawing> drawings = new List<IDrawing>();

    static void Main(string[] args)
    {
        InitializeDrawings();
        bool running = true;

        while (running)
        {
            Console.Clear();
            Console.WriteLine("Escolha a opção que deseja: ");
            Console.WriteLine("1 - Listar todos os desenhos");
            Console.WriteLine("2 - Exibir um apenas desenho");
            Console.WriteLine("3 - Adicionar um novo desenho");
            Console.WriteLine("4 - Remover um desenho");
            Console.WriteLine("5 - Salvar desenhos em arquivo. (Será salvo em um arquivo txt)");
            Console.WriteLine("0 - Encerrar programa");
            Console.WriteLine("---------------------------------------");
            Console.Write("Digite sua escolha: ");

            string escolhaUsuario = Console.ReadLine();

            switch (escolhaUsuario)
            {
                case "1":
                    ListDrawings();
                    break;

                case "2":
                    ShowDrawing();
                    break;

                case "3":
                    AddNewDrawing();
                    break;

                case "4":
                    RemoveDrawing();
                    break;

                case "5":
                    SaveDrawingsToFile();
                    break;

                case "0":
                    Console.WriteLine("Encerrando o sistema, até breve");
                    running = false;
                    break;

                default:
                    Console.WriteLine("Opção Inválida, tente novamente por gentileza");
                    break;
            }

            if (running)
            {
                Console.WriteLine("Pressione qualquer tecla para continuar...");
                Console.ReadKey();
            }
        }
    }

    static void InitializeDrawings()
    {
        drawings.Add(new Dog());
        drawings.Add(new Horse());
        drawings.Add(new Shark());
        drawings.Add(new Elephant());
    }

    static void ListDrawings()
    {
        Console.Clear();
        Console.WriteLine("Desenhos Disponíveis:");
        for (int i = 0; i < drawings.Count; i++)
        {
            Console.WriteLine($"{i + 1} - {drawings[i].Name}");
        }
    }

    static void ShowDrawing()
    {
        ListDrawings();
        Console.Write("Digite o número do desenho que deseja exibir: ");
        if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= drawings.Count)
        {
            Console.Clear();
            Console.WriteLine(drawings[index - 1].GetDrawing());
        }
        else
        {
            Console.WriteLine("Entrada inválida! Por favor, tente novamente.");
        }
    }

    static void AddNewDrawing()
    {
        Console.Clear();
        Console.Write("Digite o nome do novo desenho: ");
        string name = Console.ReadLine();

        Console.WriteLine("Digite o desenho em ASCII (terminar com uma linha vazia):");
        string drawing = "";
        string line;
        while (!string.IsNullOrEmpty(line = Console.ReadLine()))
        {
            drawing += line + "\n";
        }

        drawings.Add(new CustomDrawing(name, drawing));
        Console.WriteLine("Novo desenho adicionado com sucesso!");
    }

    static void RemoveDrawing()
    {
        ListDrawings();
        Console.Write("Digite o número do desenho que deseja remover: ");
        if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= drawings.Count)
        {
            drawings.RemoveAt(index - 1);
            Console.WriteLine("Desenho removido com sucesso!");
        }
        else
        {
            Console.WriteLine("Entrada inválida, por favor, tente novamente.");
        }
    }

    static void SaveDrawingsToFile()
    {
        Console.Write("Digite o nome do arquivo para salvar os desenhos (ex: desenhos.txt): ");
        string fileName = Console.ReadLine();

        try
        {
            using (StreamWriter writer = new StreamWriter(fileName))
            {
                foreach (var drawing in drawings)
                {
                    writer.WriteLine($"Nome: {drawing.Name}");
                    writer.WriteLine(drawing.GetDrawing());
                    writer.WriteLine("---------------------------------------");
                }
            }
            Console.WriteLine("Desenhos salvos com sucesso! Obrigado.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Erro ao salvar os desenhos: {ex.Message}");
        }
    }
}

class CustomDrawing : IDrawing
{
    public string Name { get; }
    private string Drawing { get; }

    public CustomDrawing(string name, string drawing)
    {
        Name = name;
        Drawing = drawing;
    }

    public string GetDrawing()
    {
        return Drawing;
    }
}
