def dogs_have_eatten(S, N, D, C, M):
    for i in range(N):
        if S[i]=="D":
            if D<=0 or C<0:
                return False
            D-=1
            C+=M
        else:
            C-=1
    return True

    