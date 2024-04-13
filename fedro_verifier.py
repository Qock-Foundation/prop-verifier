import sys


impl_sym = ['implies', 'IMPLIES', '->', '=>']
conj_sym = ['and', 'AND', '&&']
disj_sym = ['or', 'OR', '||']
neg_sym = ['not', 'NOT', '!', '~']
false_sym = ['false', 'FALSE', '0']


def is_implies(token):
    return token in impl_sym


def is_and(token):
    return token in conj_sym


def is_or(token):
    return token in disj_sym


def is_not(token):
    return token in neg_sym


def is_false(token):
    return token in false_sym


def matching_parenthesis(tokens, i):
    bal = 0
    for j in range(i, len(tokens)):
        if tokens[j] == '(':
            bal += 1
        elif tokens[j] == ')':
            bal -= 1
        if bal == 0:
            return j
    return -1


def parse_prop(tokens):
    if not tokens:
        raise SyntaxError('Invalid expression')
    if '(' not in tokens and ')' not in tokens:
        for i in range(len(tokens)):
            if is_implies(tokens[i]):
                return [parse_prop(tokens[:i]), tokens[i], parse_prop(tokens[i + 1:])]
        for i in range(len(tokens) - 1, -1, -1):
            if is_or(tokens[i]):
                return [parse_prop(tokens[:i]), tokens[i], parse_prop(tokens[i + 1:])]
        for i in range(len(tokens) - 1, -1, -1):
            if is_and(tokens[i]):
                return [parse_prop(tokens[:i]), tokens[i], parse_prop(tokens[i + 1:])]
        if is_not(tokens[0]):
            return [tokens[0], parse_prop(tokens[1:])]
        if len(tokens) != 1:
            raise SyntaxError('Invalid expression')
        return tokens[0]
    if '(' not in tokens and ')' in tokens:
        raise SyntaxError('Unbalanced parentheses')
    left = tokens.index('(')
    right = matching_parenthesis(tokens, left)
    if right == -1:
        raise SyntaxError('Unbalanced parentheses')
    if left == 0 and right == len(tokens) - 1:
        return parse_prop(tokens[left + 1:right])
    result = [*tokens[:left], parse_prop(tokens[left + 1:right]), *tokens[right + 1:]]
    return parse_prop(result)


def is_axiom_then1(prop):
    """
    a -> (b -> a)
    """
    try:
        a, i1, [b, i2, a_] = prop
        assert is_implies(i1) and is_implies(i2)
        assert a == a_
        return True
    except:
        return False


def is_axiom_then2(prop):
    """
    (a -> (b -> c)) -> ((a -> b) -> (a -> c))
    """
    try:
        [a, i1, [b, i2, c]], i3, [[a_, i4, b_], i5, [a__, i6, c_]] = prop
        for i in [i1, i2, i3, i4, i5, i6]:
            assert is_implies(i)
        assert a == a_ and a_ == a__
        assert b == b_
        assert c == c_
        return True
    except:
        return False


def is_axiom_and1(prop):
    """
    (a && b) -> a
    """
    try:
        [a, c1, b], i1, a_ = prop
        assert is_and(c1)
        assert is_implies(i1)
        assert a == a_
        return True
    except:
        return False


def is_axiom_and2(prop):
    """
    (a && b) -> b
    """
    try:
        [a, c1, b], i1, b_ = prop
        assert is_and(c1)
        assert is_implies(i1)
        assert b == b_
        return True
    except:
        return False


def is_axiom_and3(prop):
    """
    a -> (b -> (a && b))
    """
    try:
        a, i1, [b, i2, [a_, c1, b_]] = prop
        assert is_implies(i1) and is_implies(i2)
        assert is_and(c1)
        assert a == a_ and b == b_
        return True
    except:
        return False


def is_axiom_or1(prop):
    """
    a -> (a || b)
    """
    try:
        a, i1, [a_, d1, b] = prop
        assert is_implies(i1)
        assert is_or(d1)
        assert a == a_
        return True
    except:
        return False


def is_axiom_or2(prop):
    """
    b -> (a || b)
    """
    try:
        b, i1, [a, d1, b_] = prop
        assert is_implies(i1)
        assert is_or(d1)
        assert b == b_
        return True
    except:
        return False


def is_axiom_or3(prop):
    """
    (a -> c) -> ((b -> c) -> ((a || b) -> c))
    """
    try:
        [a, i1, c], i2, [[b, i3, c_], i4, [[a_, d1, b_], i5, c__]] = prop
        for i in [i1, i2, i3, i4, i5]:
            assert is_implies(i)
        assert is_or(d1)
        assert a == a_ and b == b_ and c == c_ and c_ == c__
        return True
    except:
        return False


def is_axiom_false(prop):
    """
    0 -> a
    """
    try:
        f, i1, a = prop
        assert is_implies(i1)
        assert is_false(f)
        return True
    except:
        return False


def follows_by_mp(prop, prev_props):
    for a_implies_b in prev_props:
        if len(a_implies_b) != 3:
            continue
        a, i1, b = a_implies_b
        if is_implies(i1) and a in prev_props and b == prop:
            return True
    return False


if __name__ == '__main__':
    author = input('Your name: ')
    print(f'Hello, {author}!')
    prev_props = []
    last_line = ''
    for i, line in enumerate(sys.stdin.readlines()):
        last_line = line.strip()
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        line = line.replace('!', '! ')
        line = line.replace('~', '~ ')
        tokens = line.split()
        prop = parse_prop(tokens)
        axiom = None
        if is_axiom_then1(prop):
            axiom = 'THEN-1'
        elif is_axiom_then2(prop):
            axiom = 'THEN-2'
        elif is_axiom_and1(prop):
            axiom = 'AND-1'
        elif is_axiom_and2(prop):
            axiom = 'AND-2'
        elif is_axiom_and3(prop):
            axiom = 'AND-3'
        elif is_axiom_or1(prop):
            axiom = 'OR-1'
        elif is_axiom_or2(prop):
            axiom = 'OR-2'
        elif is_axiom_or3(prop):
            axiom = 'OR-3'
        elif is_axiom_false(prop):
            axiom = 'FALSE'
        elif follows_by_mp(prop, prev_props):
            axiom = 'MODUS-PONENS'
        if axiom is None:
            print(f'[ERROR] proposition {i + 1}, parsed as {prop}, this proposition is not an axiom nor a corollary')
            print('PROOF IS INCORRECT')
            exit(1)
        print(f'[OK]    proposition {i + 1} follows by {axiom}')
        prev_props.append(prop)
    print('PROOF IS CORRECT :)')
    with open('accepted-proofs.html', 'a') as logs:
        logs.write(f'{author} proved that {last_line}! <br>\n')
        logs.flush()
