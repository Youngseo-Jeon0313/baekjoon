#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int arr[100010];

void binarySearch(int ans) {
	int start = 0;
	int end = N - 1;
	int mid;
	while (end >= start) {
		mid = (start + end) / 2;
		if (arr[mid] == ans) {
			cout << 1 << '\n';
			return;
		}
		else if (arr[mid] > ans) {
			end = mid - 1;
		}
		else {
			start = mid + 1; 
		}
	}
	cout << 0 << '\n';
	return;
}

int main_() {
	ios_base::sync_with_stdio(false); cin.tie(0); //cin �ӵ� ������ �ذ�����
	//C++ ǥ�� ��Ʈ������ Cǥ�� ��Ʈ����� ������ ����� ���� �Ŀ� ����ȭ ���� ���� -> ����ȭ�� 0���� �ϸ� 'C�� �������ϱ�' �ӵ� ����
	cin >> N;
	int temp;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		arr[i] = temp;
	}
	sort(arr, arr + N);

	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> temp;
		binarySearch(temp);
	}
	return 0;
}