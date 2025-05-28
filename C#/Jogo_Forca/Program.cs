using System;
using System.Collections.Generic;

namespace Jogo_Forca
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] palavras = { "amor", "azul", "escolha", "praia" };
            //definindo alguns nomes para iniciar o jogo

            Random sort = new Random();
            string palavra_secreta = palavras[sort.Next(palavras.Length)];
            char[] acertos = new string('_', palavra_secreta.Length).ToCharArray();
            // usando do '_' para fzer uma troca dos cracteres da palavra sorteada para este
            // o ToCharArry() converte strings em arrey, permitindo manipular letras de modo individual

            int tentativas = 6;
            List<char> erros = new List<char>();
            while (tentativas > 0 && new string(acertos) != palavra_secreta)
            {
                Console.Clear();
                Console.WriteLine("Jogo da forca");
                Console.WriteLine($"Palavra: {string.Join(" ", acertos)}");
                Console.WriteLine($"Erros: {string.Join(" ", erros)}");
                Console.WriteLine($"Tentativas restantes: {tentativas}");
                Console.Write("Digite uma letra: ");
                string entrada = Console.ReadLine()?.ToLower();
                // O uso do ToLower() faz com que  letra digitada seja necessariamente minuscula
                
                if (string.IsNullOrWhiteSpace(entrada) || entrada.Length != 1 || !char.IsLetter(entrada[0]))
                // IsNullOrWhiteSpace realiza uma verificação se há espaços nulos ou vazios na entrada
                // O Length garante que tenha pelo menos um digito para avançar
                // O IsLetter faz verificação se a entrada é um cractere de A a Z, realizando um filtragem de caracteres
                
                {
                    Console.WriteLine("Entrada inválida (tecle Enter para continuar) ");
                    Console.ReadLine();
                    continue;
                }
                char letra = entrada[0];
                if (palavra_secreta.Contains(letra))
                {
                    for (int i = 0; i < palavra_secreta.Length; i++)
                    {
                        if (palavra_secreta[i] == letra)
                        {
                            acertos[i] = letra;
                        }
                    }
                }
                else
                {
                    if (!erros.Contains(letra))
                    {
                        erros.Add(letra);
                        tentativas--;
                    }
                }
            }
            Console.Clear();
            if (new string (acertos) == palavra_secreta)
            {
                Console.WriteLine("Parabéns, você acertou!");
                Console.WriteLine($"A palavra era: {palavra_secreta}");
            }
            else
            {
                Console.WriteLine($"Você perdeu. a palavra era: {palavra_secreta}");
            }
        }
    }
}
    