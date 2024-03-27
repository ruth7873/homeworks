#pragma once
#include <string>
#include <iostream>
using namespace std;
class Soldier
{
public:
	int identity;
	string name;
	string familyName;
	int num_campaigns_participated;
	Soldier(int identity, string name, string familyName, int num_campaigns_participated);
	Soldier() {}
	virtual ~Soldier();
	virtual bool medal() = 0;
	virtual void print();
	virtual string soldierType() = 0;
	virtual void add(Soldier& s);
	virtual int getSociometricScore() { throw "ERROR: this function is just for officer soldier"; };
	string getFname() { return familyName; }
	string getName() { return name; }
};