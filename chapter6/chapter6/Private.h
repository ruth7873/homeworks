#pragma once
#include "Soldier.h"
#include <vector>
class Private:public Soldier
{protected:
	vector<int>campaign_ratings;
public:
	Private() {}
	Private(int identity, string name, string familyName, int num_campaigns_participated, vector<int>campaign_ratings) :Soldier(identity, name, familyName, num_campaigns_participated), campaign_ratings(campaign_ratings) {};
	bool medal() override;
	void print() override;
	string soldierType() override;
	void add(Soldier& s)override;
};

