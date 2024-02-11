// #include<stdio.h>
// int main(void)
// {
//     int a,b;
//     a=2;
//     b=4;
//     printf("%d+%d=%d",a,b,a+b);

//     return 0;
// }

// #include<stdio.h>
// int main(void)
// {
//     int a=5;
//     int*p;
//     p=&a;
    
//     printf("p=%d\n",p);
//     printf("a'saddress=%p\n",&a);
// }

// #include<stdio.h>
// int max(int num1,int num2);
// int main(void)
// {
//     int a=100;
//     int b=200;
//     int ret;

//     ret=max(a,b);

//     printf("Max value is:%d\n",ret);

//     return 0;
// }

// int max(int num1,int num2)
// {
//     int result;
//     if(num1>num2)
//         result =num1;
//     else
//         result =num2;

//     return result;
// }


// #include<stdio.h>
// #include<stdlib.h>

// int main(void)
// {
//     int i,j,no_prime,n;
//     printf("请输入n的值:");
//     scanf("%d",&n);

//     i=2;

//     printf("以下是2-%d的质数:",n);
//     while(i<=n)
//     {
//         no_prime=0;
//         for(j=2;j<i;j++)
//         if(i%j==0)
//         {
//             no_prime=1;
//             break;

//         }

//         if(no_prime==0)
//         printf("%d ",i);
//         i++;
//     }

//     printf("\n");
//     return 0;

// }

// #include<stdio.h>
// #include<stdlib.h>
// int area(int,int);

// int main(void)
// {
//     int l,b,rect_area;
//     printf("请输入长和宽：");
//     scanf("%d,%d",&l,&b);

//     rect_area=area(l,b);
//     printf("长方形的面积：%d",rect_area);

//     return 0;

// }

// int area(int l,int b)
// {
//     return l*b;
// }

// #include<stdio.h>
// #include<stdlib.h>
// float pow(float x,int y)
// {
//     float p=1;
//     int i;
//     for(i=1;i<=y;i++)
//     p=p*x;
//     return p;
// }

// int main(void)
// {
//     float x;
//     int y;

//     printf("请输入次方运算如(2^3):");
//     scanf("%f^%d",&x,&y);
//     printf("次方运算结果：%.4f\n",pow(x,y));

//     return 0;
// }

// #include<stdio.h>
// #include<stdlib.h>

// int x=10;
// int main(void)
// {
//     void setx1();
//     void setx2();
//     printf("在main函数中x=:%d\n",x);
//     setx1();
//     printf("在main函数中x=:%d\n",x);
//     setx2();
//     printf("在main函数中x=:%d\n",x);
//     return 0;

// }
// void setx1()
// {
//     x=20;
//     printf("在setx1函数中x=%d\n",x);

// }
// void setx2()
// {
//     x=30;
//     printf("在setx2函数中x=%d\n",x);
// }


// #include<stdio.h>
// int factorial(int);

// int main(void)
// {
//     int i,n;
//     printf("请输入计算到几阶的阶乘：");
//     scanf("%d",&n);

//     for(i=0;i<=n;i++)
//     printf("%d!值为 %3d\n",i,factorial(i));

//     return 0;
// }
// int factorial(int i)
// {
//     int sum;
//       if(i==0)
//         return(1);
//       else
//       sum=i*factorial(i-1);
//       return sum;
// }

// #include<stdio.h>
// int fib(int);

// int main(void)
// {
//     int a,b;

    
//     printf("请输入:");
//     scanf("%d",&a);

//     printf("fib数列%d项结果:%d",a,fib(a));

//     return 0;

// }
// int fib(int a)
// {
//     int sum;
//       if(a==0)
//         return(0);
//       else if(a==1)
//         return(1);
//       else
//       sum=fib(a-1)+fib(a-2);
//       return sum;
// }

// #include<stdio.h>
// int main(void)
// {
//     extern float PI;
//     float radius,area;

//     printf("请输入圆的半径：");
//     scanf("%f",&radius);

//     area=radius*radius*PI;
//     printf("圆的面积：%f",area);

//     return 0;

// }
// float PI=3.1415926;

// #include<stdio.h>
// #define BJ "nb"
// int main(void)
// {
//     printf("binjie,");
//     printf(BJ);
//     printf("!");

//     return 0;
// }


// #include<stdio.h>
// #define C(F) (F-32)*5/9

// int main(void)
// {
//     int Ft;

//     printf("请输入华氏温度：");
//     scanf("%d",&Ft);
//     printf("%d华氏度等于%d摄氏度",Ft,C(Ft));

//     return 0;
// }

// #include<stdio.h>
// #include<stdlib.h>
// #define User 1

// #if User==1
//  #define Max(a,b)(a>b?a:b)
// #endif
// int main(void)
// {
//     int x,y;
//     printf("请输入两个数比较大小：");
//     scanf("%d %d",&x,&y);

//     printf("最大值：%d",Max(x,y));

//     return 0;
// }

// #include<stdio.h>
// #define OFF 2
// int main(void)
// {
//     #ifndef ON 
//     #define ON 1
//     #endif

//     #ifndef OFF
//     #define OFF 3
//     #endif

//     printf("%d,%d",ON,OFF);
// }


// #include<stdio.h>

// int square(int);

// int main(void)
// {
//     int x,y;
//     printf("请输入一个数字：");
//     scanf("%d",&x);

//     printf("%d^2:%d",x,square(x));

//     return 0;
// }
// int square(int x)
// {
//     int y;
//     y=x*x;
//     return y;
// }

// #include<stdio.h>
// int cubic(int);
// int F(int);

// int main(void)
// {
//     int x;
//     printf("请输入数字：");
//     scanf("%d",&x);

//     printf("%d^2=%d\n",x,cubic(x));
//     printf("4*%d^3 +12*%d^2 -100=%d\n",x,x,F(x));

//     return 0;
// }

// int cubic(int x)
// {
//     int y;
//     y=x*x*x;
//     return y;
// }
// int F(int x)
// {
//     int y;
//     y=4*cubic(x)+12*x*x-100;

//     return y;
// }

// #include<stdio.h>
// #define Max(a,b) (a>b?a:b)

// int main(void)
// {
//     int a,b;
//     printf("请输入两个数（用逗号隔开）:");
//     scanf("%d,%d",&a,&b);
//     printf("Max:%d",Max(a,b));

//     return 0;
// }

/*英尺英寸换算*/
// #include<stdio.h>

// void transfer(float*,float*);

// int main()
// {
//     float foot,inch;
//     printf("请输入英尺及英寸的值：");
//     scanf("%f %f",&foot,&inch);
//     printf("%.0f英尺 %.0f英寸=",foot,inch);
//     transfer(&foot,&inch);/*传址调用*/
//     printf("%.0f米 %.2f厘米\n",foot,inch);

//     return 0;
// }

// void transfer(float*x,float*y)
// {
//     float result;
//     result=(*x*12+*y)*2.54;
//     *x=(int)result/100;
//     *y=result-*x*100;
// }

/*传址和传址函数计算加权平均数*/
// #include<stdio.h>
// void score(int a,int b,int c,float*d);

// int main(void)
// {
//     int math,eng,chi;
//     float weight=1.0;
//     printf("请输入成绩数语英：");
//     scanf("%d,%d,%d",&math,&eng,&chi);
//     printf("---------------------------------\n");
//     printf("原本成绩(数语英):%d  %d  %d\n",math,eng,chi);
//     score(math,eng,chi,&weight);
//     printf("----------------------------------\n");
//     printf("加权分数:数学： %.1f,英语： %.1f,语文： %.1f",weight*math,weight*eng,weight*chi);

//     return 0;

// }
// void score(int a,int b,int c,float*d)
// {
//     float average=(a+b+c)/3;

//     if(average>=90)
//       *d=1.1;
//     else if(average>=80)
//       *d=1.07;
//     else if(average>=70)
//       *d=1.03;

// }

// #include<stdio.h>
// #include<stdlib.h>
// #include"function package.h"

// int main(void)
// {
//   int i,n;
//   float sum;

//   printf("请输入n的值:");
//   scanf("%d",&n);

//   for(i=1;i<=n;i++)
//   {
//     sum+=(float)factorial(i)/square(i);
//     printf("%d!/%d^2",i,i);
//     if(i<n)
//     printf("+");
//   }
//   printf("=%f",sum);

//   return 0;
// }


// #include<stdio.h>
// float add(void);
// int main(void)
// {
//   printf("%f",add());
//   return 0;
// }
// float add(void)
// {
//   float a=8.2,b=6.6;
//   return(a+b);
// }

// #define MUL(a) a*a*a
// int main(void)
// {
// int i=5;
// printf("%d",MUL(i++));
// }

// #include<stdio.h>
// #include<stdlib.h>
// int main(void)
// {
//   int i,Score[5]={8,34,24};
//   for(i=0;i<=5;i++)
//   printf("Score[%d]=%d\n",i,Score[i]);

//   return 0;
// }

// #include<stdio.h>
// #include<stdlib.h>

// int main(void)
// {
//   int i,Score[5]={1,2,3,4,5},total=0;
//   for(i=0;i<=4;i++)
//   {
//   printf("第%d位同学分数:%d\n",i+1,Score[i]);
//   total+=Score[i];
//   }
//   printf("---------------------\n");
//   printf("总分:%d",total);

//   return 0;



//}

// #include<stdio.h>
// int main(int argc,char *argv[])
// {
//   int i;
//   if(argc==1)
//     printf("未指定参数");
//   else
//   {
//     printf("number:%d\n",argc-1);
//     printf("namelist:\n");
//     for(i=1;i<argc;i++)
//     printf("%s\n",argv[i]);
//   }
//   return 0;

// }

// #include<stdio.h>
// int main()
// {
//   int i;
//   int Tel_fee[3][2]={1234,23,1345,22,3244,25,2431,42};

//   printf("--电话号码--\n");
//   for(i=0;i<3;i++)
//   {
//     printf("%d    %d元\n",Tel_fee[i][0],Tel_fee[i][1]);
//     printf("---------------------\n");

//   }
//   return 0;
// }

// #include<stdio.h>
// int main()
// {
//   int Score[2][4]={77,75,83,92,38,29,28,89,};
//   int i,j,total;

//   for(i=0;i<2;i++)
//   {
//     total=0;
//     for(j=0;j<4;j++)
//     {
//       printf("第%d组成绩:%d\n",i+1,Score[i][j]);
//       total+=Score[i][j];
//     }
    
//     printf("第%d组的总成绩:%d\n",i+1,total);
//     printf("-----------------------------\n");
//     printf("\n");
//   }
//   return 0;
// }

// #include<stdio.h>
// int main(void)
// {
//   int arr[2][2];
//   int sum;
//   printf("|a1 b1|\n");
//   printf("|a2 b2|\n");

//   printf("请输入a1:");
//   scanf("%d",&arr[0][0]);
//   printf("请输入b1:");
//   scanf("%d",&arr[0][1]);
//   printf("请输入a2:");
//   scanf("%d",&arr[1][0]);
//   printf("请输入b2:");
//   scanf("%d",&arr[1][1]);

//   sum=arr[0][0]*arr[1][1]-arr[1][0]*arr[0][1];
//   printf("|%d %d|\n",arr[0][0],arr[0][1]);
//   printf("|%d %d|\n",arr[1][0],arr[1][1]);
//   printf("sum=%d",sum);

//   return 0;
// }


// #include<stdio.h>
// #define SIZE 6
// void Multiple(int arr[]);

// int main(void)
// {
//   int i,A[SIZE]={1,2,3,4,5,6};

//   printf("调用函数前:");
//   for(i=0;i<SIZE;i++)
//   {
//     printf("%d ",A[i]);
    

//   }
//   printf("\n");
//   Multiple(A);
//   printf("调用后:");
  

//   for(i=0;i<SIZE;i++)
//     printf("%d ",A[i]);
//   printf("\n");

//   return 0;


// }
// void Multiple(int arr[])
// {
//   int i;
//   for(i=0;i<SIZE;i++)
//     arr[i]*=2;
// }

// #include<stdio.h>
// int main()
// {
//     printf("hello,world!");
//     return 0;
// }

// #include <stdio.h>  
// #include <math.h>  
  
// int main() {  
//     int a, b, i, j, k, n, sum,temp;  
  
//     printf("请输入区间[a, b]的左右端点：");  
//     scanf("%d %d", &a, &b);  
  
//     printf("区间[%d, %d]内的水仙花数为：\n", a, b);  
  
//     for (i = a; i <= b; i++) 
//     {  
//         n = 0;  
//         sum = 0;  
//         temp = i;  
//         while (temp != 0) //判断是几位数
//         {  
//             n++;  
//             temp = temp / 10;  
//         }  
//         temp = i;  
//         while (temp != 0) 
//         {  
//             k = temp % 10;  
//             sum = sum + pow(k, n);  
//             temp = temp / 10;  
//         }  
//         if (i == sum) 
//         {  
//             printf("%d\n", i);  
//         }  
//     }  
  
//     return 0;  
// }


// #include<stdio.h>
// int main()
// {
//   int m=0256,n=256;
//   printf("%o %o\n",m,n);
  
// }

// #include <stdio.h>
// int a [101],n;
// void quicksort (int left ,int right)
// {
//     int i,j,t,temp;
//     if (left>right)
//     return  ;
//     temp=a[left];
//     i=left;
//     j=right;
//     while (i!=j)
//     {
//         while(a[j]>=temp &&i<j)
//         j--;
//         while (a[i]<=temp &&i<j)
//         i++;
//         if (i<j)
//         {
//             t=a[i];
//             a[i]=a[j];
//             a[j]=t;
//         }
//     }
//     a[left]=a[i];
//     a[i]=temp;
//     quicksort (left,i-1);
//     quicksort (i+1,right);
// }
// int main()
// {
//     int i,j,t;
//     scanf("%d",&n);
//     for(i=1;i<=n;i++)
//     scanf ("%d",&a[i]);
//     quicksort (1,n);
//     for (i=1;i<=n;i++)
//     printf ("%d ",a[i]);
//     getchar ();
//     getchar ();
//     return 0;
// }
// #include<stdio.h>
// int main()
// {
//     printf("hello,world");
//     return 0;
// }



// #include<stdio.h>
// #include<math.h>
// int main(void)
// {
//     int i;
//     for(i=2;i==0;)
//     printf("%d",i--);
//     return 0;
// }

// #include<stdio.h>
// int main()
// {
//     int x=0,y;
//     if(x!=0)y=1;
//     else y=2;
//     printf("%d",y);
// }
   
// #include<stdio.h>
// int main()
// {
//     int x=0,y;
//     if(!x)y=1;
//     else y=2;
//     printf("%d",y);
// }
// #include<stdio.h>
// int main()
// {
//     int i=2;
    
//     printf("%d",i%3);
// }

// #include<stdio.h>
// int main()
// {
//     int num1=10;
//     int num2=20;
//     int *ptr;

//     ptr=&num1;
//     printf("num1=%d\t *ptr=%d\t ptr=%p\t&num1=%p\n",
//     num1,*ptr,ptr,&num1);
// }

// #include<stdio.h>
// int main()
// {
// 	int a[8]={6,12,18,42,44,52,67,94},i,m,low,high,mid;
// 	printf("输入一个要查找的数据：");
// 	scanf("%d",&m);
// 	low=0,high=7;
// 	while(low<high)
// 	{
// 		mid=(low+high)/2;
// 		if(m==a[mid]) break;
// 		else if(m<a[mid]) high=mid-1;
// 		else low=mid+1;
// 	}
// 	if(low<=high)
// 		printf("%d是数组中第%d个元素\n",m,mid+1);
// 	else
// 		printf("%d不在数组中\n",m);
// }

// #include<stdio.h>
// int main()
// {
// int Temp[][3]={{1,2,3},{23,4,5},{2,6,8}};
// int i,j;
// for(i=0;i<3;i++)
// {
//     for(j=0;j<3;j++)
//     {
//         printf("%d ",Temp[i][j]);
//     }
// }
    
// return 0;
// }

// #include<stdio.h>
// int main()
// {
//     int arr[3],i;
//     scanf("%d %d %d",&arr);
//     for(i=0;i<3;i++)
//     {
//     printf("%d",arr[i]);
//     }
// }

// #include<stdio.h>  
// int main()  
// {  
//     int arr[3], i;  
//     scanf("%d %d %d", arr);  
//     for(i = 0; i < 3; i++)  
//     {  
//         printf("%d ", arr[i]);  
//     }  
//     return 0;  
// }