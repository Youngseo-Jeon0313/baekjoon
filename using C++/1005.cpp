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
		//n���� �湮�ϱ� ���� ť�� �����ȴٸ� ����Ŭ�� �߻��� ���̴�.
		if (q.empty()) {
			printf("����Ŭ�� �߻��߽��ϴ�.");
			return;
		}
		int x = q.front(); //q �� �տ� �� ������
		q.pop(); //front ������ ����
		result[i] = x;
		for (int j = 0; j < a[x].size(); j++) {
			int y = a[x][j];
			//���� ���������� 0�� �� �ִٸ� ť�� �����Ѵ�.
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

	//a��� �迭���� �ش� index �ȿ� �� ������ �������� ���� ���� ����
	//inDegree�� ���������� ���� ��������
}