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

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); //cin 속도 문제를 해결해줌
	//C++ 표준 스트림들이 C표준 스트림들과 각각의 입출력 연산 후에 동기화 여부 설정 -> 동기화를 0으로 하면 'C와 끊어지니까' 속도 향상됨
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