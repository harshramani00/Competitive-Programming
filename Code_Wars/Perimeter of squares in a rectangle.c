typedef unsigned long long ull;
ull perimeter(int n) {
    __int128 i,fibo,f1=1,f2=0,sum=1;
    if (n==1) sum=1;
    for(i=2,sum=1;i<=n+1;i++)
    {
    fibo=f1+f2;
    sum+=fibo;
    f2=f1;
    f1=fibo;
    }
    return 4*sum;
}