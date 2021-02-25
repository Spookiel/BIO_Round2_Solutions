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



int siz[200001];
vi graph[200001];

int dfs(int u, int f){
	
	if(graph[u].size()==1 && graph[u][0]==f){
		
		siz[u] = 1;
		return 1;
	}
	
	int tot=1;
	for(auto adj: graph[u]){
		if(adj==f) continue;
		
		tot += dfs(adj, u);
		
		
	}
	siz[u] = tot;
	return siz[u];
	
	
	
}




int main(void){
	
	ifstream fin("scoop.in");
	ofstream fout("scoop.out");
	
	int start;
	
	//Use a DFS to calculate the size of all subtrees from the start location
	// Then answer is (a*3*2 for all a where a is the size of subtree)-(max(subtrees)*3)
	fin >> n >> start;
	
	for(int i=0; i < n; i++){
		fin >> a >> b;
		graph[a].pb(b);
		graph[b].pb(a);
		
	}
	
	dfs(start, 0);
	ll tot=0;
	
	ll large=-1;
	for(auto adj: graph[start]){
		tot += siz[adj]*6;
		//cout << adj << " " << siz[adj] << "\n";
		large = max((ll) siz[adj]*3, large);
		
		
		
	}
	tot -= large;
	cout << "ANSWER: " << tot << "\n";
	fout << tot << "\n";
	
	

	
	
	
	
	
	
	
	
	
	
	return 0;
}
