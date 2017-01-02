# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

from ast_tree import Node

def load_node(name):
    def _deco(func):
        def _func(self, p):
            func(self, p)
            node = Node(name)
            for i in range(1, len(p)):
                node.add(p[i])
            p[0] = node
        return _func
    return _deco


start = 'start'

def p_start(p):
    '''start : table_definition'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_table_name(p):
    '''table_name : ID
                  | ID '.' ID'''
    node = Node("table_name")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_table_col_list(p):
    '''table_col_list : table_col_term
                      | table_col_list COMMA table_col_term'''
    node = Node("table_col_list")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_table_col_term(p):
    '''table_col_term : ID DATATYPE table_comment'''
    node = Node("table_col_term")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_table_comment(p):
    '''table_comment : empty
                     | COMMENT STR'''
    node = Node("table_comment")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_table_partitioned(p):
    '''table_partitioned : empty
                         | PARTITIONED BY '(' table_col_list ')' '''
    node = Node("table_partitioned")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_table_lifecycle(p):
    '''table_lifecycle : empty
                       | LIFECYCLE NUMBER'''
    node = Node("table_lifecycle")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def p_if_not_exists(p):
    '''if_not_exists : empty 
                     | IF NOT EXISTS'''
    node = Node("if_not_exists")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node


def p_table_definition(p):
    '''table_definition : CREATE TABLE if_not_exists table_name '(' table_col_list ')' table_comment table_partitioned table_lifecycle
                        | CREATE TABLE if_not_exists table_name LIKE table_name'''
    node = Node("table_definition")
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node


# -------EXPR------------------------
@load_node("expr_list")
def p_expr_list(p):
    '''expr_list : line_expr 
                 | expr_list COMMA line_expr'''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

# Build the parser
parser = yacc.yacc()
