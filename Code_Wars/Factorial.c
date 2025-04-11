unsigned __int128 factorial(unsigned n){
    __int128 fact, i;
         fact=1;
        for(i=1;i<=n;i++)
        {
           fact*=i;
        }
        return fact;
    }