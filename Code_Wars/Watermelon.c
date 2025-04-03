#include <stdbool.h>

bool divide(unsigned weight)
{   if(weight==2)
    {return false;}
    else if(weight%2==0)
    {return true;}
    else
    {return false;}
}