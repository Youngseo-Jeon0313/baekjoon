int Make_SegmentTree(int Node, int Start, int End)
{
    if (Start == End) return SegmentTree[Node] = Arr[Start];

    int Mid = (Start + End) / 2;
    int Left_Result = Make_SegmentTree(Node * 2, Start, Mid);
    int Right_Result = Make_SegmentTree(Node * 2 + 1, Mid + 1, End);
    SegmentTree[Node] = Left_Result + Right_Result;

    return SegmentTree[Node];
}

int main(void)
{
    int Tree_Height = (int)ceil(log2(N));
    int Tree_Size = (1 << (Tree_Height + 1));
    SegmentTree.resize(Tree_Size);
    Make_SegmentTree(1, 0, N - 1);
}

