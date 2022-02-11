
#include <stdio.h>
int main()
{
    char alp;
    printf("Enter the alphabet you want to check.\n==>");
    scanf("%c",&alp);
    
    if( alp == 'a' || alp=='e' || alp == 'i' || alp == 'o' ||
         alp == 'u' || alp=='A' || alp == 'E' || alp == 'I'
          || alp == 'O' || alp == 'U')
    
       { printf("%c is vowel.\n",alp);}
    else
    {
         printf("%c is a consonant.\n",alp);
    }
    
       
}