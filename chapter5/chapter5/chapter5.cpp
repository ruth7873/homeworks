// chapter5.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include "QueueVector.h"
#include "SearchTree.h"
#include "Book.h"
#include <time.h>
using namespace std;
void printMenu() {
	cout << "a - add book to the library" << endl;
	cout << "b - delete book from the library" << endl;
	cout << "c - search book in the library" << endl;
	cout << "d - print all the books of the library by alphabetic order" << endl;
	cout << "e - exit" << endl;
}
Book enterBook(Book b) {
	cout << "enter a book"<<endl;
	cin >> b;
	return b;
}
int main()
{
	SearchTree<Book> library;
	char choose;
	printMenu();
	while (true)
	{
		cout << "enter a- e"<<endl;
		cin >> choose;
		Book b;
		switch (choose)
		{
		case 'a':
			b=enterBook(b);
			library.add(b);
			break;
		case 'b':
			b=enterBook(b);
			if (!library.search(b))
				cout << "not exist"<<endl;
			else library.remove(b);
			break;
		case 'c':
			b=enterBook(b);
			if (library.search(b))
				cout << "exist"<<endl;
			else
				cout << "not exist"<<endl;
				break;
		case 'd':
			library.inOrder();
			break;
		case 'e':
			exit(0);
		default: cout << "error!"<<endl;

		}
	}
	/*
	std::cout << "Hello World!\n";
	QueueVector<int> queue (10);
	srand((unsigned)time(NULL));
	try {

		for (int i = 0; i < 10; i++)
		{
			queue.enqueue(rand() % 100);
		}
	}
	catch (const std::exception& e) {
		cout << "Exception caught: " << e.what() << endl;
	}
	while (!queue.isEmpty())
	{
		cout << queue.dequeue() << " ";
	}
	cout << endl;
	try {

	cout << queue.dequeue();
	}
	catch (const std::exception& e) {
		cout << "Exception caught: " << e.what() << endl;
	}
	SearchTree<int> t;
	t.add(5);
	t.add(10);
	t.add(8);
	t.add(2);
	t.add(6);
	t.add(9);
	t.breadthScan();
	t.remove(5);
	t.breadthScan();*/

}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
