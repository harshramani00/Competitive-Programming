int seats_in_theater(int n_cols, int n_rows, int col, int row)
{
    int xrows,xcols,dis;
    xrows=n_rows-(row);
    xcols=n_cols-(col-1);
    dis=(xrows*xcols);
    return dis;
}