unsigned sequence_sum(unsigned start, unsigned end, unsigned step)
{
    if(start>end)  return 0;
    return start+sequence_sum(start+step,end,step);
}