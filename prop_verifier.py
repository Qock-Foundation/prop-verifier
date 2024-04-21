#!/usr/bin/python3
import sys, re
#from cPyparsing import nums, alphas, Word, oneOf, opAssoc, infixNotation
from grammar.visitor import kek_conversion

def eq(a, a_):
  return str(a) == str(a_)

def eq3(a, a_, a__):
  return eq(a, a_) and eq(a_, a__)

def is_axiom(p):
  equivalence = lambda l : isinstance(l, list) and len(l) == 3 and l[1] == 'equiv'
  implication = lambda l : isinstance(l, list) and len(l) == 3 and l[1] == 'implies'
  disjunction = lambda l : isinstance(l, list) and len(l) == 3 and l[1] == 'or'
  xor = lambda l : isinstance(l, list) and len(l) == 3 and l[1] == 'xor'
  conjunction = lambda l : isinstance(l, list) and len(l) == 3 and l[1] == 'and'
  negation = lambda l : isinstance(l, list) and len(l) == 2 and l[0] == 'not'
  falsehood = lambda l : l == 'false'
  #print(implication(p), implication(p[2]), eq(p[0], p[2]
  if implication(p) and implication(p[2]) and eq(p[0], p[2][2]):
    return 1  # THEN-1: a implies b implies a
  if implication(p) and implication(p[0]) and implication(p[0][2]) and implication(p[2]) and implication(p[2][0]) and implication(p[2][2]) and eq3(p[0][0], p[2][0][0], p[2][2][0]) and eq(p[0][2][0], p[2][0][2]) and eq(p[0][2][2], p[2][2][2]):
    return 2  # THEN-2: (a implies b implies c) implies (a implies b) implies (a implies c)
  if implication(p) and conjunction(p[0]) and eq(p[0][0], p[2]):
    return 3  # AND-1: a and b implies a
  if implication(p) and conjunction(p[0]) and eq(p[0][2], p[2]):
    return 4  # AND-2: a and b implies b
  if implication(p) and implication(p[2]) and conjunction(p[2][2]) and eq(p[0], p[2][2][0]) and eq(p[2][0], p[2][2][2]):
    return 5  # AND-3: a implies b implies a and b
  if implication(p) and disjunction(p[2]) and eq(p[0], p[2][0]):
    return 6  # OR-1: a implies a or b
  if implication(p) and disjunction(p[2]) and eq(p[0], p[2][2]):
    return 7  # OR-2: b implies a or b
  if implication(p) and implication(p[0]) and implication(p[2]) and implication(p[2][0]) and implication(p[2][2]) and disjunction(p[2][2][0]) and eq(p[0][0], p[2][2][0][0]) and eq(p[2][0][0], p[2][2][0][2]) and eq3(p[0][2], p[2][0][2], p[2][2][2]):
    return 8  # OR-3: (a implies c) implies (b implies c) implies (a or b implies c)
  if implication(p) and falsehood(p[0]):
    return 9  # FALSE: false implies a
  if implication(p) and equivalence(p[0]) and implication(p[2]) and eq(p[0][0], p[2][0]) and eq(p[0][2], p[2][2]):
    return 10 # EQUIV-1: (a equiv b) implies (a implies b)
  if implication(p) and equivalence(p[0]) and implication(p[2]) and eq(p[0][0], p[2][2]) and eq(p[0][2], p[2][0]):
    return 11 # EQUIV-2: (a equiv b) implies (b implies a)
  if implication(p) and implication(p[0]) and implication(p[2]) and implication(p[2][0]) and equivalence(p[2][2]) and eq3(p[0][0], p[2][0][2], p[2][2][0]) and eq3(p[0][2], p[2][0][0], p[2][2][2]):
    return 12 # EQUIV-3: (a implies b) implies (b implies a) implies (a equiv b)
  if implication(p) and negation(p[0]) and implication(p[2]) and falsehood(p[2][2]) and eq(p[0][1], p[2][0]):
    return 13 # NOT-1: not a implies (a implies false)
  if implication(p) and implication(p[0]) and falsehood(p[0][2]) and negation(p[2]) and eq(p[0][0], p[2][1]):
    return 14 # NOT-2: (a implies false) implies not a
  if implication(p) and xor(p[0]) and disjunction(p[2]) and conjunction(p[2][0]) and negation(p[2][0][2]) and conjunction(p[2][2]) and negation(p[2][2][0]) and eq3(p[0][0], p[2][0][0], p[2][2][0][1]) and eq3(p[0][2], p[2][0][2][1], p[2][2][2]):
    return 15 # XOR-1: a xor b implies a and not b or not a and b
  if implication(p) and disjunction(p[0]) and conjunction(p[0][0]) and negation(p[0][0][2]) and conjunction(p[0][2]) and negation(p[0][2][0]) and xor(p[2]) and eq3(p[0][0][0], p[0][2][0][1], p[2][0]) and eq3(p[0][0][2][1], p[0][2][2], p[2][2]):
    return 16 # XOR-2: a and not b or not a and b implies a xor b
  return False

def follows_by_mp(proposition_parsed, theorems):
  for a_implies_b in theorems:
    if len(a_implies_b) == 3 and a_implies_b[1] == 'implies':
      a, _, b = a_implies_b
      if str(a) in map(str, theorems) and str(b) == str(proposition_parsed):
        return a, b
  return False

theorems = []

author = input('author ')
assert re.search('^[a-zA-Z0-9_]*( draft)?$', author) is not None, f'author name should be alphanumeric without spaces etc, your author name is "{author}"'
print(f'Hello, {author[:-6] if author.endswith(" draft") else author}!!!\n')
i, skips = -1, 0
for i, s in enumerate(sys.stdin):
  s = s[:-1].split('#')[0].split('//')[0].strip()
  #proposition_parsed = formula_t.parseString(s)[0]
  print(f'Line {i+1}: ', s)
  if s == '':
    skips += 1
    print(f'NOTE on line {i+1}: empty proposition, not counted (skipped lines so far: {skips})')
    continue
  if s == 'stop':
    print(f'NOTE on line {i+1}: stopword read, exiting')
    quit(0)
  proposition_parsed = kek_conversion(s)
  print('  parsed as:    ', str(proposition_parsed))
  axiom_i = is_axiom(proposition_parsed)
  if axiom_i:
    print(f'  recognized as axiom {axiom_i}')
    theorems.append(proposition_parsed)
  else:
    mp_info = follows_by_mp(proposition_parsed, theorems)
    if mp_info:
      premise, conclusion = mp_info
      print(f'  follows by Modus Ponens with premise {premise} and conclusion {conclusion}, indeed')
      theorems.append(proposition_parsed)
    else:
      print(f'\nERROR on line {i+1}: got "{s}", parsed as {proposition_parsed}, this proposition is not an axiom and doesn\'t follow from the previous ones by Modus Ponens')
      print('PROOF IS INCORRECT.')
      quit(1)
  sys.stdout.flush()
print('PROOF IS CORRECT! :)\n')

from logs_filename import logs_filename

if author[-6:] != ' draft':
  with open(logs_filename, 'a') as logs:
    logs.write(f'{author} proved that {s} in {i+1-skips} lines! <br>\n')
    logs.flush()
  print(f'(This was proof in {i+1-skips} propositions was recorded)')
elif i + 1 - skips > 0:
  print(f'(This proof in {i+1-skips} propositions was market as draft, so not recorded)')
else:
  print(f'(This proof contains {i+1} lines, all {skips} of which are comments/empty, so nothing recorded)')
quit(0)
