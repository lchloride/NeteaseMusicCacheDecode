#include <stdio.h>
#define OPERATOR 0xA3

int main(int argc, char const *argv[])
{
	FILE *fin, *fout;
	char ch;

	if ((fin = fopen(argv[1], "rb")) == NULL) {
		printf("Cannot open input file.\n");
		return 1;
	}

	if ((fout = fopen(argv[2], "wb")) == NULL) {
		printf("Cannot open output file.\n");
		return 1;
	}

	while (!feof(fin)) 
	{
		ch = fgetc(fin);
		ch = ch ^ OPERATOR;
		fputc(ch, fout);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}