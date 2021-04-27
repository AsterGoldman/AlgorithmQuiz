def solution(board, moves):
    answer = 0
    stack = []
    for col in moves:
        for row in board:
            if row[col-1] != 0:
                if len(stack) == 0:
                    stack.append(row[col-1])
                    row[col-1] = 0
                    break
                elif stack[-1] == row[col-1]:
                    stack.pop()
                    row[col-1] = 0
                    answer += 2
                    break
                else:
                    stack.append(row[col-1])
                    row[col-1] = 0
                    break
    return answer