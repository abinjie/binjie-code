int square(int x)/*平方函数*/
{
    x*=x;
    return x;
}

int factorial(int i)/*阶乘函数*/
{
    int sum;
    if(i==0)
    return (1);
    else
    sum=i*factorial(i-1);
    return sum;

}