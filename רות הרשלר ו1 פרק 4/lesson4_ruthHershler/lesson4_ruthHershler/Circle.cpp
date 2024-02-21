#include "Circle.h"
Circle::Circle(float rad) :Shape(1), radius(rad) {

}
//void Circle::setRadius(int x) {
//	radius = x;
//}
//int Circle::getRadius() {
//	return radius;
//}
bool Circle::isSpecial() const {
	if (numOfPoints > 0 && points[0] != nullptr) {
		return points[0]->getX() == 0 && points[0]->getY() == 0;
	}
	return false;
}
void Circle::printSpecial()const {
	if (isSpecial())
		std::cout << "A canonical circle with a radius " << radius << "\n";
}
float Circle::area()const {
	return M_PI * radius * radius;
}
