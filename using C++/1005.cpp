#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <random>

using namespace std;

int indegree[1005];
map<int, int> resultCost;
map<int, int> cost;


int main(void) {

	int T;
	cin >> T;
	while (T--) {
		int answer = 0;
		int N, K, node_cost, x, y, W;
		cin >> N >> K;
		vector<vector<int>> v(N + 1);
		queue<int> q;

		
		for (int k = 1; k <=N; k++) {
			//D에다가 넣기
			cin >> node_cost; //우리는 몇 번 받는 건지 알기 때문에 이렇게 개행해서 받는다.
			cost[k] = node_cost; 
			resultCost[k] = node_cost;
		}
		for (int j = 0; j < K; j++) {
			cin >> x >> y;
			v[x].push_back(y);//v라는 배열에는 해당 index 안에 그 정점을 진입으로 갖는 정점 대입
			indegree[y]++;//진입차수 하나씩 늘려주기
		}

		cin >> W;

		for (int i = 1; i <= N; i++) {
			if (i == W) continue;
			else if (indegree[i] == 0) { q.push(i); } //진입이 0인 거 일단 넣기
		}
		while (!q.empty()) {
			int idx = q.front(); //popleft
			q.pop();
			int Size = v[idx].size();
			for (int j = 0; j < Size; j++) {
				int n = v[idx][j]; //해당 index v[index] 속 원소를 하나씩 꺼낸다.
				resultCost[n] = max(resultCost[n], resultCost[idx] + cost[n]);
				if (--indegree[n] == 0) q.push(n);
			}
		}
		cout << resultCost[W] << endl;

		for (int j = 1; j <= N; j++) {
			indegree[j] = 0;
			resultCost[j] = 0;
			cost[j] = 0;
		}
	}
	return 0;
}