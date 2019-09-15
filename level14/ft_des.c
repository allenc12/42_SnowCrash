#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char*
ft_des(const char *param_1)
{
	char cVar1;
	char *pcVar2;
	unsigned int uVar3;
	char *pcVar4;
	unsigned char bVar5;
	unsigned int local_20;
	int local_1c;
	int local_18;
	int local_14;

	bVar5 = 0;
	pcVar2 = strdup(param_1);
	local_1c = 0;
	local_20 = 0;
	do {
		uVar3 = 0xffffffff;
		pcVar4 = pcVar2;
		do {
			if (uVar3 == 0)
				break;
			uVar3 = uVar3 - 1;
			cVar1 = *pcVar4;
			pcVar4 = pcVar4 + (unsigned int)bVar5 * -2 + 1;
		} while (cVar1 != '\0');
		if (~uVar3 - 1 <= local_20) {
			return pcVar2;
		}
		if (local_1c == 6) {
			local_1c = 0;
		}
		if ((local_20 & 1) == 0) {
			if ((local_20 & 1) == 0) {
				local_14 = 0;
				while (local_14 < (int)"0123456"[local_1c]) {
					pcVar2[local_20] = pcVar2[local_20] + -1;
					if (pcVar2[local_20] == '\x1f') {
						pcVar2[local_20] = '~';
					}
					local_14 = local_14 + 1;
				}
			}
		} else {
			local_18 = 0;
			while (local_18 < (int)"0123456"[local_1c]) {
				pcVar2[local_20] = pcVar2[local_20] + '\x01';
				if (pcVar2[local_20] == '\x7f') {
					pcVar2[local_20] = ' ';
				}
				local_18 = local_18 + 1;
			}
		}
		local_20 = local_20 + 1;
		local_1c = local_1c + 1;
	} while( true );
}

const char *const tok_3000 = "I`fA>_88eEd:=`85h0D8HE>,D";
const char *const tok_3001 = "7`4Ci4=^d=J,?>i;6,7d416,7";
const char *const tok_3002 = "<>B16\\AD<C6,G_<1>^7ci>l4B";
const char *const tok_3003 = "B8b:6,3fj7:,;bh>D@>8i:6@D";
const char *const tok_3004 = "?4d@:,C>8C60G>8:h:Gb4?l,A";
const char *const tok_3005 = "G8H.6,=4k5J0<cd/D@>>B:>:4";
const char *const tok_3006 = "H8B8h_20B4J43><8>\\ED<;j@3";
const char *const tok_3007 = "78H:J4<4<9i_I4k0J^5>B1j`9";
const char *const tok_3008 = "bci`mC{)jxkn<\"uD~6%g7FK`7";
const char *const tok_3009 = "Dc6m~;}f8Cj#xFkel;#&ycfbK";
const char *const tok_3010 = "74H9D^3ed7k05445J0E4e;Da4";
const char *const tok_3011 = "70hCi,E44Df[A4B/J@3f<=:`D";
const char *const tok_3012 = "8_Dw\"4#?+3i]q&;p6 gtw88EC";
const char *const tok_3013 = "boe]!ai0FB@.:|L6l@A?>qJ}I";
const char *const tok_3014 = "g <t61:|4_|!@IF.-62FH&G~DCK/Ekrvvdwz?v|";

const char *const toks[] = {
	tok_3000,
	tok_3001,
	tok_3002,
	tok_3003,
	tok_3004,
	tok_3005,
	tok_3006,
	tok_3007,
	tok_3008,
	tok_3009,
	tok_3010,
	tok_3011,
	tok_3012,
	tok_3013,
	tok_3014,
};

int
main(int argc, const char *argv[])
{
	char *ret;
	int ii;

	if (argc >= 2) {
		ii = atoi(argv[1]);
		if (ii < 0 || ii > 15) {
			fputs("Error: must specify a number from 0 to 14 inclusive.", stderr);
			return 1;
		}
		ret = ft_des(toks[ii]);
		puts(ret);
		free(ret);
	} else {
		for (ii = 0; ii < 15; ++ii) {
			ret = ft_des(toks[ii]);
			printf("tok_3%03d = %s\n", ii, ret);
			free(ret);
		}
	}
}
