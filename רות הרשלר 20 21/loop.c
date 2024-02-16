#include <stdio.h>
int main(int argc, char* argv[])
{
if(argc==1)
	{printf("no parameters!!!\n");
	return 1;}
	
int n=atoi(argv[1]);
int sum=0;
for(int i=0;i<n;i++)
	{
	for(int j=0;j<n;j++)
		sum+=i*j;
	printf("i: %d sum:%d\n",i,sum);
	}
return 0;
}

