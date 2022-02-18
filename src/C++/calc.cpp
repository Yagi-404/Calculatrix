#include <iostream>
#include <stdio.h>

using namespace std;

void add(double num1, double num2)
{
    cout << "Answer : " << num1 + num2 << endl;
}

void substract(double num1, double num2)
{
    cout << "Answer : " << num1 - num2 << endl;
}

void multiply(double num1, double num2)
{
    cout << "Answer : " << num1 * num2 << endl;
}

void divide(double num1, double num2)
{
    cout << "Answer : " << num1 / num2 << endl;
}

void calc(void)
{
    double num1;
    double num2;
    char op;

    cout << "Enter a number :\n";
    cin >> num1;
    // cout << "Your number is " << num1 << endl;

    cout << "Enter an operator : \n";
    cin >> op;

    cout << "Enter a number : \n";
    cin >> num2;

    if(!op) {
        cout << "You TRY but I CATCH ;)";
    } else if(op == '+') {
        add(num1, num2);
    } else if(op == '-') {
        substract(num1, num2);
    } else if(op == '*') {
        multiply(num1, num2);
    } else if(op == '/') {
        divide(num1, num2);
    } else {
        cout << "Invalid operator... +, -, * or / expected." << endl;
        return;
    }
}

int main(void)
{
    calc();

    return 0;
}