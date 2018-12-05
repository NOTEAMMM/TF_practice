import numpy
import tensorflow as tf

input1 = tf.placeholder(dtype=float)
input2 = tf.placeholder(dtype=float)
output = tf.matmul(input1,input2)

with tf.Session() as sess:
    print (sess.run([output],feed_dict={input1:[[1.,3.]],input2:[[2.],[5.]]}))