#include "Rectangle.h"
Rectangle::Rectangle() :Shape(4) {}
bool Rectangle::isSpecial() const {
	if (numOfPoints == 4) {
		double side1 = calcSideLength(*(points[0]), *(points[1]));
		double side2 = calcSideLength(*(points[1]), *(points[2]));
		double side3 = calcSideLength(*(points[2]), *(points[3]));
		double side4 = calcSideLength(*(points[3]), *(points[0]));
		return side1 == side2&&side1 == side3&&side1 == side4;
	}
	return false;
}
//double Rectangle::calcSideLength(const Shape::Point& point1, const Shape::Point& point2)const {
//	return std::sqrt(std::pow(point1.getX() - point2.getX(), 2) + std::pow(point1.getY() - point2.getY(), 2));
//}
void Rectangle::printSpecial()const {
	if (isSpecial())
		std::cout << "Square with a side length " << calcSideLength(*(points[1]), *(points[0])) << "\n";
}
float Rectangle::area()const {
	double a = calcSideLength(*(points[1]), *(points[2]));
	double b = calcSideLength(*(points[0]), *(points[1]));

	return a * b;
}