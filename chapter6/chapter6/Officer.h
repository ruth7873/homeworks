#pragma once
#include "Soldier.h"
class Officer:public Soldier
{private:
	int sociometricScore;
public:
	Officer() {}
	Officer(int identity, string name, string familyName, int num_campaigns_participated,int sociometricScore) :Soldier(identity, name, familyName, num_campaigns_participated), sociometricScore(sociometricScore) {}
	bool medal() override;
	void print() override;
	string soldierType() override;
	void add(Soldier& s)override;
	int getSociometricScore() override { return sociometricScore; }
};