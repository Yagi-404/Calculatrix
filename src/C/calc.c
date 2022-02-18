#include <stdio.h>

int caclculator()
{
    double num1;
    double num2;
    char op;

    // inputs

    printf("Enter a number : ");
    scanf("%lf", &num1);
    
    printf("Enter an operator : ");
    scanf(" %c", &op);
    
    printf("Enter a number : ");
    scanf("%lf", &num2);

    if (!op) {
        printf("You try but I catch ;)\n");
        return 1;

    } else if (op == '+') {
        printf("%f\n", num1 + num2);
    } else if (op == '-') {
        printf("%f\n", num1 - num2);
    } else if (op == '*') {
        printf("%f\n", num1 * num2);
    } else if (op == '/') {
        printf("%f\n", num1 / num2);
    } else {
        printf("Please enter a valid operator...\n");
    }
    return 0;
}

int main()
{
    caclculator();
    return 0;
}