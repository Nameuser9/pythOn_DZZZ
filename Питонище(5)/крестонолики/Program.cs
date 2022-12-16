void PrintArray2(int[,] col)
{
    //int count = col.Length;
    //int position = 0;
   for (int i = 0; i < col.GetLength(0); i++)
    {
        for (int j = 0; j < col.GetLength(1); j++)
        {
        Console.Write($"{ col [i , j]} ");        
        }
    Console.WriteLine();
    }  
}
int[,] array = new int [3,3];
PrintArray2(array);
int i = 0;
while ( i < 9)
{
    if (i % 2 == 0)
    {
        firsthod:
        Console.WriteLine("Ходит первый игрок");
        Console.WriteLine("укажите координату хода");
        int a = Convert.ToInt32(Console.ReadLine());
        int b = Convert.ToInt32(Console.ReadLine());
        if ((array[a-1,b-1] == 1 |array[a-1,b-1] == 2))
        {Console.WriteLine("клетка уже занята, выбери ещё раз");
            goto firsthod;}
            array[a-1,b-1] = 1;
        PrintArray2(array);
        
    }
    else
    {
       secondhod: 
    Console.WriteLine("Ходит второй игрок");
    Console.WriteLine("укажите координату хода");
    int x = Convert.ToInt32(Console.ReadLine());
    int y = Convert.ToInt32(Console.ReadLine());
    if ((array[x-1,y-1] == 1 |array[x-1,y-1] == 2))
        {Console.WriteLine("клетка уже занята, выбери ещё раз");
            goto secondhod;}
    array[x-1,y-1] = 2;
    PrintArray2(array);
    
    }
  i++; 
   if (i > 4)
   {
    if  (array[0,0] == array[1,1] && array[1,1] == array[2,2])
        {if (array[1,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
        else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[0,0]==array[1,0]&&array[1,0] ==array[2,0])
        {if (array[1,0]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
        else
                {Console.WriteLine("победил второй игрок");
                break;}}  
    if (array[0,0]==array[0,1]&&array[0,2] ==array[0,2])
        {if (array[0,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
        else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[0,1]==array[1,1]&& array[1,1]==array[2,1])
        {if (array[1,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
        else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[2,0]==array[2,1]&& array[2,1]==array[2,2])
        {if (array[2,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
            else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[0,2]==array[1,2]&& array[1,2]==array[2,2])
        {if (array[1,2]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
            else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[0,0]==array[1,1]&& array[1,1]==array[1,2])
        {if (array[1,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
            else
                {Console.WriteLine("победил второй игрок");
                break;}}
    if (array[0,2]==array[1,1]&& array[1,1]==array[2,0])
    {if (array[1,1]==1)
                {Console.WriteLine("победил первый игрок");
                break;}
            else
                {Console.WriteLine("победил второй игрок");
                break;}}
    }
}
