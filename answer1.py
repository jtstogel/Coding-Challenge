import collections

"""
Started at 10:32
The front of the array is the top
The back is the bottom
"""


"""
  Performs the procedure below, mutating the input array. 
  Index 0 of the input array corresponds to the top of the deck.
  a. Take the top card off the deck and set it on the table (build a stack on the table)
  b. Take the next card off the top of deck and put it on the bottom of the deck in your hand.
  c. Continue doing (a) and (b) until all the cards are on the table stack.
"""
def perform_procedure(arr):
  deque = collections.deque(arr)
  i = len(arr) - 1
  while len(deque):
    arr[i] = deque.popleft()
    i -= 1
    if len(deque):
      deque.append(deque.popleft())
  return arr

def is_ordered_deck(arr):
  return all(map(lambda x: x[0]==x[1],
                 zip(arr, range(len(arr)))))

def answer_inefficient_brute_force(n):
  arr = list(range(n))
  n = 1
  perform_procedure(arr)
  while not is_ordered_deck(arr):
    perform_procedure(arr)
    n += 1
  return n


if __name__ == '__main__':
  for i in range(1, 10):
    print(i, answer_inefficient_brute_force(i))
