#pragma once
#include "Tree.h"
#include <iostream>
using namespace std;

template<class T>
class SearchTree : public Tree<T>
{
public:
	void add(T value) override;
	bool  search(T value) override;
	void remove(T value) override;

private:
	void add(typename Tree<T>::Node* current, T val);
	bool  search(typename Tree<T>::Node* current, T val);
	typename Tree<T>::Node* find(typename Tree<T>::Node* current, T val);
};

template <class T>
void SearchTree<T>::add(T val)
{
	// add value to binary search tree 
	if (!Tree<T>::root)
	{
		Tree<T>::root = new typename Tree<T>::Node(val);
		return;
	}
	add(Tree<T>::root, val);
}

template <class T>
void SearchTree<T>::add(typename Tree<T>::Node* current, T val)
{
	if (current->value < val)

		if (!current->right)
		{
			current->right = new typename Tree<T>::Node(val);
			current->right->parent = current;
			return;
		}
		else add(current->right, val);
	else

		if (!current->left)
		{
			current->left = new  typename Tree<T>::Node(val);
			current->left->parent = current;
			return;
		}
		else add(current->left, val);
}

template <class T>
bool SearchTree<T>::search(T value)
{
	return search(Tree<T>::root, value);
}
template <class T>
bool SearchTree<T>::search(typename Tree<T>::Node* current, T val)
{
	// see if argument value occurs in tree
	if (!current)
		return false;	// not found
	if (current->value == val)
		return true;
	if (current->value < val)
		return search(current->right, val);
	else
		return search(current->left, val);
}
template <class T>
typename Tree<T>::Node* SearchTree<T>::find(typename Tree<T>::Node* current, T val)
{
	// see if argument value occurs in tree
	if (!current)
		return NULL;	// not found
	if (current->value == val)
		return current;
	if (current->value < val)
		return find(current->right, val);
	else
		return find(current->left, val);
}
template <class T>
void SearchTree<T>::remove(T val)
{
	typename Tree<T>::Node* node = find(Tree<T>::root, val);
	if (!node)
		return;
	if (!node->left && !node->right) {
		if (node->parent)
		{
			if (node->parent->left == node)
				node->parent->left = NULL;
			else
				node->parent->right = NULL;
		}
		else
		{
			Tree<T>::root = NULL;
		}
		delete node;
	}
	else if (!node->left || !node->right)
	{
		typename Tree<T>::Node* child = node->left ? node->left : node->right;
		if (node->parent)
		{
			if (node->parent->left == node)
				node->parent->left = child;
			else
				node->parent->right = child;
		}
		else
			Tree<T>::root = child;
		delete node;
	}
	else {
		typename Tree<T>::Node* successor = node->right;
		while (successor->left)
			successor = successor->left;

		node->value = successor->value;

		if (successor->parent->left == successor)
			successor->parent->left = successor->right;
		else
			successor->parent->right = successor->right;

		if (successor->right)
			successor->right->parent = successor->parent;

		delete successor;
	}
}
