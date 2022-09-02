#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include <tuple>
#include <string>
#include <queue>
#include <cmath>
#include <map>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; 
	cin >> N;

	for (int i = 0; i < N; i++) {
		map <string, int> m;
		int M;
		cin >> M;
		for (int j = 0; j < M; j++) {
			string key; string value;
			cin >> value >> key;
			if (m.find(key) == m.end()) {
				m.insert({ key,1 });
			}
			else m[key]++;
		};
		
		int ans = 1;
		map<string, int>::iterator iter;
		for (iter = m.begin(); iter != m.end(); iter++) {
			//cout << "¾Æ¾Æ" << iter->second;
			ans *= (iter->second+1);
		}
		cout  << ans-1 <<endl;
	}
}
