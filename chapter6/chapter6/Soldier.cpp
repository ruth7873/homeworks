#include "Soldier.h"
Soldier::Soldier(int identity, string name, string familyName, int num_campaigns_participated) :identity(identity), name(name), familyName(familyName), num_campaigns_participated(num_campaigns_participated) {}
Soldier::~Soldier() {

}
void Soldier::print() {
	cout << this->soldierType()<<endl;
	cout << "identity: " << identity << endl;
	cout << "name: " << name << endl;
	cout << "family-name: " << familyName << endl;
	cout << "num campaigns participated: " << num_campaigns_participated << endl;
}
void Soldier::add(Soldier& s) {
	cout << "enter id, first name, last name and number of operations"<<endl;
	cin >> s.identity >> s.name >> s.familyName >> s.num_campaigns_participated;
}
