// # include <iostream>
// int Multiply(int a,int b)
// {
//     return a*b;
// }
// int main()
// {
//     int result1 = Multiply(10,2);
//     std::cout << result1 << std :: endl;
//     std::cin.get();
// }

// #include<iostream>
// using namespace std;
// int main()
// {
//     cout << "hello world" << endl;
//     int age;
//     cin >> age;
//     cout << "You are " << age << ".";
//     return 0;
// }

// #include <iostream>
// int main()
// {
//     std :: cout << "Enter two numbers:" << std :: endl;
//     int v1 = 0; int v2 = 0;
//     std :: cin >> v1 >> v2;
//     std :: cout << "The sum of " << v1 << " and " << v2
//                 << " is " << v1 + v2 << std :: endl;
//     return 0;
// }

//test 1.4.1
//1.9
// #include <iostream>
// int main()
// {
//     int num = 50, sum = 0;
//     while(num <= 100)
//     {
//         sum += num;
//         ++num;
//     }
//     std :: cout <<"The sum is "<< sum << std :: endl;
//     return 0;
// }

//1.10
// #include <iostream>
// int main()
// {
//     int num = 10;
//     while(num >= 1)
//     {
//         std :: cout << num << std :: endl;
//         --num;
//     }
// }

//1.11
// #include <iostream>
// int main()
// {
//     int num1,num2;
//     std :: cin >> num1 >>num2;
//     while (num1 <= num2)
//     {
//         std :: cout << num1 << std :: endl;
//         ++num1;
//     }
// }


//for循环
// #include <iostream>
// int main()
// {
//     int sum = 0;
//     for (int val = 1; val <= 10; ++val)
//         sum += val;
//     std :: cout << "Sum of 1 to 10 inclusive is "
//                 << sum << std :: endl;
//     return 0;
// }


// #include <iostream>
// int main()
// {
//     int sum = 0;
//     for(int i = -100; i <= 100; ++i)
//     {
//         sum += i;
//     }
//     std :: cout << sum;
//     return 0;
// }

// #include <iostream>
// int main()
// {
//     int a,b;
//     int flag=1;
//     std :: cout <<"enter two number: ";
//     std :: cin >> a >> b;
//     while(true)
//     {
//         flag = 0;
//     if (a<b)
//     {
//        for(; a <= b;a++)
//     {
//         std :: cout << a <<std::endl;
//     }
//     break;
//     }
//     else
//     {
//         std :: cout << "please enter again";
//         std :: cin >> a >>b;
//     }
//     }
//     return 0;
// }
    

// #include <iostream>
// int main()
// {
//     int sum = 0, value = 0;
//     while (std :: cin >> value)//文件结束符为ctrl + z
//         sum += value;
//     std :: cout << "Sum is: " << sum << std :: endl;
//     return 0;
// }

#include <iostream>
int main()
{
    int currVal = 0,val = 0;
    if(std :: cin >> currVal)
    {
        int cnt = 1;
        while (std :: cin >> val)
        {
            if (val == currVal)
                ++cnt;
            else
            {
                std :: cout << currVal <<
            }
        }
    }
}