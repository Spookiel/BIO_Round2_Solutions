#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
typedef long long ll;

using namespace std;
int const MAXN =1e5;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define pb push_back


ll n,a,b;

vector<pi> adj8={{0,1}, {0,-1}, {1,0}, {1,-1}, {1,1},{-1,0},{-1,1},{-1,1}};
vector<pi> adj4 = {{0,1}, {0,-1}, {1,0}, {-1,0}};
vi rows;
vi cols;
vi grid[8];

int countVis(vi seq){
	int large=0;
	int vis = (int) seq.size();
	for(auto i: seq){
		if(large > i) vis--;
		else large=i;
		
		
	}
	return vis;
}

vi counter(vi seq){
	vi ans(9);
	
	for(auto i: seq){
		ans[i]++;
	}
	
	return ans;
	
	
}

int maxVis(vi seq){
	
	vi occs = counter(seq);
	vi left;
	for(int j=1; j <= (int) seq.size(); j++){
		if(occs[j]==0) left.pb(j);
		
		
	}
	
	
	int c=0;
	for(int i=0; i < (int) seq.size(); i++){
		if(seq[i]==0){
			seq[i] = left[c];
			c += 1;
			
		}
		
		
	}
	
	return (int) countVis(seq);
	
	
	
}

int minVis(vi seq){
	//cout << "-------------\n";
	vi occs = counter(seq);
	vi left;
	for(int j=(int) seq.size(); j >= 0; j--){
		if(occs[j]==0) left.pb(j);
		
		
	}
	
	
	int c=0;
	for(int i=0; i < (int) seq.size(); i++){
		
		if(seq[i]==0){
			seq[i] = left[c];
			c += 1;
			
		}
		//cout << seq[i] << " ";
		
		
	}
	//cout << "\n" << (int) countVis(seq) << "\n";
	//cout << "\n---------------\n";
	
	return (int) countVis(seq);
	
	
	
}


bool checkFinal(){
	
	int len = grid[0].size();
	vi col;
	for(int i=0; i < len; i++){
		if(countVis(grid[i]) != rows[i]) return false;
		col.clear();
		for(int j=0; j < len; j++){
			col.pb(grid[j][i]);
			
		}
		
		if(countVis(col)!=cols[i]) return false;
		
	}
	
	
	return true;
}



bool check(){
	
	int len = grid[0].size();
	vi col;
	//cout << len << " HERE\n";
	for(int i=0; i < len; i++){
		
		vi occs = counter(grid[i]);
		for(int j=1; j <= len; j++){
			if(occs[j] > 1) return false;
		}
		
		if(minVis(grid[i]) > rows[i] || maxVis(grid[i]) < rows[i]){
			
			//for(auto k: grid[i]) cout << k << " ";
			//cout << "\n";
			//cout << maxVis(grid[i]) << "\n";
			//cout << "RETURNED HERE\n";
			return false;
		}
		
		col.clear();
		
		for(int j=0; j < len; j++){
			col.pb(grid[j][i]);
			
			
			
		}
		occs = counter(col);
		
		for(int j=1; j <= len; j++){
			if(occs[j] > 1) return false;
			
		}
		
		if(minVis(col) > cols[i] || maxVis(col) < cols[i]) return false;
		
		
	}
	return true;
	
	
	
}

void solve(int x, int y){

		//	for(int i=0; i < (int) grid[0].size(); i++){
		//	for(auto j: grid[i]){
		//		cout << j << " ";
					
		//	}
		//	cout << "\n";
		//}
	//cout << "--------------------\n";
	
	
	if(y==n){
		if(checkFinal()){
			cout << "FOUND\n";
			for(int i=0; i < (int) grid[0].size(); i++){
				for(auto j: grid[i]){
					cout << j << " ";
					
				}
				cout << "\n";
			}
			//cout << "-------------";
			exit(0);
		}
		return;
		
		
		
	}
	
	if(grid[y][x]!=0){
		if(x==n-1){
			solve(0, y+1);
			
		}else{
			
			solve(x+1, y);
		}
		return;
		
		
	}else{
		
		for(int val=1; val <= n; val++){
			//cout << val << "\n";
			grid[y][x] = val;
			if(check()){
				//cout << "FOUND VALID VALUE " << val << " " << x << " " << y << "\n";
				if(x==n-1){
					solve(0, y+1);
				}else{
					solve(x+1, y);
				}
				
				
			}
			grid[y][x] = 0;
			
			
			
		}
		
		
		
	}
	
	
	
	
	
	
	
	
	
	
	
}

int main(void){
	
	vi tseq = {4,2,3,1};
	
	cout << minVis(tseq) << "\n";
	
	ifstream fin("future.in");
	ofstream fout("future.out");
	
	fin >> n;

	for(int i=0; i < n; i++){
		for(int j=0; j < n; j++){
			grid[i].pb(0);
			
		}
	}
	for(int i=0; i < n; i++){
		fin  >> a;
		rows.pb(a);
	}
	
	for(int i=0; i < n; i++){
		fin  >> a;
		cols.pb(a);
	}
	
	
	
	solve(0,0);
	
	
	return 0;
}
