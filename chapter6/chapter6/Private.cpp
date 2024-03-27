#include "Private.h"
#include <algorithm>
bool Private::medal() {
	int sum = 0;
	for (int i = 0; i < campaign_ratings.size(); i++)
	{
		sum += campaign_ratings[i];
	}
	return num_campaigns_participated>=10 && sum / campaign_ratings.size() > 95;
}
void Private::print(){
	Soldier::print();
	cout << "campaign_ratings: ";
	for (int i = 0; i < campaign_ratings.size(); i++)
	{
		cout << campaign_ratings[i] << " ";
	}
	cout << endl;
}
string Private::soldierType() {
	return "private";
}
void Private::add(Soldier& s)
{
	Soldier::add(s);
	if (num_campaigns_participated == 0)
		return;
	cout << "enter " << num_campaigns_participated << " grades" << endl;
	int grade;
	for (int i = 0; i < num_campaigns_participated; i++)
	{
		cin >> grade;
		campaign_ratings.push_back(grade);
	}
}