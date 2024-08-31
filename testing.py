# def horse_step(self, x, y ):
#         is_passed = []
#         tryed = []
#         is_passed.append((x,y))
#         while self.length != len(is_passed):
#             move_found = False
        
#             for dot in self.chessboard[(x, y)]:
#                 if dot not in is_passed:
#                     is_passed.append((dot[0],dot[1]))
#                     tryed.append(((dot[0],dot[1])))
#                     current = (x,y)
#                     x = dot[0]
#                     y = dot[1]
#                     tryed_current = (x,y)
#                     move_found = True
#                     break
#             print(x,y)
            
#             if not move_found:
#                 is_passed.remove(tryed_current)
#                 for new_dot in self.chessboard[(current)]:
#                     if new_dot not in tryed:
#                         is_passed.append((new_dot[0],new_dot[1]))
#                         tryed.append((new_dot[0],new_dot[1]))
#                         current = ...
#                         x = new_dot[0]
#                         y = new_dot[1]



# x = 1
# y = 2
# z = (x,y)

# print(z)

# x = 5
# y = 6
# z = (x,y)

# print(z)


a = [(1, 1), (3, 2), (2, 4), (1, 2), (3, 3), (2, 5), (1, 3), (2, 1), (4, 2), (3, 4), (1, 5), (2, 3), (3, 1), (5, 2), (4, 4)]
b= a.index((1,1))
# print(b)
for i in range(0,4):
    print(i)