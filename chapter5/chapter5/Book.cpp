#include "Book.h"

std::ostream& operator<<(std::ostream& lhs, const Book& rhs) {
	return	lhs << "code: " << rhs.code << " author: " << rhs.author << " book - name: " << rhs.bookName << endl;
}
std::istream& operator>>(std::istream& lhs, Book& rhs) {
	return	lhs >> rhs.code >> rhs.author >> rhs.bookName;
}

bool operator==(const Book& lhs, const Book& rhs) {
	return (lhs.code == rhs.code && lhs.bookName.compare(rhs.bookName) == 0 && lhs.author.compare(rhs.author) == 0);
}
bool operator!=(const Book& lhs, const Book& rhs) {
	return !(lhs == rhs);
}
bool operator<(const Book& lhs, const Book& rhs) {
	if (lhs.author != rhs.author)
		return (lhs.author.compare(rhs.author)) < 0;
	if (lhs.bookName != rhs.bookName)
		return (lhs.bookName.compare(rhs.bookName)) < 0;
	return lhs.code < rhs.code;
}
bool operator<=(const Book& lhs, const Book& rhs) {
	return !(lhs > rhs);
}
bool operator>(const Book& lhs, const Book& rhs) {
	return rhs < lhs;
}
bool operator>=(const Book& lhs, const Book& rhs) {
	return !(lhs < rhs);
}