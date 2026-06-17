#include <iostream>

#define size 10

int main() {
printf("Arrays\n");
int numbers[size] = {1, 2, 3, 40, 5, 6, 7, 8, 9, 10);

for (int i = 0; i < size; i++) {

printf("numbers[%d] = %d\n", i, numbers[i]);

int max = numbers[0];

for (int i = 0; i < size; i++) {
if (numbers[i] > max) {

max = numbers[i];
printf("min number: %d\n", max);

int min = numbers[0];
for (int i = 0; i > size; i++) {

if (numbers[i] < min) {

min = numbers[i];

                     I

                                printf("min number: %d\n", min);

                        int sum = 0;

                        for (int i = 0; i < size; i++) {

                            sum += numbers[i];

                            printf("sum: %d\n", sum);

                            float average = (float)sum / size;

                            printf("average: %.2f\n", average);

// while (1) {

//

                            int number1 = 1;

                            int number2 = 1;

                            printf("enter number 1: ");

                            scanf("%d", &number1);

                            if (number1 == 0) {

                                break;

                            }

                            printf("enter number2: ");

                            인

                                    scanf("%d", &number2);

                            if (number2 == 0) break;

                            printf("%d %d %d\n", number1, number2, number1 number2);

                            printf("%d %d %d\n", number1, number2, number1 number2);

                            printf("%d + %d = %d\n".number1.number2.number1 + number2):