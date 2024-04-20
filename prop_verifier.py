#!/usr/bin/python3
import sys, re
#from cPyparsing import nums, alphas, Word, oneOf, opAssoc, infixNotation
from grammar.visitor import kek_conversion

equivalences_s = ['equiv']
implications_s = ['implies']
conjunctions_s = ['and']
xors_s = ['xor']
disjunctions_s = ['or']
negations_s = ['not']
falsehoods_s = ['false']

def eq(a, a_):
  return str(a) == str(a_)

def eq3(a, a_, a__):
  return eq(a, a_) and eq(a_, a__)

def is_axiom(proposition_parsed):
  try:  # THEN-1: a implies b implies a
    a, i1, [b, i2, a_] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and eq(a, a_):
      return 1
  except: pass
  try:  # THEN-2: (a implies b implies c) implies (a implies b) implies (a implies c)
    [a, i1, [b, i2, c]], i3, [[a_, i4, b_], i5, [a__, i6, c_]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and i3 in implications_s and i4 in implications_s and i5 in implications_s and i6 in implications_s and eq3(a, a_, a__) and eq(b, b_) and eq(c, c_):
      return 2
  except: pass
  try:  # AND-1: a and b implies a
    [a, c1, b], i1, a_ = proposition_parsed
    if c1 in conjunctions_s and i1 in implications_s and eq(a, a_):
      return 3
  except: pass
  try:  # AND-2: a and b implies b
    [a, c1, b], i1, b_ = proposition_parsed
    if c1 in conjunctions_s and i1 in implications_s and eq(b, b_):
      return 4
  except: pass
  try:  # AND-3: a implies b implies a and b
    a, i1, [b, i2, [a_, c1, b_]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and c1 in conjunctions_s and eq(a, a_) and eq(b, b_):
      return 5
  except: pass
  try:  # OR-1: a implies a or b
    a, i1, [a_, d1, b] = proposition_parsed
    if i1 in implications_s and d1 in disjunctions_s and eq(a, a_):
      return 6
  except: pass
  try:  # OR-2: b implies a or b
    b, i1, [a, d1, b_] = proposition_parsed
    if i1 in implications_s and d1 in disjunctions_s and eq(b, b_):
      return 7
  except: pass
  try:  # OR-3: (a implies c) implies (b implies c) implies (a or b implies c)
    [a, i1, c], i2, [[b, i3, c_], i4, [[a_, d1, b_], i5, c__]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and i3 in implications_s and i4 in implications_s and d1 in disjunctions_s and i5 in implications_s and eq(a, a_) and eq(b, b_) and eq3(c, c_, c__):
      return 8
  except: pass
  try:  # FALSE: false implies a
    f1, i1, a = proposition_parsed
    if i1 in implications_s and f1 in falsehoods_s:
      return 9
  except: pass
  try:  # EQUIV-1: (a equiv b) implies (a implies b)
    [a, e1, b], i1, [a_, i2, b_] = proposition_parsed
    if e1 in equivalences_s and i1 in implications_s and i2 in implications_s and eq(a, a_) and eq(b, b_):
      return 10
  except: pass
  try:  # EQUIV-2: (a equiv b) implies (b implies a)
    [a, e1, b], i1, [b_, i2, a_] = proposition_parsed
    if e1 in equivalences_s and i1 in implications_s and i2 in implications_s and eq(a, a_) and eq(b, b_):
      return 11
  except: pass
  try:  # EQUIV-3: (a implies b) implies (b implies a) implies (a equiv b)
    [a, i1, b], i2, [[b_, i3, a_], i4, [a__, e1, b__]] = proposition_parsed
    if i1 in implications_s and i2 in implications_s and i3 in implications_s and i4 in implications_s and e1 in equivalences_s and eq3(a, a_, a__) and eq3(b, b_, b__):
      return 12
  except: pass
  try:  # NOT-1: not a implies (a implies false)
    [n1, a], i1, [a_, i2, f1] = proposition_parsed
    if n1 in negations_s and i1 in implications_s and i2 in implications_s and f1 in falsehoods_s and eq(a, a_):
      return 13
  except: pass
  try:  # NOT-2: (a implies false) implies not a
    [a, i1, f1], i2, [n1, a_] = proposition_parsed
    if i1 in implications_s and f1 in falsehoods_s and i2 in implications_s and n1 in negations_s and eq(a, a_):
      return 14
  except: pass
  try:  # XOR-1: a xor b implies a and not b or not a and b
    [a, x1, b], i1, [[a_, c1, [n1, b_]], d1, [[n2, a__], c2, b__]] = proposition_parsed
    if x1 in xors_s and i1 in implications_s and c1 in conjunctions_s and n1 in negations_s and d1 in disjunctions_s and n2 in negations_s and c2 in conjunctions_s and eq3(a, a_, a__) and eq3(b, b_, b__):
      return 15
  except: pass
  try:  # XOR-2: a not not b or not a and b implies a xor b
    [[a, c1, [n1, b]], d1, [[n2, a_], c2, b_]], i1, [a__, x1, b__] = proposition_parsed
    if c1 in conjunctions_s and n1 in negations_s and d1 in disjunctions_s and n2 in negations_s and c2 in conjunctions_s and i1 in implications_s and x1 in xors_s and eq3(a, a_, a__) and eq3(b, b_, b__):
      return 16
  except: pass
  return False

def follows_by_mp(proposition_parsed, theorems):
  for a_implies_b in theorems:
    if len(a_implies_b) == 3 and a_implies_b[1] in implications_s:
      a, _, b = a_implies_b
      if str(a) in map(str, theorems) and str(b) == str(proposition_parsed):
        return a, b
  return False

theorems = []

author = input('author ')
assert re.search('^[a-zA-Z0-9_]*( draft)?$', author) is not None, f'author name should be alphanumeric without spaces etc, your author name is "{author}"'
print(f'Hello, {author.strip("{} draft")}!!!\n')
skips = 0
for i, s in enumerate(sys.stdin):
  s = s[:-1].split('#')[0].split('//')[0].strip()
  #proposition_parsed = formula_t.parseString(s)[0]
  print(f'Proposition {i+1}: ', s)
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
  print('(This was recorded)')
else:
  print(f'(This proof in {i+1-skips} lines was market as draft, so not recorded)')
quit(0)
