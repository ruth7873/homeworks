#include "Shape.h"
#include <string>
using namespace std;
Shape::Point::Point() {}
Shape::Point::Point(const Shape::Point& o)
{
	x = o.x;
	y = o.y;
}
void Shape::Point::setX(int x1) {
	x = x1;
}
void Shape::Point::setY(int y1) {
	y = y1;
}
int Shape::Point::getX() const { return x; }
int Shape::Point::getY() const { return y; }
std::istream& operator>>(std::istream& lhs, Shape::Point& rhs) {
	cout << "enter (x,y)\n";
	std::string str;
	lhs >> str;
	int index = str.find(',');
	if (index >= 0)
	{
		std::string part1 = str.substr(0, index); // החלק הראשון מתחיל באינדקס 0 ונמשך עד למיקום של התו המפריד
		std::string part2 = str.substr(index + 1); // החלק השני מתחיל מהאינדקס הבא לתו המפריד ונמשך עד סוף המחרוזת
		rhs.x =std::stoi(part1);
		rhs.y =std::stoi(part2);
	}
	else
	{
	cout << "not valid";
	exit(1);
	}
	return lhs;	
}
std::ostream& operator<<(std::ostream& lhs, const Shape::Point& rhs) {
	lhs <<"("<< rhs.x <<"," << rhs.y<<") ";
	return lhs;
}
Shape::Shape() :numOfPoints(0) {}
Shape::Shape(int numPoints) :numOfPoints(numPoints)
{
	points = new Point* [numOfPoints];
	cout << "enter values of " << numOfPoints << " point\n";
	for (int i = 0; i < numOfPoints; i++)
	{
		points[i] = new Point;
		cin >> *(points[i]);
	}
}
Shape::Shape(const Shape& l)
{
	//Link* src, * trg;
	if (l.points == nullptr)
		points = nullptr;
	else
	{
		numOfPoints = l.numOfPoints;
		points = new Point * [numOfPoints];

		for (int i = 0; i < numOfPoints; i++)
		{
			points[i] = new Point(*(l.points[i]));
		}
	}
}
Shape::Shape(Shape&& sh)
{
	numOfPoints = sh.numOfPoints;
	points = sh.points;
	sh.points = nullptr;
}
Shape::~Shape() {
	if (points)
	{
		for (int i = 0; i < numOfPoints; i++)
		{
			delete points[i];
		}
		delete points;
	}
}

std::ostream& operator<<(std::ostream& lhs, const Shape& rhs) {
	lhs << "Points: ";
	for (int i = 0; i < rhs.numOfPoints; i++) {
		cout<<*(rhs.points[i]);
	}
	lhs << std::endl;
	return lhs;
}
double Shape::calcSideLength(const Shape::Point& point1, const Shape::Point& point2)const {
	return std::sqrt(std::pow(point1.getX() - point2.getX(), 2) + std::pow(point1.getY() - point2.getY(), 2));
}