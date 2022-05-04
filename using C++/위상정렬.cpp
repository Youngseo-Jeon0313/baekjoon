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
		//n���� �湮�ϱ� ���� ť�� �����ȴٸ� ����Ŭ�� �߻��� ���̴�.
		if (q.empty()) {
			printf("����Ŭ�� �߻��߽��ϴ�.");
			return;
		}
		int x = q.front(); //q �� �տ� �� ������
		q.pop(); //front ������ ����
		result[i] = x;
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			//���� ���������� 0�� �� �ִٸ� ť�� �����Ѵ�.
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

	//a��� �迭���� �ش� index �ȿ� �� ������ �������� ���� ���� ����
	//inDegree�� ���������� ���� ��������
}