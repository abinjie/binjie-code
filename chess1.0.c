#include <stdio.h>

#define SIZE 3

void printBoard(char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}

int checkWin(char board[SIZE][SIZE], char player) {
    // Check rows and columns
    for (int i = 0; i < SIZE; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
            return 1;
        }
    }
    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
        return 1;
    }
    return 0;
}

int isBoardFull(char board[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                return 0;
            }
        }
    }
    return 1;
}

void playerMove(char board[SIZE][SIZE]) {
    int row, col;
    while (1) {
        printf("Enter your move (row and column): ");
        scanf("%d %d", &row, &col);
        if (row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == ' ') {
            board[row][col] = 'O';
            break;
        } else {
            printf("Invalid move. Try again.\n");
        }
    }
}

void computerMove(char board[SIZE][SIZE]) {
    // Simple AI to block player's win and take win if available
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                board[i][j] = 'X';
                if (checkWin(board, 'X')) {
                    return;
                }
                board[i][j] = 'O';
                if (checkWin(board, 'O')) {
                    board[i][j] = 'X';
                    return;
                }
                board[i][j] = ' ';
            }
        }
    }
    // If no win or block, take first available spot
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j] == ' ') {
                board[i][j] = 'X';
                return;
            }
        }
    }
}

void computerFirstMove(char board[SIZE][SIZE]) {
    int row, col;
    while (1) {
        printf("Enter the computer's first move (row and column): ");
        scanf("%d %d", &row, &col);
        if (row >= 0 && row < SIZE && col >= 0 && col < SIZE && board[row][col] == ' ') {
            board[row][col] = 'X';
            break;
        } else {
            printf("Invalid move. Try again.\n");
        }
    }
}

int main() {
    char board[SIZE][SIZE] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };
    
    printf("Welcome to Tic Tac Toe!\n");
    printBoard(board);
    
    // Let user specify computer's first move
    computerFirstMove(board);
    printBoard(board);

    while (1) {
        if (checkWin(board, 'X')) {
            printf("机器赢\n");
            break;
        }
        if (isBoardFull(board)) {
            printf("平局！\n");
            break;
        }

        playerMove(board);
        printBoard(board);
        if (checkWin(board, 'O')) {
            printf("你赢\n");
            break;
        }
        if (isBoardFull(board)) {
            printf("平局！\n");
            break;
        }

        computerMove(board);
        printf("Computer's move:\n");
        printBoard(board);
    }
    
    return 0;
}
