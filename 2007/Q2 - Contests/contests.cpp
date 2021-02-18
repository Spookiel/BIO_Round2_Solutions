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

vi graph[5001];
int parents[5001];
int best[5001];
int degs[5001];
int done[5001];
int exists[5001][5001];

void bfs(int u, int v){
	
	queue<pi> doing;
	fill(best, best+5001, 999999);
	fill(parents, parents+5001, 0);
	pi start = make_pair(u, 0);
	doing.emplace(start);
	best[u] = 0;
	while(doing.size() > 0){
		pi ne = doing.front();
		doing.pop();
		int node, distance;
		node = ne.first;
		distance = ne.second;
		if(node==v) break;
		for(auto adj: graph[node]){
			
			if(distance+1 < best[adj]){
				best[adj] = distance+1;
				parents[adj] = node;
				doing.emplace(make_pair(adj, distance+1));
				
				
			}
			
			
		}
		
		
		
	}
	
	vi path;
	path.pb(v);
	while(1){
		
		int last = path.back();
		int par = parents[last];
		if(par==0) break;
		
		path.pb(par);
		
		
		
	}
	//cout << "-----------------\n";
	reverse(path.begin(), path.end());
		
	for(int k=1; k < (int) path.size(); k++){
		//cout << "REMOVING " << path[k] << " " << path[k-1] << "\n";
		exists[path[k]][path[k-1]] = 1-exists[path[k]][path[k-1]];
		exists[path[k-1]][path[k]] = 1-exists[path[k-1]][path[k]];
	}
	//cout << "-----------------\n";

	
	
	
	
	
}





int main(void){
	
	ifstream fin("contests.in");
	ofstream fout("contests.out");
	vi evens;
	int s, e;
	fin >> n;
	do{
		fin >> s >> e;
		
		if(s==-1) break;
		graph[s].pb(e);
		graph[e].pb(s);
		exists[s][e] = 1;
		exists[e][s] = 1;
		
	}while(1);
	
	for(int i=1; i <= n; i++){
		
		if(graph[i].size()%2==0) evens.pb(i);
	}
	//cout << evens.size() << "\n";
	for(int j=0; j+1 < (int) evens.size(); j+= 2){
		//cout << evens[j] << " " << evens[j+1] << "\n";
		bfs(evens[j], evens[j+1]);
		//cout << j << "\n";
		
	}
	
	

	set<pi> edgeLast;
	for(int i=1; i <= n; i++){
		for(auto k: graph[i]){
			if(k < i && exists[i][k]) edgeLast.insert(make_pair(k, i));
			else if(exists[i][k]) edgeLast.insert(make_pair(i, k));
		}
	}
	fout << edgeLast.size() << "\n";
	for(auto at: edgeLast){
		fout << at.first << " " << at.second << "\n";
		degs[at.first]++;
		degs[at.second]++;
		
	}
	
	bool isCorrect = true;
	for(int i=1; i <= n; i++){
		if(degs[i]%2==0){
			isCorrect = false;
			break;
		}
		
		
		
	}
	//cout << isCorrect << "\n";

	return 1-isCorrect;
}
