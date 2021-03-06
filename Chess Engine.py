#BY KISOTHAN SUTHAARAN
#CHESS ENGINE

#DEFINE THE POSSIBLE MOVES FOR EACH PIECE

board=[['uA0l','uB0l','uC0l','uD0','uE0','uC0r','uB0r','uA0r'],['uP1','uP2','uP3','uP4','uP5','uP6','uP7','uP8'],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],['dP9','dP10','dP11','dP12','dP13','dP14','dP15','dP16'],['dA1l','dB1l','dC1l','dD1','dE1','dC1r','dB1r','dA1r']]

#A=ROOK
def rook_slots(piece,board):
   """-"""
   slot=[]
   list_of_slots=[]   
   i=0
   for row in board:
      row_position=i
      i+=1
      k=0
      for column in row:
         column_position=k
         k+=1
         if column==piece:
            for y in range(0,8):
               slot=[row_positon, y]
               list_of_slots.append(slot)
               slot=[]
            for random in range(0,8):
               slot=[random,column_position]
               list_of_slots.append(slot)
               slot=[]
   for slot in list_of_slots:
         for row_position1 in slot:
            if row_position1 <0 or row_position1>7 or slot==piece:
               list_of_slots.remove(slot)
   return(list_of_slots)
   

#B=knight  
def knight_slots(piece,board):
      """-"""
      slot=[]
      list_of_slots=[]   
      i=0      
      for row in board:
         row_position=i
         i+=1
         k=0
         for column in row:
            column_position=k
            k+=1      
            if column==piece:
               for y in range(0,8):
                  slot=[row_positon+2, y-1]
                  list_of_slots.append(slot)
                  slot=[]    
                  slot=[row_positon+2, y+1]
                  list_of_slots.append(slot)
                  slot=[]      
                  slot=[row_positon+1, y+2]
                  list_of_slots.append(slot) 
                  slot=[]      
                  slot=[row_positon+1, y-2]
                  list_of_slots.append(slot)
                  slot=[]      
                  slot=[row_positon-2, y-1]
                  list_of_slots.append(slot) 
                  slot=[]
                  slot=[row_positon+2, y-1]
                  list_of_slots.append(slot) 
                  slot=[]
                  slot=[row_positon+1, y-2]
                  list_of_slots.append(slot)     
                  slot=[]
                  slot=[row_positon-1, y-2]
                  list_of_slots.append(slot)     
      for slot in list_of_slots:
         for row_position1 in slot:
            if row_position1 <0 or row_position1>7:
               list_of_slots.remove(slot)
      return(list_of_slots)
   
#C=BISHOP
def bishop_slots(piece,board):
      """-"""
      slot=[]
      list_of_slots=[]   
      i=0      
      for row in board:
         row_position=i
         i+=1
         k=0
         for column in row:
            column_position=k
            k+=1      
            if column==piece:
                  for random in range(0,7):
                     row_position+=1
                     column_position+=1
                     slot=[row_position,column_position]
                     list_of_slots.append(slot)
                     slot=[]
                  for row in board:
                        if piece in row:
                           row_position=board.index(row)
                           column_position=row.index(piece)
                  for random in range(0,7):
                     row_position=row_position-1
                     column_position=column_position-1
                     slot=[row_position,column_position]
                     list_of_slots.append(slot)
                     slot=[]
                  for row in board:
                        if piece in row:
                           row_position=board.index(row)
                           column_position=row.index(piece)
                  for random in range(0,7):
                     row_position=row_position+1
                     column_position=column_position-1
                     slot=[row_position,column_position]
                     list_of_slots.append(slot)
                     slot=[]
                  for row in board:
                        if piece in row:
                           row_position=board.index(row)
                           column_position=row.index(piece)
                  for random in range(0,7):
                     row_position=row_position-1
                     column_position=column_position+1
                     slot=[row_position,column_position]
                     list_of_slots.append(slot)
                     slot=[]
            for slot in list_of_slots:
               for row_position1 in slot:
                  if row_position1 <0 or row_position1>7:
                     list_of_slots.remove(slot)
      return(list_of_slots)
   
#d=queen   
def queen_slots(piece,board):
      """-"""
      i=0      
      for row in board:
         row_position=i
         i+=1
         k=0
         for column in row:
            column_position=k
            k+=1      
            if column==piece:
               for slot in bishop_slots(piece):
                  rook_slots(piece).append(slot)
      return(rook_slots)
   
def king_slots(piece,board):
      """-"""
      slot=[]
      list_of_slots=[]   
      i=0
      for row in board:
         row_position=i
         i+=1
         k=0
         for column in row:
            column_position=k
            k+=1
            if column==piece:
               slot=[row_position+1,column_position]
               list_of_slots.append(slot)
               slot=[]
               slot=[row_position-1,column_position]
               list_of_slots.append(slot)
               slot=[]
               slot=[row_position,column_position+1]
               list_of_slots.append(slot)
               slot=[]
               slot=[row_position,column_position-1]
               list_of_slots.append(slot)    
               for random in range(1):
                  row_position+=1
                  column_position+=1
                  slot=[row_position,column_position]
                  list_of_slots.append(slot)
                  slot=[]
               for row in board:
                  if piece in row:
                     row_position=board.index(row)
                     column_position=row.index(piece)
               for random in range(1):
                  row_position=row_position-1
                  column_position=column_position-1
                  slot=[row_position,column_position]
                  list_of_slots.append(slot)
                  slot=[]
               for row in board:
                  if piece in row:
                     row_position=board.index(row)
                     column_position=row.index(piece)
               for random in range(1):
                  row_position=row_position+1
                  column_position=column_position-1
                  slot=[row_position,column_position]
                  list_of_slots.append(slot)
                  slot=[]
               for row in board:
                  if piece in row:
                     row_position=board.index(row)
                     column_position=row.index(piece)
               for random in range(1):
                  row_position=row_position-1
                  column_position=column_position+1
                  slot=[row_position,column_position]
                  list_of_slots.append(slot)
                  slot=[]  
      for slot in list_of_slots:
               for row_position1 in slot:
                  if row_position1 <0 or row_position1>7:
                     list_of_slots.remove(slot)
      return(list_of_slots)
   
def up_pawn_slots(piece,board):
   """-"""
   slot=[]
   list_of_slots=[]   
   i=0      
   for row in board:
      row_position=i
      i+=1
      k=0
      for column in row:
         column_position=k
         k+=1      
         if column==piece:
            if board[row_position+1][column_position]==0 and row_position+1>0 and row_position+1<8:
               slot=[row_position+1,column_position]
               list_of_slots.append(slot)
               slot=[]
            if row_position==1 and board[row_position+1][column_position]==0 and board[row_position+2][column_position]==0 and row_position+2>0 and row_position+2<8 :
               slot=[row_position+2,column_position]
               list_of_slots.append(slot)
               slot=[]
            if board[row_position+1][column_position+1]!=0 and row_position!=1 and row_position+1>0 and row_position+1<7 and column_position+1>0 and column_position+1<8:
               if board[row_position+1][column_position+1][0]=='d':
                  slot=[row_position+1,column_position+1]
                  list_of_slots.append(slot)
                  slot=[]
            if board[row_position+1][column_position-1]!=0 and row_position!=1 and row_position+1>0 and row_position+1<8 and column_position+1>0 and column_position+1<8:
               if board[row_position+1][column_position+1][0]=='d':
                  slot=[row_position+1,column_position-1]
                  list_of_slots.append(slot)
                  slot=[]
   for slot in list_of_slots:
      for row_position1 in slot:
            if row_position1 <0 or row_position1>7:
               list_of_slots.remove(slot)
   return(list_of_slots)

def down_pawn_slots(piece,board):
   """-"""if square[1]=='A':
               for slot in rook_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
   slot=[]
   list_of_slots=[]   
   i=0      
   for row in board:
      row_position=i
      i+=1
      k=0
      for column in row:
         column_position=k
         k+=1      
         if column==piece:
            if board[row_position-1][column_position]==0 and row_position-1>0 and row_position-1<7:
               slot=[row_position-1,column_position]
               list_of_slots.append(slot)
               slot=[]
            if row_position==6 and board[row_position-1][column_position]==0 and board[row_position-2][column_position]==0 and row_position-2>0 and row_position-2<8 :
               slot=[row_position-2,column_position]
               list_of_slots.append(slot)
               slot=[]
               slot=[row_poisition-2,column_position]
               list_of_slots.append(slot)
            if board[row_position-1][column_position-1]!=0 and row_position!=6 and row_position-1>0 and row_position-1<8 and column_position-1>0 and column_position-1<8:
               if board[row_position-1][column_position-1][0]=='u':
                  slot=[row_position-1,column_position-1]
                  list_of_slots.append(slot)
                  slot=[]
            if board[row_position-1][column_position+1]!=0 and row_position!=1 and row_position-1>0 and row_position-1<7 and column_position+1>0 and column_position+1<7:
               if board[row_position-1][column_position+1][0]=='u':
                  slot=[row_position-1,column_position+1]
                  list_of_slots.append(slot)
                  slot=[]
   for slot in list_of_slots:
      for row_position1 in slot:
            if row_position1 <0 or row_position1>7:
               list_of_slots.remove(slot)
   return(list_of_slots)
         
#PROGRAM KOSAKSI TO MAKE THE BEST MOVE AMONG ALL THE POSSIBILITES


def get_danger_squares(board):
   """-"""
   danger_squares=[]
   for line in board:
      for square in line:
         if square[0]=='d':
            if square[1]=='A':
               for slot in rook_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
            if square[1]=='B':
               for slot in knight_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
            if square[1]=='C':
               for slot in bishop_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
            if square[1]=='D':
               for slot in queen_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
            if square[1]=='E':
               for slot in king_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
            if square[1]=='P':
               for slot in down_pawn_slots(square,board):
                  if board[slot[0]][slot[1]][0]=='u':
                     danger_squares.append(slot)
                     
def get_most_danger_square(board): #englobes the previous block-> so if we call this, we dont need to call "get_danger_squares"
   """-"""
   priority_list=['E','D','A','C','B','P']
   danger_square_list=[]
   for square in get_danger_squares(board):
      if square[1]=='E':
         danger_square_list.append(square)
         break
      elif square[1]=='D':
         danger_square_list.append(square)
         break
      elif square[1]=='A':
         danger_square_list.append(square)
         break
      elif square[1]=='C':
         danger_square_list.append(square)
         break
      elif square[1]=='B':
         danger_square_list.append(square)
         break
      elif square[1]=='P':
         danger_square_list.append(square) 
         break
   final_list=[]
   if len(danger_square_list)!=1:
      for square in danger_square_list:
         for row in board:
            if square in row:
               final_list.append(board.index(row))
               final_list.append(row.index(square))
   return(final_list)

def check(board):
   for row in board:
      for box in row:
         if box[0]=='d':
            if box[1]=='A':
               for slot1 in rook_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True
            elif box[1]=='B':
               for slot1 in knight_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True                  
            elif box[1]=='C':
               for slot1 in bishop_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True                  
            elif box[1]=='D':
               for slot1 in queen_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True                  
            elif box[1]=='E':
               for slot1 in king_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True                  
            elif box[1]=='P':
               for slot1 in down_pawn_slots(box,board):
                  if board[slot1[0]][slot1[1]][0]=='u' and board[slot1[0]][slot1[1]][1]=='E' :
                     return True   
   return False

def change_board(slot_origin,slot_destination,board):
   """-"""
   for row in board:
      for square in row:
         if square==board[slot_origin[0]][slot_origin[1]]:
               board[slot_destinatiom[0]][slot_destination[1]]=square
               board[slot_origin[0]][slot_origin[1]]=0
   return(board)
      
      
def best_move(slot_origin,list_of_slots,board):
   """-"""
   if check(board)==True:
      for slot in list_of_slots:
         if check(change_board(slot_origin,slot))==True:
            list_of_slots.pop(list_of_slots.index(slot))
   if len(list_of_slots)!=0:
      list_of_lists=[]
      new_list=[]
      for slot in list_of_slots:
         new_list=[]
         if board[slot[0]][slot[1]][0]=='d' :
            for row in change_board(slot_origin,slot,board):
               for square in row:
                  if box[0]=='d':
                     if box[1]=='A':
                        for slot1 in rook_slots(box,board):
                           if board[slot1[0]][slot1[1]][0]=='u':
                              new_list.append('A')
                     elif box[1]=='B':
                        for slot1 in knight_slots(box,board):
                           if board[slot1[0]][slot1[1]][0]=='u':
                              new_list.append('B')
                     elif box[1]=='C':
                        for slot1 in bishop_slots(box,board):
                           if board[slot1[0]][slot1[1]][0]=='u':
                              new_list.append('C')
                     elif box[1]=='D':
                        for slot1 in queen_slots(box,board):
                           if board[slot1[0]][slot1[1]][0]=='u':
                              new_list.append('D')
                     elif box[1]=='E':
                        for slot1 in king_slots(box,board):
                           if board[slot1[0]][slot1[1]][0]=='u':
                              new_list.append('E')  
         list_of_lists.append(new_list)
      final_list=[]
      for list_ in list_of_lists:
         if len(list_)==0:
            final_list.append(list_of_slots[lists_of_lists.index(list_)])
      for slot in final_list:
         if board[slot[0]][slot[1]][0]=='d':
            return(change_board(slot_origin,slot,board))
         else:
            pts=[]
            list_of_pts=[]
            for slot in list_of_slots:
               pts=[]
               new_board1=change_board(slot_origin,slot,board)
               for row in new_board1:
                     for square in row:
                        slot_of_square=[]
                        slot_of_square.append(new_board1.index(row))
                        slot_of_square.append(row.index(square))
                        if square[0]=='d':
                           if square[1]=='A':
                              for possibility in rook_slots:
                                 new_board2=change_board(new_board1[slot_of_square[0]][slot_of_square[1]],possibility,new_board1)
                                 for line in new_board2:
                                    for box in line:
                                       if box[0]=='u':
                                          if box[1]=='A':
                                             for slot1 in rook_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='d':
                                                   pts.append(1)
                                          elif box[1]=='B':
                                             for slot1 in knight_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='d':
                                                   pts.append(1)
                                          elif box[1]=='C':
                                             for slot1 in bishop_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='d':
                                                   pts.append(1)
                                          elif box[1]=='D':
                                             for slot1 in queen_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='d':
                                                   pts.append(1)
                                          elif box[1]=='E':
                                             for slot1 in king_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='d':
                                                   pts.append(1)
                                          elif box[1]=='P':
                                             for slot1 in down_pawn_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(1)
                                       if box[0]=='d':
                                          if box[1]=='A':
                                             for slot1 in rook_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)
                                          elif box[1]=='B':
                                             for slot1 in knight_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)
                                          elif box[1]=='C':
                                             for slot1 in bishop_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)
                                          elif box[1]=='D':
                                             for slot1 in queen_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)
                                          elif box[1]=='E':
                                             for slot1 in king_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)
                                          elif box[1]=='P':
                                             for slot1 in down_pawn_slots(box,board):
                                                if board[slot1[0]][slot1[1]][0]=='u':
                                                   pts.append(-1)    
               list_of_pts.append(pts)       
            list_of_sum=[]
            dummy=[]
            for pts in list_of_pts:
               list_of_sum.append(sum(pts))
            for sum_ in list_of_sum:
                  if sum_==max(list_of_sum):
                     index=list_of_sum.index(sum_)
                     break
            return(change_board(slot_origin,list_of_slots[index],board))            
   else:
      print("Checkmate to Kosaksi !")
   
                                  
def defense_move_for_danger_square(danger_slot,board):
   """-"""
   for square in get_most_danger_square(board):
      if square[1]=='E':
            return(best_move(danger_slot,king_slots(square,board),board))
      if square[1]=='D':
            return(best_move(danger_slot,queen_slots(square,board),board))
      if square[1]=='C':
            return(best_move(danger_slot,bishop_slots(square,board),board))
      if square[1]=='B':
            return(best_move(danger_slot,knight_slots(square,board),board))
      if square[1]=='A':
            return(best_move(danger_slot,rook_slots(square,board),board))
      if square[1]=='P':
            return(best_move(danger_slot,up_pawn_slots(square,board),board))
         
def check_mate(board):
   """-"""
   slot_origin=[]
   tick=[]
   for row in board:
      for square in row:
         if square[0]=='u':
            if square[1]=='E': 
               for slot in king_slots(square,board):
                  slot_origin=[]
                  slot_origin.append(board.index(row))
                  slot_origin.aooend(row.index(square))
                  if check(change_board(slot_origin,slot,board))==True:
                     tick.append(1)
               if len(king_slots(square,board))==len(tick):
                  return True
               else:
                  return False
               
def get_all_possible_moves(board):
   poss=[]
   sub=[]
   for row in board:
      for piece in row:
         if piece[0]=='u':
            sub=[]
            sub.append(piece)
            if piece[1]=='A':
               for slot in rook_slots(piece,board):
                  poss.append(slot)
            if piece[1]=='B':
               for slot in knight_slots(piece,board):
                  poss.append(slot)
            if piece[1]=='C':
               for slot in bishop_slots(piece,board):
                  poss.append(slot)
            if piece[1]=='D':
               for slot in queen_slots(piece,board):
                  poss.append(slot)
            if piece[1]=='E':
               for slot in king_slots(piece,board):
                  poss.append(slot)
            if piece[1]=='P':
               for slot in up_pawn_slots(piece,board):
                  poss.append(slot)   
         poss.append(sub)
   return(poss)
                     
         
# GAME PROCESS; TELL THE COMPUTER WHAT TO DO (WHAT TO ASK FROM KOSAKSI) AT MY EACH TURN

board=[['uA0l','uB0l','uC0l','uD0','uE0','uC0r','uB0r','uA0r'],['uP1','uP2','uP3','uP4','uP5','uP6','uP7','uP8'],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],['dP9','dP10','dP11','dP12','dP13','dP14','dP15','dP16'],['dA1l','dB1l','dC1l','dD1','dE1','dC1r','dB1r','dA1r']]

from random import randint

if randint(0,1)==0:
   print("You start !")
   board=input("Modify and paste the new board as list of list to submit your move")
else:
   print("Kosaksi will start !")
   random_slot=random.choice(get_all_possible_moves(board)
   if board[random_slot[0]][random.slot[1]][1]=='
   
   

while check_mate(board)==True:
   
      board=input("Modify and paste the new board as list of list to submit your move")
      
    



   
               
      
      
     
   
                   
               
               
