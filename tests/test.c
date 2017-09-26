include <stdio.h>
//
int dummy_var;
#define dummy_define

#ifdef dummy_define
    printf ("Dummy define defined");
#else
    printf ("Dummy define is not defined");
#endif

// This is single line comment

/* This is 
multiline
comment
Block
*/

int t6,t5,t3;

union
{
    unsigned int All;
    struct
    {
        unsigned char Byte1;
        unsigned char Byte2;
        unsigned char Byte3;
        unsigned char Byte4;
    } structsample;
} ui32= {0,0,0,0};

int main()
{
    int i, space, rows, k=0, count = 0, count1 = 0;

    printf("Enter number of rows: ");
    scanf("%d",&rows);

    for(i=1; i<=rows; ++i)
    {
        for(space=1; space <= rows-i; ++space)
        {
            printf("  ");
            ++count;
        }

        while(k != 2*i-1)
        {
            if (count <= rows-1)
            {
                printf("%d ", i+k);
                ++count;
            }
            else
            {
                ++count1;
                printf("%d ", (i+k-2*count1));
            }
            ++k;
        }
        count1 = count = k = 0;

        printf("\n");
    }
    return 0;
}

void main2()
{
    int i, space, rows, k=0, count = 0, count1 = 0;

    printf("Enter number of rows: ");
    scanf("%d",&rows);

    for(i=1; i<=rows; ++i)
    {
        for(space=1; space <= rows-i; ++space)
        {
            printf("  ");
            ++count;
        }

        while(k != 2*i-1)
        {
            if (count <= rows-1)
            {
                printf("%d ", i+k);
                ++count;
            }
            else
            {
                ++count1;
                printf("%d ", (i+k-2*count1));
            }
            ++k;
        }
        count1 = count = k = 0;

        printf("\n");
    }
}

//Dummy Block
{
;
}

