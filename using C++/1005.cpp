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


int main_(void) {

	int T;
	cin >> T;
	while (T--) {
		int answer = 0;
		int N, K, node_cost, x, y, W;
		cin >> N >> K;
		vector<vector<int>> v(N + 1);
		queue<int> q;

		
		for (int k = 1; k <=N; k++) {
			//D���ٰ� �ֱ�
			cin >> node_cost; //�츮�� �� �� �޴� ���� �˱� ������ �̷��� �����ؼ� �޴´�.
			cost[k] = node_cost; 
			resultCost[k] = node_cost;
		}
		for (int j = 0; j < K; j++) {
			cin >> x >> y;
			v[x].push_back(y);//v��� �迭���� �ش� index �ȿ� �� ������ �������� ���� ���� ����
			indegree[y]++;//�������� �ϳ��� �÷��ֱ�
		}

		cin >> W;

		for (int i = 1; i <= N; i++) {
			if (i == W) continue;
			else if (indegree[i] == 0) { q.push(i); } //������ 0�� �� �ϴ� �ֱ�
		}
		while (!q.empty()) {
			int idx = q.front(); //popleft
			q.pop();
			int Size = v[idx].size();
			for (int j = 0; j < Size; j++) {
				int n = v[idx][j]; //�ش� index v[index] �� ���Ҹ� �ϳ��� ������.
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