#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable : 6031)
#include "game.h"
 
int ret = 0;
void game(void)
{
    //设置二维数组
    char board[ROW][COL];
    //初始化棋盘
    init(board, ROW, COL);
    //打印棋盘
    print(board, ROW, COL);
    printf("--------游戏开始——---———\n");
    printf("\n");
    //人机对弈
    int tmp = rand() % 2;
    if (0 == tmp)        //玩家下棋
    {
        while (1)
        {
            //玩家下棋+判断
            playerA(board, ROW, COL);
            print(board, ROW, COL);
            ret = judge(board, ROW, COL);
            if (ret != 'C')
            {
                break;
            }
            //电脑下棋+判断
            int a = attack(board, ROW, COL);
            if (0 == a)
            {
                int d = defense(board, ROW, COL);
                if (0 == d)
                {
                    playerB(board, ROW, COL);
                    print(board, ROW, COL);
                }
                else
                {
                    print(board, ROW, COL);
                }
            }
            else
            {
                print(board, ROW, COL);
            }
            ret = judge(board, ROW, COL);
            if (ret != 'C')
            {
                break;
            }
        }
    }
    else            //电脑下
    {
        while (1)
        {
            int a = attack(board, ROW, COL);
            if (0 == a)
            {
                int d = defense(board, ROW, COL);
                if (0 == d)
                {
                    playerB(board, ROW, COL);
                    print(board, ROW, COL);
                }
                else
                {
                    print(board, ROW, COL);
                }
            }
            else
            {
                print(board, ROW, COL);
            }
            ret = judge(board, ROW, COL);
            if (ret != 'C')
            {
                break;
            }
            //玩家下棋+判断
            playerA(board, ROW, COL);
            print(board, ROW, COL);
            ret = judge(board, ROW, COL);
            if (ret != 'C')
            {
                break;
            }
        }
    }
 
    if ('*' == ret)
    {
        printf("你侥幸获胜了\n");
        printf("准备下一把\n");
    }
    else if ('#' == ret)
    {
        printf("你居然打不赢电脑\n");
        printf("准备下一把\n");
    }
    else if ('Q' == ret)
        printf("平局\n");
}
 
//初始化棋盘
void init(char board[ROW][COL], int row, int col)
{
    int i = 0;
    int j = 0;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            board[i][j] = ' ';
        }
    }
    //初始化一块空间，首元素地址知道了，初始为什么呢？初始化多少字节呢？
    memset(&board[0][0], ' ', row * col * sizeof(board[0][0]));
}
 
//打印棋盘
void print(char board[ROW][COL], int row, int col)
{
    int i = 0;
    for (i = 1; i <= 3; i++)
    {
        printf("%d   ", i);
    }
    printf("\n");
    for (i = 0; i < row; i++)
    {
        int j = 0;
        //数据的打印
        for (j = 0; j < col; j++)
        {
            printf(" %c ", board[i][j]);
            if (j < col - 1)
                printf("|"); //1个数据打印完后，打印|
        }
        printf("%d", i + 1);
        printf("\n");
        //分割行的打印
        if (i < row - 1)
        {
            for (j = 0; j < col; j++)
            {
                printf("___");
                if (j < col - 1)
                    printf("|");
            }
        }
        printf("\n");
    }
}
 
//pA下棋
void playerA(char board[ROW][COL], int row, int col)
{
    printf("到你的回合了\n");
    int x = 0;
    int y = 0;
    while (1)
    {
        printf("请输入你要下的坐标： ");
        scanf("%d %d", &x, &y);
        if (x > 0 && x <= row && y > 0 && y <= col)
        {
            if (board[x - 1][y - 1] == ' ')
            {
                board[x - 1][y - 1] = '*';
                break;
            }
            else
                printf("坐标被占用，请重新选择\n");
        }
        else
        {
            printf("输入值越界，请输入3*3坐标\n");
        }
    }
}
 
//pB下棋
void playerB(char board[ROW][COL], int row, int col)
{
    int x = 0;
    int y = 0;
    printf("电脑下棋\n");
    while (1)
    {
        x = rand() % row;
        y = rand() % col;
        if (board[x][y] == ' ')
        {
            board[x][y] = '#';
            break;
        }
    }
}
 
//判断输赢
//*为玩家
//#为电脑
//Q为平局
//C为继续
char judge(char board[ROW][COL], int row, int col)
{
    int i = 0;
    for (i = 0; i < row; i++)
    {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ')
        {
            return board[i][0];
        }
    }
    for (i = 0; i < col; i++)
    {
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ')
        {
            return board[0][i];
        }
    }
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ')
    {
        return board[0][0];
    }
    if (board[0][2] == board[1][1] && board[2][1] && board[0][2] != ' ')
    {
        return board[0][2];
    }
    if (IsFull(board, row, col))
    {
        return 'Q';
    }
    else
        return 'C';
}
 
//判断棋盘是否满
int IsFull(char board[ROW][COL], int row, int col)
{
    int i = 0;
    int j = 0;
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
        {
            if (board[i][j] == ' ')
                return 0;
        }
    }
    return 1;
}
 
//电脑进攻函数 q=0随机下 q=1进攻
int attack(char board[ROW][COL], int row, int col)
{
    int q = 0;
    int i = 0;
    //判断行是否有机会
    for (i = 0; i < row; i++)
    {
        if (board[i][0] == board[i][1] && board[i][0] == '#' && board[i][2] == ' ')
        {
            board[i][2] = '#';
            q = 1;
            return q;
        }
        if (board[i][0] == board[i][2] && board[i][0] == '#' && board[i][1] == ' ')
        {
            board[i][1] = '#';
            q = 1;
            return q;
        }
        if (board[i][1] == board[i][2] && board[i][1] == '#' && board[i][0] == ' ')
        {
            board[i][0] = '#';
            q = 1;
            return q;
        }
    }
    //判端列是否有机会
    for (i = 0; i < col; i++)
    {
        if (board[0][i] == board[1][i] && board[0][i] == '#' && board[2][i] == ' ')
        {
            board[2][i] = '#';
            q = 1;
            return q;
        }
        if (board[0][i] == board[2][i] && board[0][i] == '#' && board[1][i] == ' ')
        {
            board[1][i] = '#';
            q = 1;
            return q;
        }
        if (board[1][i] == board[2][i] && board[1][i] == '#' && board[0][i] == ' ')
        {
            board[0][i] = '#';
            q = 1;
            return q;
        }
    }
    //判断正对角线是否有机会
    if (board[0][0] == board[1][1] && board[0][0] == '#' && board[2][2] == ' ')
    {
        board[2][2] = '#';
        q = 1;
        return q;
    }
    if (board[0][0] == board[2][2] && board[0][0] == '#' && board[1][1] == ' ')
    {
        board[1][1] = '#';
        q = 1;
        return q;
    }
    if (board[2][2] == board[1][1] && board[2][2] == '#' && board[0][0] == ' ')
    {
        board[0][0] = '#';
        q = 1;
        return q;
    }
    //判断反对角线是否有机会
    if (board[0][2] == board[1][1] && board[0][2] == '#' && board[2][0] == ' ')
    {
        board[2][0] = '#';
        q = 1;
        return q;
    }
    if (board[0][2] == board[2][0] && board[0][2] == '#' && board[1][1] == ' ')
    {
        board[1][1] = '#';
        q = 1;
        return q;
    }
    if (board[2][0] == board[1][1] && board[2][0] == '#' && board[0][2] == ' ')
    {
        board[0][2] = '#';
        q = 1;
        return q;
    }
    return q;            //不需要进攻
}
 
//电脑防守函数
int defense(char board[ROW][COL], int row, int col)
{
    int q = 0;
    int i = 0;
    //判断行是否有机会
    for (i = 0; i < row; i++)
    {
        if (board[i][0] == board[i][1] && board[i][0] == '*' && board[i][2] == ' ')
        {
            board[i][2] = '#';
            q = 1;
            return q;
        }
        if (board[i][0] == board[i][2] && board[i][0] == '*' && board[i][1] == ' ')
        {
            board[i][1] = '#';
            q = 1;
            return q;
        }
        if (board[i][1] == board[i][2] && board[i][1] == '*' && board[i][0] == ' ')
        {
            board[i][0] = '#';
            q = 1;
            return q;
        }
    }
    //判端列是否有机会
    for (i = 0; i < col; i++)
    {
        if (board[0][i] == board[1][i] && board[0][i] == '*' && board[2][i] == ' ')
        {
            board[2][i] = '#';
            q = 1;
            return q;
        }
        if (board[0][i] == board[2][i] && board[0][i] == '*' && board[1][i] == ' ')
        {
            board[1][i] = '#';
            q = 1;
            return q;
        }
        if (board[1][i] == board[2][i] && board[1][i] == '*' && board[0][i] == ' ')
        {
            board[0][i] = '#';
            q = 1;
            return q;
        }
    }
    //判断正对角线是否有机会
    if (board[0][0] == board[1][1] && board[0][0] == '*' && board[2][2] == ' ')
    {
        board[2][2] = '#';
        q = 1;
        return q;
    }
    if (board[0][0] == board[2][2] && board[0][0] == '*' && board[1][1] == ' ')
    {
        board[1][1] = '#';
        q = 1;
        return q;
    }
    if (board[2][2] == board[1][1] && board[2][2] == '*' && board[0][0] == ' ')
    {
        board[0][0] = '#';
        q = 1;
        return q;
    }
    //判断反对角线是否有机会
    if (board[0][2] == board[1][1] && board[0][2] == '*' && board[2][0] == ' ')
    {
        board[2][0] = '#';
        q = 1;
        return q;
    }
    if (board[0][2] == board[2][0] && board[0][2] == '*' && board[1][1] == ' ')
    {
        board[1][1] = '#';
        q = 1;
        return q;
    }
    if (board[2][0] == board[1][1] && board[2][0] == '*' && board[0][2] == ' ')
    {
        board[0][2] = '#';
        q = 1;
        return q;
    }
    return q;        //不需要防守
}