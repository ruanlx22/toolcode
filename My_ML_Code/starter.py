#starter.py
import dataprocess
import measurement
import models
import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing



if __name__ == '__main__':
	#DATA
	X_train, Y_train = dataprocess.get_data(path = '../data/trainingset.csv')
	X_cross, Y_cross = dataprocess.get_data(path = '../data/crossset.csv')
	X_test, Y_test = dataprocess.get_data(path = '../data/testset.csv')
	X_train = dataprocess.addDimensional(X_train)
	X_cross = dataprocess.addDimensional(X_cross)

	#model selction
	model_lrr, fig_pr_lrr = models.model_liner_logistic_regression(X_train, Y_train)
	Y_cross_pred = model_lrr.predict(X_cross)
	
	#F1 score:
	print(measurement.f1(Y_cross, Y_cross_pred))

	#draw figue
	# plt.show(fig_pr_lrr)
	# fig_db_lrr = measurement.draw_decision_boundary_2D(X_train, Y_train, X_cross, Y_cross)
	# plt.show(fig_db_lrr)
