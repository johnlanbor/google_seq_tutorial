import tensorflow as tf

session = tf.Session()
saver = tf.train.Saver()
file_path = '../tmp/nmt_model_12000/translate.ckpt-12000'
saver.restore(session, file_path)


