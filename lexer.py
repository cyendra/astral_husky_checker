import ply.lex as lex

reserved = {
    'CREATE' : 'CREATE',
    'TABLE' : 'TABLE',
    'PARTITIONED' : 'PARTITIONED',
    'BY' : 'BY',
    'COMMENT' : 'COMMENT',
    'IF' : 'IF',
    'NOT' : 'NOT',
    'EXISTS' : 'EXISTS',
    'LIFECYCLE' : 'LIFECYCLE',
    'LIKE' : 'LIKE',
    'AS' : 'AS',
    'CAST' : 'CAST',
    'TRUE' : 'BOOLEAN',
    'FALSE' : 'BOOLEAN',
    'AND' : 'AND',
    'OR' : 'OR',
    'ASC' : 'ASC',
    'DESC' : 'DESC'
}

data_types = set([
    'BIGINT',
    'DOUBLE',
    'STRING'
])

tokens = [
    'COMMA',
    'STR',
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DATATYPE'
] + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_$][a-zA-Z_0-9${}]*'
    t.type = reserved.get(t.value.upper(), 'ID')    # Check for reserved words
    if t.value.upper() in data_types:
        t.type = 'DATATYPE'
    if t.type != 'ID':
        t.value = t.value.upper()
    return t

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_COMMA   = r','

t_GE      = r'>='
t_LE      = r'<='
t_EQ      = r'=|=='
t_NE      = r'<>|!='
t_GT      = r'>'
t_LT      = r'<'




literals = [ '(', ')', '{', '}', '.' , ':']

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+|\d+\.\d+'
    if t.value.find('.') != -1:
        t.value = float(t.value)
    else:
        t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\--.*'
    pass
#------

def t_STR(t):
    r'\'.*\'|\".*\"'
    # t.value = '\"' + t.value[1:-1] + '\"'
    return t


# Build the lexer
lexer = lex.lex()
