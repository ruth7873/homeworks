#pragma once
#include <iostream>
#include "Shape.h"
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

class Circle :public Shape
{
	float radius;
public:
	Circle(float radius);
	//int getRadius();
	//void setRadius(int x);
	bool isSpecial()const override;
	void printSpecial()const override;
	float area()const override;

};
