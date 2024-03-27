#pragma once
#include "Private.h"
class Commander :public Private
{
private:
	bool isCombatant;
public:
	Commander() {}
	Commander(int identity, string name, string familyName, int num_campaigns_participated, vector<int>campaign_ratings, bool isCombatant)
		: Private(identity, name, familyName, num_campaigns_participated, campaign_ratings), isCombatant(isCombatant) {}
	bool medal() override;
	void print() override;
	string soldierType() override;
	void add(Soldier& s)override;
	bool getIsComBatant() { return isCombatant; }
};