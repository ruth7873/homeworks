#include "Officer.h"
bool Officer::medal() {
	return num_campaigns_participated > 2 && sociometricScore >= 92;
}
void Officer::print() {
	Soldier::print();
	cout << "performanceRating: " << sociometricScore << endl;
}
string Officer::soldierType() {
	return "officer";
}
void Officer::add(Soldier& s)
{
	Soldier::add(s);
	cout << "enter number of sociometric score" << endl;
	cin >> sociometricScore;
}