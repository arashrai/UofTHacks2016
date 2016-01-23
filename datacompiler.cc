#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
int main(int argc, char* argv[])
{
	string textFileName;
	vector<string> line;
	while(cin >> textFileName)
	{
		ifstream text(textFileName.c_str());
		if(text.fail())
		{
			cerr << "Error, can't open specified text!" << endl;
			return 0;
		}	
		string token;
		while(getline(text, token))
		{
			line.push_back(token);
		}
	}
	for(int i = 0; i<line.size(); i++)
	{
		for(int j = i+1; j<line.size(); j++)
		{
			if(line[i]=="")
			{
				break;
			}
			if(line[i]==line[j])
			{
				line[j] = "";
			}
		}
		line[i] = line[i] + "\n";
		cout << line[i];
	}
	return 0;
}
