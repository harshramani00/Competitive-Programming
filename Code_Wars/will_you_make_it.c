#include <stdbool.h>

bool zero_fuel(double distance_to_pump, double mpg, double fuel_left)
{
    if(mpg*fuel_left>=distance_to_pump)
    {  return 1; }
    else
    {  return 0;  }
}