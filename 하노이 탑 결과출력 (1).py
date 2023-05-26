MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"

def move(N, start, end):
  print(MSG_FORMAT.format(N, start, end))

def hanoi(N, start, end, sub):
  if N == 1:
    move(1, start, end)
    return
  else:
    hanoi(N-1, start, sub, end)
    move(N, start, end)
    hanoi(N-1, sub, end, start)
hanoi(3, "A", "C", "B")