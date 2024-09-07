#define _CRT_SECURE_NO_WARNINGS 1
#pragma warning(disable : 6031)
//头文件的包含
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <windows.h>
//全局变量
#define ROW 3
#define COL 3
 
//函数的声明
//菜单
void menu();
//游戏模块
void game(void);
//初始化棋盘
void init(char board[ROW][COL], int row, int col);
//打印棋盘
void print(char board[ROW][COL], int row, int col);
//玩家A下棋
void playerA(char board[ROW][COL], int row, int col);
//玩家B下棋
void playerB(char board[ROW][COL], int row, int col);
//判断输赢
char judge(char board[ROW][COL], int row, int col);
//判断棋盘是否满
int IsFull(char board[ROW][COL], int row, int col);
//电脑进攻函数
int attack(char boatd[ROW][COL], int row, int col);
//电脑防守函数
int defense(char board[ROW][COL], int row, int col);