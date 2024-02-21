//// lesson4_ruthHershler.cpp : This file contains the 'main' function. Program execution begins and ends there.
////
//
#include <iostream>
#include "Shape.h"
#include "Circle.h"
#include "Triangle.h"
#include "Rectangle.h"
using namespace std;

int main()
{
    cout << "How many shapes do you want to define?\n";
    int numShapes,choose;
    cin >> numShapes;
    
    Shape** shapes = new Shape * [numShapes];
    for (int i = 0; i < numShapes; i++)
    {
        cout << "Which shape will you choose? Circle - 1,Triangle -3 , Rectangle - 4\n";
        cin >> choose;
        switch (choose)
        {
        case 1:
            float radius;
            cout << "Enter radius\n";
            cin >> radius;
            shapes[i] = new Circle(radius);
            break;
        case 3:
            shapes[i] = new Triangle();
            break;
        case 4:
            shapes[i] = new Rectangle();
            break;
        default:
            cout << "invalid input";
            i = i - 1;
        }
    }
    for (int i = 0; i < numShapes; i++)
    {
        cout << *shapes[i] << " area is: " << shapes[i]->area() << " ";
        shapes[i]->printSpecial();
        cout << "\n";
    }


}
//
//// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
//// Debug program: F5 or Debug > Start Debugging menu
//
//// Tips for Getting Started: 
////   1. Use the Solution Explorer window to add/manage files
////   2. Use the Team Explorer window to connect to source control
////   3. Use the Output window to see build output and other messages
////   4. Use the Error List window to view errors
////   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
////   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
