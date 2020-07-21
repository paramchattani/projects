# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:36:11 2020

@author: param
"""



#we will give pixels as data to our hideen layers 
''' we will go like imput --> hidden layer 1(activation function) --> output1 --> 
hidden layer 2 activation function --> output -->cost function --> optimisation -->
minimize cost --> go backward and then manipulate weights'''
# backprop + feed forward = epoch
import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data",one_hot=True)
# output as 0=[1,0,0,0,0,0,0,0,0,0] # format for one_hot 
 #          1=[0,1,0,0,0,0,0,0,0,0]
#multiclass classification 
#10 classes [0-9]
node_1=500
node_2=500
n_classes=10
batch_size=128
hm_epochs=5
# take 128 features as one time
x=tf.placeholder('float',[None,784])# only linear data of 784 pixels 
y=tf.placeholder('float')# label for the data
def nn_model(data):
    hidden_layer_1={'weights':tf.Variable(tf.random_normal([784,node_1])),'biases':tf.Variable(tf.random_normal([node_1]))}
    # we are deciding number of weighs and biases in each layer
    # i/p data * weights + bias
    hidden_layer_2={'weights':tf.Variable(tf.random_normal([node_1,node_2])),'biases':tf.Variable(tf.random_normal([node_2]))}
    output_layer={'weights':tf.Variable(tf.random_normal([node_2,n_classes])),'biases':tf.Variable(tf.random_normal([n_classes]))}
    l1=tf.add(tf.matmul(data,hidden_layer_1['weights']),hidden_layer_1['biases'])
    l1=tf.nn.relu(l1)
    l2=tf.add(tf.matmul(l1,hidden_layer_2['weights']),hidden_layer_2['biases'])
    l2=tf.nn.relu(l2)
    l3=tf.add(tf.matmul(l2,output_layer['weights']),output_layer['biases'])
    return l3

def train_neural_network(x):
    prediction=nn_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y) )
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(hm_epochs):
            epoch_loss=0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                ex,ey=mnist.train.next_batch(batch_size)
                _,c=sess.run([optimizer,cost],feed_dict={x:ex,y:ey})
                epoch_loss+=c
            print('epochs',epoch,'completed out of ',hm_epochs,'epoch error',epoch_loss)
        correct=tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
        accuracy=tf.reduce_mean(tf.cast(correct,'float'))
        print('accuracy:',accuracy.eval({x:mnist.test.images,y:mnist.test.labels}))
train_neural_network(x)        
            