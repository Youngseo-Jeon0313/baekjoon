class String {
public:
	String(char* init, int m); //*this�� ���� m�� ���ڿ� init���� �ʱ�ȭ�ϴ� ������

	int operator==(String t) {
		if (*this == t) return 1;
		else return 0;
	};
	int operator!() {
		if (*this.empty()) return 1;
		else return 0;
	};
	int Length();
	String Concat(String t);
	String Substr(int i, int j);
	int Find(String pat);
};

int String::Find(String pat)
{
	char* p = pat.str, * s = str;
	int i = 0;
	if (*p && *s)
		while (i<=Length() - pat.Length())
			if (*p++ == *s++) {
				if (!*p) return i;
			}
			else {
				i++; s = str + i; p = pat.Substr;
			}

}