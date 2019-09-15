#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
	if (argc != 2)
		return 0;
	char *str = strdup(argv[1]);
	for (int ii=0; str[ii] != '\0'; ++ii) {
		putchar(str[ii]-ii);
	}
	puts("");
}
