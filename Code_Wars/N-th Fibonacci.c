typedef unsigned long long ull;

ull nth_fib(int n) {

    if (n==1) return 0;
    if (n==2) return 1;
    __int128 i,fibo,f1=1,f2=0;
    for(i=3;i<=n;i++)
    {
    fibo=f1+f2;
    f2=f1;
    f1=fibo;
    }
    return fibo;
    

}