#include <iostream>
#include <stdio.h>
#include <math.h>

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

void power(double num1, double num2)
{
    cout << "Answer : " << pow(num1, num2) << endl;
}

void sqroot(double num1)
{
    cout << "Answer : " << sqrt(num1) << endl;
}

void cbroot(double num1)
{
    cout << "Answer : " << cbrt(num1) << endl;
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
    if(! (op == 's' || op == 'c'))
    {
        cout << "Enter a number : \n";
        cin >> num2;
    }

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
    } else if(op == '^') {
        power(num1, num2);
    } else if(op == 's') {
        sqroot(num1);
    } else if(op == 'c') {
        cbroot(num1);
    } else {
        cout << "Invalid operator... +, -, *, /, ^, s (for sqrt) or c (for cbrt) expected." << endl;
        return;
    }
}

int main(void)
{
    calc();

    return 0;
}
