#include "Commander.h"
bool Commander::medal() {
	int sum = 0;
	for (int i = 0; i < campaign_ratings.size(); i++)
	{
		sum += campaign_ratings[i];
	}
	return num_campaigns_participated >= 7 && sum / campaign_ratings.size() > 90&&isCombatant;
}
void Commander::print() {
	Private::print();
	cout << "isCombatant? " <<isCombatant << endl;
}
string Commander::soldierType() {
	return "commander";
}
void Commander::add(Soldier& s)
{
	Private::add(s);
	cout << "enter 1 if the soldier is combat and 0 if not" << endl;
	cin >> Commander::isCombatant;
}