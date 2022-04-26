#include <iostream>
#include <vector>
#include <queue>
#define MAX 32001

using namespace std;

int n, inDegree[MAX];
vector<int> a[MAX];
int result[MAX];
queue<int> q;
void topologySort() {
	
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
		for (int j = 0; j < a[x].size(); j++) {
			int y = a[x][j];
			//만약 진입차수가 0인 게 있다면 큐에 삽입한다.
			if (--inDegree[y] == 0)
				q.push(y);
		}
	}
	for (int i = 1; i <= n; i++) {
		printf("%d ", result[i]);
	}

}

int main(void) {
	int m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int front, back;
		cin >> front >> back;
		a[front].push_back(back);
		inDegree[back]++;
	}
	
	topologySort();

	//a라는 배열에는 해당 index 안에 그 정점을 진입으로 갖는 정점 대입
	//inDegree는 진입차수가 각각 쓰여있음
}