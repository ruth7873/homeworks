#pragma once
#include <iostream>
#include <string>
using namespace std;
class Book
{
private:
	int code;
	string author;
	string bookName;
public:
	Book() :code(0), author(""), bookName("") {}

	friend std::ostream& operator<<(std::ostream& lhs, const Book& rhs);
	friend std::istream& operator>>(std::istream& lhs, Book& rhs);

	friend bool operator==(const Book& lhs, const Book& rhs);
	friend bool operator!=(const Book& lhs, const Book& rhs);
	friend bool operator<(const Book& lhs, const Book& rhs);
	friend bool operator<=(const Book& lhs, const Book& rhs);
	friend bool operator>(const Book& lhs, const Book& rhs);
	friend bool operator>=(const Book& lhs, const Book& rhs);
};