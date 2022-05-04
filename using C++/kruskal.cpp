#include <iostream>
#include <algorithm>
#include <vector>
#define n 7
using namespace std;

//부모노드 가져오기
int getParent(int set[], int x) {
	if (set[x] == x) return x;
	return set[x] = getParent(set, set[x]);
}

//부모 노드를 병합
void unionParent(int set[], int a, int b) {
	a = getParent(set, a);
	b = getParent(set, b);
	if (a < b) set[b] = a;
	else set[a] = b;
}

//같은 노드를 가지는지 확인
int find(int set[], int a, int b) {
	a = getParent(set, a);
	b = getParent(set, b);
	if (a == b) return 1;
	else return 0;
}

//간선 클래스 선언
class Edge {
public :
	int node[2];
	int distance;
	Edge(int a, int b, int distance) {
		this->node[0] = a;
		this->node[1] = b;
		this->distance = distance;
	}
 bool operator < (Edge& edge) {
	return this->distance < edge.distance;
}
};

int main(void) {

	int m = 11;
	int set[n];
	vector<Edge> v;
	v.push_back(Edge(1, 7, 12));
	v.push_back(Edge(1, 4, 28));
	v.push_back(Edge(1, 2, 67));
	v.push_back(Edge(1, 5, 17));
	v.push_back(Edge(2, 4, 24));
	v.push_back(Edge(3, 5, 20));
	v.push_back(Edge(3, 6, 37));
	v.push_back(Edge(4,7,13));
	v.push_back(Edge(5, 6, 45));
	v.push_back(Edge(5, 7, 73));


sort(v.begin(), v.end());


for (int i = 0; i < n; i++) {
	set[i] = i;
}

int sum = 0;
for (int i = 0; i < v.size(); i++) {
	if (!find(set, v[i].node[0] - 1, v[i].node[1] - 1)) {
		sum += v[i].distance;
		unionParent(set, v[i].node[0] - 1, v[i].node[1] - 1);
	}
}
printf("%d\n", sum);

}