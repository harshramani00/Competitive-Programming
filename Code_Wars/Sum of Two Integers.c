int add(int x, int y)
{
 if (y == 0)
        return x;
    else
        return add( x ^ y, (x & y) << 1);
}