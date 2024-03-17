#pragma once
#include "Queue.h"
#include <iostream>
#include <math.h>
using namespace std;
template <class T>
class QueueVector :public Queue<T>
{
private:
	T* data;
	int capacity;
	int head;
	int rear;
public:
	QueueVector(int size = 100) :capacity(size), head(0), rear(0) {
		data = new T[capacity];
	};
	QueueVector(const QueueVector& source);
	~QueueVector() override;
	void clear() override;
	void enqueue(T value) override;
	T dequeue() override;
	T front()const override { return data[head]; };
	bool isEmpty()const override { return head == rear; }
};

template <class T>
QueueVector<T>::QueueVector(const QueueVector& source) {
	capacity = source.capacity;
	head = source.head;
	rear = source.rear;
	data = new T[capacity];
	for (int i = head; i != rear; i = (i + 1) % capacity) {
		data[i] = source.data[i];
	}
}
template <class T>
QueueVector<T>::~QueueVector() {
	if (data)
		delete[] data;
	data = NULL;
}

template <class T>
void QueueVector<T>::clear() {
	if (data)
		delete[]data;
	data = NULL;
	capacity = 0;
	head = 0;
	rear = 0;
}

template <class T>
void QueueVector<T>::enqueue(T value) {
	if (rear+1%capacity==head){
		throw ("Queue is full");
	}
	data[rear] = value;
	rear = (rear + 1) % capacity;
}

template <class T>
T QueueVector<T>::dequeue() {
	if (isEmpty()) {
		throw exception("Queue is empty");
	}

	T value = data[head];
	head = (head + 1) % capacity;
	return value;
}