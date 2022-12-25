from collections import deque

M, N, K = list(map(int, input().split()))
spell = input().split()
spell = "".join(spell)

menus = input().split()
menus = "".join(menus)
# spell = list(map(int, input().split()))
# menus = list(map(int, input().split()))

try:
    a = menus.rindex(spell)
    print("secret")
except:
    print("normal")

# candidates = deque([])
# success = False
# for i in range(len(menus)):
#     menu = menus[i]
#     for _ in range(len(candidates)):
#         spell_idx = candidates.popleft()
#         if spell_idx == len(spell):
#             success = True
#             break
#         if spell[spell_idx] == menu:
#             candidates.append(spell_idx+1)
#     if success:
#         break
#     if menu == spell[0]:
#         candidates.append(1)

# if success:
#     print("secret")
# else:
#     print("normal")