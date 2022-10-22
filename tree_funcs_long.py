""" File: tree_funcs_long.py
    Author: Andrew Le
    Purpose: This program contains several function that will be used to traverse through trees. Some trees might be Binary Search trees
    and some may not. Using loops and recursion each function must be able to complete its given task by the prompt. Some functions
   will have to handle empty trees and some assume the trees are not empty.
"""

from tree_node import TreeNode


def bst_search_loop(root, val):
    '''
    This function will traverse through a binary tree using a while loop
    to find a given parameter value. If the value is found, return the node
    that contains the value. if not, return "None"
    '''
    if root is None:
        return None
    while root != None:
        if val > root.val:
            root = root.right
        elif val < root.val:
            root = root.left
        else:
            return root
            return None


def tree_search(root, val):
    '''
    This function will traverse through a given tree for a given parameter value.
    If the value is found, return the node which contains it, if not return None.
    this function will not assume if the tree is binary or not/ the order of the values.
    '''
    if root == None:
        return None
    if root.val == val:
        return root
    left_node = tree_search(root.left, val)
    if left_node != None:
        return left_node
    right_node = tree_search(root.right,val)
    if right_node != None:
        return right_node

def bst_insert_loop(root,val):
    '''
    This function will insert a given parameter variable "value" into a given paramter
    variable "root" tree without using recursion. nothing will be returned, the function
    will simply process the root and value.
    '''
    cur = root
    parent= None
    while cur:
        parent = cur
        if val < cur.val:
            cur = cur.left
        else:
            cur = cur.right
    if val < parent.val:
        parent.left = TreeNode(val)
    else:
        parent.right = TreeNode(val)
def pre_order_traversal_print(root):
    '''
    This function will traverse through the given tree in "pre-order" order.
    then the function will print out the tree in the given order one value per line.
    '''
    if root is None:
        return
    print(root.val)
    pre_order_traversal_print(root.left)
    pre_order_traversal_print(root.right)

def in_order_traversal_print(root):
    '''
    This function will traverse through the given tree in "in-order" order.
    then the function will print out the tree in the given order one value per line.
    '''
    if root is None:
        return
    in_order_traversal_print(root.left)
    print(root.val)
    in_order_traversal_print(root.right)

def post_order_traversal_print(root):
    '''
    This function will traverse through the given tree in "post-order" order.
    then the function will print out the tree in the given order one value per line.
    '''
    if root is None:
        return
    post_order_traversal_print(root.left)
    post_order_traversal_print(root.right)
    print(root.val)

def in_order_vals(root):
    '''
    This function will take in a tree and traverse through the tree in "in order" order
    the function will then return an array in the same order.
    '''
    if root is None:
        return []
    left_list = in_order_vals(root.left)
    right_list = in_order_vals(root.right)
    return left_list + [root.val] + right_list

def bst_max(root):
    '''
    This function will traverse through a given tree "root", (assuming the tree is a BST) and find
    the maximum value of the tree using a while loop to find the right-most node in the tree.
    '''
    cur = root
    while cur.right != None:
        cur = cur.right
    return cur.val


def tree_max(root):
    '''
    This function will return the maximum value of a given tree NOT assuming the tree is a
    BST, the function will loop through each value to find the maximum of both the right
    and left children until the maximum of those values is found.
    '''
    val = []
    val.append(root)
    maximum = -1
    while(len(val)>0):
        cur = val[0]
        val.pop(0)
        if maximum == -1 or cur.val > maximum:
            maximum = cur.val
        if cur.left != None:
            val.append(cur.left)
        if cur.right != None:
            val.append(cur.right)
    return maximum




























