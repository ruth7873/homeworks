#pragma once
#include "Shape.h"
class Triangle:public Shape
{
private:
//double calcSideLength(const Shape::Point& point1, const Shape::Point& point2) const; 
public:
	Triangle();
	bool isSpecial()const override;
	void printSpecial()const override;
	float area()const override;
};

