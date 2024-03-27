#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>
#include "Soldier.h"
#include "Private.h"
#include "Commander.h"
#include "Officer.h"
using namespace std;

enum option {
	stop,	//	סיום התוכנית
	addNewSoldier,	//	הוספת חייל חדש
	medalList,	//	הדפסת פרטי כל החיילים הזכאים לצל"ש
	mostSociometric,	//	הדפסת שם (משפחה ופרטי) של  החייל בעל ציון סוציומטרי מקסימלי 
	countMedalPrivate,	//	הדפסת מספר החיילים הטירוניים הזכאים לצל"ש
	noCombatCommander,	//	הדפסת שמות (משפחה ופרטי) של המפקדים שאינם בקרבי
	overSoldier,	//	הדפסת הודעה מתאימה, האם קיים חייל שהשתתף ביותר מ- 15  מבצעים צבאיים
	removeOfficer,	//	מחיקת כל החיילים הקצינים שלא השתתפו כלל במבצע צבאי
};

void add(list<Soldier*>& soldiers);  //השלם\י פרמטר- ווקטור או רשימה  
void medal(list<Soldier*>& soldiers);// קריאה לפונקציה print של כל חייל ברשימה
Soldier* mostSociometricScore(list<Soldier*>& soldiers);  //השלם\י פרמטר- ווקטור או רשימה  

int main()
{
	list<Soldier*> soldiers; // קריאה לפונקציה add עם מצביעים ל-Soldier
	// הצהרה על ווקטור או רשימה של חיילים
		int op;
	cout << "enter 0-7\n";
	cin >> op;
	while (op != stop)
	{
		switch (op)
		{
		case addNewSoldier: add(soldiers);  //הוספת חייל חדש
			break;
		case medalList: medal(soldiers);  //הדפסת פרטי הזכאים לצל"ש
			break;
		case mostSociometric: {   //הדפסת שם הקצין בעל ציון סוציומטרי גבוה ביותר 
			Soldier* s = mostSociometricScore(soldiers); // השלם\י פרמטר-וקטור או רשימה
			cout << "Officer soldier with most sociometric score: ";
			cout << s->getFname() << ' ' << s->getName() << endl;
			break;
		}
		case countMedalPrivate: {
			cout << "# private soldier for medal: ";
			cout << count_if(soldiers.begin(), soldiers.end(), [](Soldier* s) {if (s->soldierType() == "private") return s->medal(); }); //הדפסת מספר הזכאים לצל"ש בטירונים
			cout << endl;
			break;
		}
		case noCombatCommander: {
			cout << "list of no combat commander soldier :";
			//הדפסת רשימת(שם משפחה ופרטי) החיילים המפקדים שאינם בקרבי
			for_each(soldiers.begin(), soldiers.end(), [](Soldier* s) {
				if (s->soldierType() == "commander" && !((Commander*)s)->getIsComBatant())
					cout << s->getFname() << ' ' << s->getName();
				});
			cout << endl;
			break;
		}
		case overSoldier:
		{
			if (any_of(soldiers.begin(), soldiers.end(), [](Soldier* s) { return s->num_campaigns_participated > 15; })) // קיים חייל שהשתתף ביותר מ- 15 מבצעים צבאיים
				cout << "there is a soldier that takes more than 15 operations\n";
			else
				cout << "no soldier takes more than 15 operations\n";

			break;
		}
		//case removeOfficer:
		//	//מחיקה מהווקטור/רשימה של כל החיילם קצינים שאינם השתתפו כלל במבצעים צבאיים
		//{
		//	auto i = remove_if(soldiers.begin(), soldiers.end(), [](Soldier* s) {return s->soldierType() == "officer" && s->num_campaigns_participated == 0; });
		//	for_each(i, soldiers.end(), [](Soldier* s) {cout << s << ' '; });//הדפסת כל הרשימה לאחר מחיקת האיברים
		//	break;
		//}
		case removeOfficer:
		{
			// מחיקת כל החיילים קצינים שלא השתתפו במבצעים צבאיים
			soldiers.erase(remove_if(soldiers.begin(), soldiers.end(), [](Soldier* s) {
				return s->soldierType() == "officer" && s->num_campaigns_participated == 0;
				}), soldiers.end());

			// הדפסת כל הרשימה לאחר מחיקת האיברים
			for (const auto& soldier : soldiers) {
				soldier->print();
			}

			break;
		}

		};
		cout << "enter 0-7\n";
		cin >> op;
	}
	return 0;
}


void add(list<Soldier*>& soldiers)
{
	cout << "enter 1 to add a private soldier" << endl;
	cout << "enter 2 to add a commander soldier" << endl;
	cout << "enter 3 to add a officer soldier" << endl;
	int choise;
	cin >> choise;
	switch (choise)
	{
	case 1: {
		auto p = new Private();
		p->add(*p);
		soldiers.push_back(p);
		break;
	}

	case 2: {
		auto c = new Commander();
		c->add(*c);
		soldiers.push_back(c);
		break;
	}
	case 3: {
		auto o = new Officer();
		o->add(*o);
		soldiers.push_back(o);
		break;
	}
	default:
		cout << "error!!!";
		break;
	}
}  
void medal(list<Soldier*>& soldiers)
{
	cout << "The soldiers entitled to the medal:" << endl;
	for (auto it = soldiers.begin(); it != soldiers.end(); it++)
		if ((*it)->medal())
			(*it)->print(); // קריאה לפונקציה print של כל חייל ברשימה

}
Soldier* mostSociometricScore(list<Soldier*>& soldiers) {
	Soldier* maxScore = nullptr;
	int max = 0;
	for (auto it = soldiers.begin(); it != soldiers.end(); ++it) {
		if ((*it)->soldierType() == "officer" && (*it)->getSociometricScore() > max) {
			max = (*it)->getSociometricScore();
			maxScore = *it;
		}
	}
	return maxScore;
}