#pragma once
#include "Shape.h"
class Rectangle:public Shape
{
private:
	//double calcSideLength(const Shape::Point& point1, const Shape::Point& point2) const;
public:
	Rectangle();
	bool isSpecial()const override;
	void printSpecial()const override;
	float area()const override;
};

