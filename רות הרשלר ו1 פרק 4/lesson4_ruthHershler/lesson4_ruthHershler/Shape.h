#pragma once
#include <iostream>
class Shape
{
public:
	class Point
	{
		int x, y;
	public:
		Point();
		Point(const Shape::Point& o);
		void setX(int x);
		int getX()const;
		void setY(int y);
		int getY()const;
		friend std::istream& operator>>(std::istream& lhs, Shape::Point& rhs);
		friend std::ostream& operator<<(std::ostream& lhs, const Shape::Point& rhs);
	};
	Shape();
	Shape(int numPoints);
	Shape(const Shape& l);//copy ctor
	Shape(Shape&& sh);//move ctor
	virtual ~Shape();
	friend std::ostream& operator<<(std::ostream& lhs, const Shape& rhs);
	virtual float area()const = 0;
	virtual bool isSpecial()const = 0;
	virtual void printSpecial()const = 0;
	double calcSideLength(const Shape::Point& point1, const Shape::Point& point2) const;


protected:
	int numOfPoints;
	Shape::Point** points;
};