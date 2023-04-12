def fun(A,B):
  if (B == 0)
    return A
  else:
    return fun(B, A % B)

ans = fun (100, 2000)
print(ans)

