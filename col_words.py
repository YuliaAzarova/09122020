s = input()
ans = 0
for smb in s:
    if smb in '0123456789':
        ans += 1
print(ans)