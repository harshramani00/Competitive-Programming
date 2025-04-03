unsigned long long finance(unsigned long long n) {
    __int128 sum=0,i,j,temp;
    temp=n;
    for(i=0;i<=n;i++)
    {
    for(j=2*i;j<=temp;j++)
    {
    sum+=j;
    }
    temp++;
    }
    return sum;
}