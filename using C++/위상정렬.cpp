#include <iostream>
#include <vector>
#include <queue>
#define MAX 10

using namespace std;

int n, inDegree[MAX];
vector<int> a[MAX];

void topologySort() {
	int result[MAX];
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		if (inDegree[i] == 0) q.push(i);
	}
	for (int i = 1; i <= n; i++) {
		//n개를 방문하기 전에 큐가 비어버렸다면 사이클이 발생한 것이다.
		if (q.empty()) {
			printf("사이클이 발생했습니다.");
			return;
		}
		int x = q.front(); //q 맨 앞에 꺼 가져옴
		q.pop(); //front 데이터 없앰
		result[i] = x;
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			//만약 진입차수가 0인 게 있다면 큐에 삽입한다.
			if (--inDegree[y] == 0)
				q.push(y);
		}
	}
		for (int i = 1; i <= n; i++) {
			printf("%d ", result[i]);
	}

}

int phase_Alignment_main(void) {
	n = 7;
	a[1].push_back(2);
	inDegree[2]++;
	a[1].push_back(5);
	inDegree[5]++;
	a[2].push_back(3);
	inDegree[3]++;
	a[3].push_back(4);
	inDegree[4]++;
	a[4].push_back(6);
	inDegree[6]++;
	a[5].push_back(6);
	inDegree[6]++;
	a[6].push_back(7);
	inDegree[7]++;
	topologySort();

	//a라는 배열에는 해당 index 안에 그 정점을 진입으로 갖는 정점 대입
	//inDegree는 진입차수가 각각 쓰여있음
}