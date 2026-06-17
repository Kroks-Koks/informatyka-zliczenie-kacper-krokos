#include <iostream>


int main() {
    while (1) {
        int number1 = 1;
        int number2 = 1;

        printf("enter number 1: ");
        scanf("%d", &number1);
        if (number1 == 0) {
            break;
        }

        printf("enter number 2: ");
        scanf("%d", &number2);
        if (number2 == 0) {
            break;
        }

        printf("%d - %d = %d\n", number1, number2, number1 - number2);
        printf("%d + %d = %d\n", number1, number2, number1 + number2);
        printf("%d * %d = %d\n", number1, number2, number1 * number2);
        printf("%d / %d = %d\n", number1, number2, number1 / number2);
    }

    return 0;
}