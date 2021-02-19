#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
typedef long long ll;

using namespace std;
int const MAXN =1e5;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define pb push_back


ll n,a,b,c;

vector<pi> adj8={{0,1}, {0,-1}, {1,0}, {1,-1}, {1,1},{-1,0},{-1,1},{-1,1}};
vector<pi> adj4 = {{0,1}, {0,-1}, {1,0}, {-1,0}};

int main(void){
	
	ifstream fin("pin.in");
	ofstream fout("pin.out");
	
	fin >> n;
	set<int> ans;
	vi last;
	for(int j=0; j < n; j++){
		fin >> a;
		last.pb(a);
		
	}
	set<int> curSet;
	
	cout << last.size() << "\n";
	vi cur;
	for(int k=0; k < n; k++){
		fin >> a;
		cur.pb(a);
			
	}
	
	for(auto la: cur){
			for(auto ta: last){
				cout << la << " " << ta << " " << la-ta << "\n";
				ans.insert(la-ta);
		}
	}
	last = cur;
	cout << "---------\n";
	for(int i=0; i < n-1; i++){
		cur.clear();
		curSet.clear();
		for(int k=0; k < n; k++){
			fin >> a;
			cur.pb(a);
				
		}
		
		for(auto la: cur){
			for(auto ta: last){
				cout << la << " " << ta << " " << la-ta << "\n";
				curSet.insert(la-ta);
			}
		}
	cout << "---------\n";
	set<int> newans;
	for(auto i: ans){
		
		if(curSet.count(i) > 0) newans.insert(i);
	}
	ans = newans;
	last = cur;
	}
	
	
	for(auto ab: ans){
		cout << ab << "\n";
	}
	
	return 0;
}
