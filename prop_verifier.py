#!/usr/bin/python3

import sys, re
from cPyparsing import nums, alphas, Word, oneOf, opAssoc, infixNotation

implications_s = ['implies', 'IMPLIES', '->', '=>']
conjunctions_s = ['and', 'AND', '&&']
disjunctions_s = ['or', 'OR', '||']
negations_s = ['not', '!', '~']
falsehoods_s = ['false', 'FALSE', '0']

variables_t = Word(alphas)
formula_t = infixNotation(variables_t, [
                (oneOf(negations_s), 1, opAssoc.RIGHT),
                (oneOf(disjunctions_s), 2, opAssoc.LEFT),
                (oneOf(conjunctions_s), 2, opAssoc.LEFT),
                (oneOf(implications_s), 2, opAssoc.RIGHT),
              ])

def is_axiom(proposition_parsed):
  try: # THEN-1: a implies b implies a
    a, i1, [b, i2, a_] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and str(a) == str(a_):
      return True
  except:
    pass
  try: # THEN-2: (a implies b implies c) implies (a implies b) implies (a implies c)
    [a, i1, [b, i2, c]], i3, [[a_, i4, b_], i5, [a__, i6, c_]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and i3 in implications_s and i4 in implications_s and i5 in implications_s and i6 in implications_s and str(a) == str(a_) == str(a__) and str(b) == str(b_) and str(c) == str(c_):
      return True
  except:
    pass
  try: # AND-1: a and b implies a
    [a, c1, b], i1, a_ = proposition_parsed
    if c1 in conjunctions_s and i1 in implications_s and str(a) == str(a_):
      return True
  except:
    pass
  try: # AND-2: a and b implies b
    [a, c1, b], i1, b_ = proposition_parsed
    if c1 in conjunctions_s and i1 in implications_s and str(b) == str(b_):
      return True
  except:
    pass
  try: # AND-3: a implies b implies a and b
    a, i1, [b, i2, [a_, c1, b_]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and c1 in conjunctions_s and str(a) == str(a_) and str(b) == str(b_):
      return True
  except:
    pass
  try: # OR-1: a implies a or b
    a, i1, [a_, d1, b] = proposition_parsed
    if i1 in implications_s and d1 in disjunctions_s and str(a) == str(a_):
      return True
  except:
    pass
  try: # OR-2: b implies a or b
    b, i1, [a, d1, b_] = proposition_parsed
    if i1 in implications_s and d1 in disjunctions_s and str(b) == str(b_):
      return True
  except:
    pass
  try: # OR-3: (a implies c) implies (b implies c) implies (a or b implies c)
    [a, i1, c], i2, [[b, i3, c_], i4, [[a_, d1, b_], i5, c__]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and i3 in implications_s and i4 in implications_s and d1 in disjunctions_s and i5 in implications_s and str(a) == str(a_) and str(b) == str(b_) and str(c) == str(c_) == str(c__):
      return True
  except:
    pass
  try: # FALSE: false implies a
    false, i1, a = proposition_parsed
    if i1 in implications_s and false in falsehoods_s:
      return True
  except:
    pass
  return False

def follows_by_mp(proposition_parsed, theorems):
  for a_implies_b in theorems:
    if len(a_implies_b) == 3 and a_implies_b[1] in implications_s:
      a, _, b = a_implies_b
      if str(a) in map(str, theorems) and str(b) == str(proposition_parsed):
        return True
  return False

theorems = []

author = input('author ')
assert re.search('^[a-zA-Z0-9_]*$', author) is not None, f'author name should be alphanumeric without spaces etc, your author name is "{author}"'
print(f'Hello, {author}!!!')
for i, s in enumerate(sys.stdin):
  s = s[:-1]
  proposition_parsed = formula_t.parseString(s)[0]
  print('parsed as', proposition_parsed)
  if is_axiom(proposition_parsed):
    print(f'proposition {i} recognized as axiom')
    theorems.append(proposition_parsed)
  elif follows_by_mp(proposition_parsed, theorems):
    print(f'proposition {i} follows by Modus Ponens, indeed')
    theorems.append(proposition_parsed)
  else:
    print(f'ERROR on line {i}: got "{s}", parsed as {proposition_parsed}, this proposition is not an axiom and doesn\'t follow from the previous ones by Modus Ponens')
    print('PROOF IS INCORRECT.')
    quit(1)
  sys.stdout.flush()
print('PROOF IS CORRECT! :)')

with open('accepted-proofs.html', 'a') as logs:
  logs.write(f'{author} proved that {s}! <br>\n')
  logs.flush()
quit(0)
