char compare(int x, int y) {
	if (x > y) return '>';
	else if(x < y) return '<';
	else return '=';
}

int BinarySearch(int* a, const int x, const int left, const int right)
//정렬된 배열 [left], ~~, a[right] 에서 x 탐색
{
	if (left <= right) {
		int middle = (left + right) / 2;
		switch (compare(x, a[middle])) {
		case '>': return BinarySearch(a, x, middle + 1, right); //x>a[middle]
		case '<': return BinarySearch(a, x, left, middle-1); //x<a[middle]
		case '=': return middle; //x=a[middle]
		}
	}
	return -1;
}