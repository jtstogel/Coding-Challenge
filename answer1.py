import collections
from fractions import gcd
# Started at 10:32


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

"""
Solves problem by simulating procedure... O(mn), where m is the answer
"""
def answer_inefficient_brute_force(n):
  deck = list(range(n))
  n = 1
  perform_procedure(deck)
  while not is_ordered_deck(deck):
    perform_procedure(deck)
    n += 1
  return n

def lcm(x, y):
  return x * y // gcd(x, y)


"""
Solves problem by finding the period of each card's path then taking the lcm -> O(n)
"""
def answer(n):
  min_period = 1
  deck_mapping = list(range(n))
  perform_procedure(deck_mapping)
  # we will find the period of all cards now
  unaccounted_for = set(range(n))
  while unaccounted_for:
    x = unaccounted_for.pop()
    curr = deck_mapping[x]
    period = 1
    while curr != x:
      # anything along our path has the same period as x, so we can remove dup computation
      unaccounted_for.remove(curr)
      curr = deck_mapping[curr]
      period += 1
    min_period = lcm(min_period, period)
  return min_period


if __name__ == '__main__':
  for i in range(1, 500):
    lcm_method = answer(i)
    print(i, lcm_method)




