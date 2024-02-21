#include "Triangle.h"
Triangle::Triangle() :Shape(3) {}
bool Triangle::isSpecial() const {
	if (numOfPoints == 3) {
		double side1 = calcSideLength(*(points[1]), *(points[0]));
		double side2 = calcSideLength(*(points[2]), *(points[1]));
		double side3 = calcSideLength(*(points[0]), *(points[2]));
		return side1 == side2 == side3;
	}
	return false;
}
//double Triangle::calcSideLength(const Shape::Point& point1, const Shape::Point& point2)const {
//	return std::sqrt(std::pow(point1.getX() - point2.getX(), 2) + std::pow(point1.getY() - point2.getY(), 2));
//}
void Triangle::printSpecial()const {
	if (isSpecial())
		std::cout << "An isosceles triangle with a side length " << calcSideLength(*(points[1]), *(points[0])) << "\n";
}
float Triangle::area()const {
	double a = calcSideLength(*(points[1]), *(points[2]));
	double b = calcSideLength(*(points[0]), *(points[2]));
	double c = calcSideLength(*(points[0]), *(points[1]));

	double angleC = std::acos((a * a + b * b - c * c) / (2 * a * b));

	double area = 0.5 * a * b * std::sin(angleC);

	return area;
}