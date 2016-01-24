#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <locale>
using namespace std;
int main(int argc, char* argv[])
{
	string textFileName;
	vector<string> line;

	cin >> textFileName;
	ifstream text(textFileName.c_str());
	if(text.fail())
	{
		cerr << "Error, can't open specified text!" << endl;
		return 0;
	}	

	string token;
	int i = 0;
	while(getline(text, token, ','))
	{
		line.push_back(token);
		if(i == 0)
		{
			line[i].erase(0, 1);
		}
		else
		{
			line[i].erase(0, 2);
		}
		line[i].erase(line[i].length()-1, string::npos);
		i++;
	}

	cin >> textFileName;
	vector<string> dataV;
	ifstream data(textFileName.c_str());
	locale loc;
	while(getline(data, token))
	{
		dataV.push_back(token);
	}
	for(int i = 0; i<dataV.size(); i++)
	{
		dataV[i] = dataV[i] + "\n";
		token = "";
		for(int j = 0; j<dataV[i].length(); j++)
		{
			token = token + tolower(dataV[i][j], loc);
		}
		dataV[i] = token;
	}

	int count = 0;
	for(int i = 0; i<line.size(); i++)
	{
		for(int j = 0; j<dataV.size(); j++)
		{
			if(dataV[j].find(line[i]) != string::npos)
			{
				count++;
			}
		}

		cout << line[i] << ": " << count << endl;
		count = 0;
	}
	return 0;
}
