using System;
using System.Threading;

class Program
{
    static void Main()
    {
        for (int x = 10; x >=1; x--)
        {
            Thread.Sleep(1000);
            
        switch (x){
            case 10:
             Console.WriteLine("I");
                break;
            case 9:
            Console.WriteLine("am");
                break;
            case 8:
            Console.WriteLine("always");
                break;
            case 7:
            Console.WriteLine("sleepy");
                break;
            case 6:
            Console.WriteLine("when");
                break;
            case 5:
            Console.WriteLine("I");
                break;
            case 4:
            Console.WriteLine("didn't");
                break;
            case 3:
            Console.WriteLine("sleep");
                break;
            case 2:
            Console.WriteLine("early");
                break;
            case 1:
            Console.WriteLine("at night");
                break;
            default:
                break;

        }
        }
    }
}