char compare(int x, int y) {
	if (x > y) return '>';
	else if(x < y) return '<';
	else return '=';
}

int BinarySearch(int* a, const int x, const int left, const int right)
//���ĵ� �迭 [left], ~~, a[right] ���� x Ž��
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