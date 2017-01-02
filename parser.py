# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer import tokens

from ast_tree import Node


def load_node(p, name):
    node = Node(name)
    for i in range(1, len(p)):
        node.add(p[i])
    p[0] = node

def return_node(p, name):
    node = Node(name)
    for i in range(1, len(p)):
        node.add(p[i])
    return node

start = 'start'

def p_start(p):
    '''start : table_definition
             | select_stmt'''
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

#--------SELECT------------------------
def p_select_stmt(p):
    '''select_stmt : SELECT all_or_distinct select_expr_list FROM table_reference where_stmt group_stmt order_stmt distribute_stmt limit_stmt'''
    load_node(p, 'select_stmt')

def p_all_or_distinct(p):
    '''all_or_distinct : empty
                       | ALL 
                       | DISTINCT'''
    load_node(p, 'all_or_distinct')

def p_select_expr_list(p):
    '''select_expr_list : select_expr 
                        | select_expr_list COMMA select_expr'''
    load_node(p, 'select_expr_list')

def p_select_expr(p):
    '''select_expr : line_expr
                   | line_expr AS ID'''
    load_node(p, 'select_expr')

def p_table_reference(p):
    '''table_reference : table_name table_other_name
                       | '(' select_stmt ')' table_other_name'''
    load_node(p, 'table_reference')

def p_table_other_name(p):
    '''table_other_name : empty
                        | ID'''
    load_node(p, 'table_other_name')

def p_where_stmt(p):
    '''where_stmt : empty
                  | WHERE where_condition'''
    load_node(p, 'where_stmt')

def p_where_condition(p):
    '''where_condition : expr_list'''
    load_node(p, 'where_condition')

def p_group_stmt(p):
    '''group_stmt : empty
                  | GROUP BY col_list'''
    load_node(p, 'group_stmt')

def p_col_list(p):
    '''col_list : col_expr
                | col_list COMMA col_expr'''
    load_node(p, 'col_list')

def p_col_expr(p):
    '''col_expr : line_expr'''
    load_node(p, 'col_expr')

def p_order_stmt(p):
    '''order_stmt : empty
                  | ORDER BY order_condition'''
    load_node(p, 'order_stmt')

def p_order_condition(p):
    '''order_condition : order_expr
                       | order_condition COMMA order_expr'''
    load_node(p, 'order_condition')

def p_order_expr(p):
    '''order_expr : line_expr 
                  | line_expr ASC
                  | line_expr DESC'''
    load_node(p, 'order_expr')

def p_distribute_stmt(p):
    '''distribute_stmt : empty
                       | DISTRIBUTE BY distribute_condition sort_stmt'''
    load_node(p, 'distribute_stmt')

def p_distribute_condition(p):
    '''distribute_condition : expr_list'''
    load_node(p, 'distribute_condition')

def p_sort_stmt(p):
    '''sort_stmt : empty
                 | SORT BY sort_condition'''
    load_node(p, 'sort_stmt')

def p_sort_condition(p):
    '''sort_condition : expr_list'''
    load_node(p, 'sort_condition')

def p_limit_stmt(p):
    '''limit_stmt : empty
                  | LIMIT NUMBER'''
    load_node(p, 'limit_stmt')


#--------EXPR--------------------------
def p_expr_list(p):
    '''expr_list : line_expr 
                 | expr_list COMMA line_expr'''
    load_node(p, 'expr_list')

def p_line_expr(p):
    '''line_expr : factor_expr 
                 | line_expr factor_expr'''
    load_node(p, 'line_expr')

def p_factor_expr(p):
    '''factor_expr : '(' line_expr ')'
                   | simple_expr'''
    load_node(p, 'factor_expr')

def p_simple_expr(p):
    '''simple_expr : symbol_expr 
                   | func_expr 
                   | buildin_expr 
                   | NUMBER 
                   | STR 
                   | TRUE 
                   | FALSE 
                   | ID'''
    load_node(p, 'simple_expr')

def p_symbol_expr(p):
    '''symbol_expr : PLUS 
                   | MINUS 
                   | TIMES 
                   | DIVIDE 
                   | EQ 
                   | NE 
                   | GT 
                   | GE 
                   | LT 
                   | LE 
                   | AND 
                   | OR 
                   | NOT'''
    load_node(p, 'symbol_expr')

def p_func_expr(p):
    '''func_expr : ID '(' expr_list ')'
                 | ID ':' ID '(' expr_list ')' '''
    load_node(p, 'func_expr')

def p_buildin_expr(p):
    '''buildin_expr : cast_expr'''
    load_node(p, 'buildin_expr')


#------BUILDIN-------------------------------
def p_cast_expr(p):
    '''cast_expr : CAST '(' ID AS DATATYPE ')' '''
    load_node(p, 'cast_expr')


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

# Build the parser
parser = yacc.yacc()
