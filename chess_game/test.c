#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable : 6031)
#include "game.h" //自己的文件用""
 
void menu()
{
    printf("*******************\n");
    printf("***** 1 start *****\n");
    printf("***** 0 quit  *****\n");
    printf("*******************\n");
}
 
int main()
{
    int num = 0;
    srand((unsigned int)time(NULL));
    do
    {
        menu();
        printf("\n请根据菜单选择一个数(1/0): ");
        scanf("%d", &num);
        switch (num)
        {
        case 1:
            game();
            break;
        case 0:
            printf("quit this game...\n");
            break;
        default:
            printf("please chose one again\n");
            break;
        }
    } while (num);
    return 0;
}