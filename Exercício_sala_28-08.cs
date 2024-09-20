using System;

class Giraffe
{
    public string GetGiraffeSenior()
    {
        return @"
        .-^-.
  /_/_\_\
  || || ||
 (o| || |o)
   \\ //";
    }
}

class Coruja
{
    public string GetOwlDrawing()
    {
        return @"
  ^^  
 (o o)
  |O|
  -|-";
    }
}

class Dog
{
    public string GetDogRunning()
    {
        return @"
   / \__
  (    •  )
  /   .  . \
 /  |  • |  \
/_ |_  _| _\_";
    }
}

class Elephant 
{
    public string GetElephantGigant()
    {
        return @"
        /\\  ___  /\\
     (  o   o  )
    /     *     \
   / _____        \
  /_/     \____/";
    }
}

class Horse
{
    public string GetHorseScape()
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

class Program
{
    static void Main(string[] args)
    {
        Giraffe giraffe = new Giraffe();
        string giraffeSenior = giraffe.GetGiraffeSenior(); // Chamar o método para obter o desenho

        Coruja coruja = new Coruja();
        string owlDrawing = coruja.GetOwlDrawing(); // Chamar o método para obter o desenho

        Dog dog = new Dog();
        string dogRunning = dog.GetDogRunning(); // Chamar o método para obter o desenho

        
        Elephant elefante = new Elephant();
        string elefantegigante = elefante.GetElephantGigant();

        
        Horse cavalo = new Horse();
        string cavalogordo = cavalo.GetHorseScape();


        bool running = true;

        while (running)
        {
            Console.Clear();
            Console.WriteLine("Escolha a opção de desenho: ");
            Console.WriteLine("1 - Coruja");
            Console.WriteLine("2 - Girafa");
            Console.WriteLine("3 - Cachorro");
            Console.WriteLine("4 - Elefante");
            Console.WriteLine("5 - Cavalo");
            Console.WriteLine("0 - Encerrar programa");
            Console.WriteLine("---------------------------------------");
            Console.WriteLine("Digite sua escolha");

            string escolhaUsuario = Console.ReadLine();
            switch (escolhaUsuario)
            {
                case "1":
                    Console.WriteLine(owlDrawing);
                    break;

                case "2":
                    Console.WriteLine(giraffeSenior);
                    break;

                case "3":
                    Console.WriteLine(dogRunning);
                    break;

                case "4":
                    Console.WriteLine(elefantegigante);
                    break;

                case "5":
                    Console.WriteLine(cavalogordo); 
                    break;        

                case "0":
                    Console.WriteLine("Encerrando o sistema, até breve");
                    running = false; // Encerra o loop
                    break;

                default:
                    Console.WriteLine("Opção Inválida, tente novamente por gentileza");
                    break;
            }

            Console.WriteLine("Pressione qualquer tecla para continuar...");
            Console.ReadKey();
        }
    }
}
