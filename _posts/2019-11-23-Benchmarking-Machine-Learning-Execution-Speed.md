---
layout: post
permalink: blog/blog33/
categories: [Machine Learning]
---

![](https://www.freecodecamp.org/news/content/images/size/w2000/2019/11/gpu.jpg)
(Source: https://hardzone.es/noticias/tarjetas-graficas/nvidia-hopper-arquitectura-mcm/)

<!--end_excerpt-->

# Benchmarking Machine Learning Execution Speed

## Introduction

Thanks to recent advances in storage capacity and memory management, it has
become much easier to create Machine Learning and Deep Learning projects from
the comfort of our house. In this article, I will introduce you to different
possible approaches to realise Machine Learning projects in Python and give you
some indications on their trade-offs in execution speed. Some of the different
approaches are:

* Using a personal computer/laptop CPU (Central processing unit)/GPU (Graphics
processing unit)
* Using cloud services (eg. Kaggle, Google Colab)

First of all, we need to import all the necessaries dependencies.

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from xgboost import XGBClassifier
    import xgboost as xgb
    from sklearn.metrics import accuracy_score

For this example, I decided to fabricate a simple dataset using Gaussian
Distributions consisting of four features and two labels (0/1).

    # Creating a linearly separable dataset using Gaussian Distributions.
    # The first half of the number in Y is 0 and the other half 1.
    # Therefore I made the first half of the 4 features quite different from
    # the second half of the features (setting the value of the means quite
    # similar) so that make quite simple the classification between the
    # classes (the data is linearly separable).
    dataset_len = 40000000
    dlen = int(dataset_len/2)
    X_11 = pd.Series(np.random.normal(2,2,dlen))
    X_12 = pd.Series(np.random.normal(9,2,dlen))
    X_1 = pd.concat([X_11, X_12]).reset_index(drop=True)
    X_21 = pd.Series(np.random.normal(1,3,dlen))
    X_22 = pd.Series(np.random.normal(7,3,dlen))
    X_2 = pd.concat([X_21, X_22]).reset_index(drop=True)
    X_31 = pd.Series(np.random.normal(3,1,dlen))
    X_32 = pd.Series(np.random.normal(3,4,dlen))
    X_3 = pd.concat([X_31, X_32]).reset_index(drop=True)
    X_41 = pd.Series(np.random.normal(1,1,dlen))
    X_42 = pd.Series(np.random.normal(5,2,dlen))
    X_4 = pd.concat([X_41, X_42]).reset_index(drop=True)
    Y = pd.Series(np.repeat([0,1],dlen))
    df = pd.concat([X_1, X_2, X_3, X_4, Y], axis=1)
    df.columns = ['X1', 'X2', 'X3', 'X_4', 'Y']
    df.head()

![](https://www.freecodecamp.org/news/content/images/2019/11/image-32.png) <br>
<span class="figcaption_hack">Figure 1: Example Dataset</span>

Finally, we just have now to prepare our dataset to be fed in a Machine Learning
model (dividing it in features and labels, and training and test sets).

    train_size = 0.80
    X = df.drop(['Y'], axis = 1).values
    y = df['Y']

    # label_encoder object knows how to understand word labels.
    label_encoder = preprocessing.LabelEncoder()

    # Encode labels
    y = label_encoder.fit_transform(y)

    # identify shape and indices
    num_rows, num_columns = df.shape
    delim_index = int(num_rows * train_size)

    # Splitting the dataset in training and test sets
    X_train, y_train = X[:delim_index, :], y[:delim_index]
    X_test, y_test = X[delim_index:, :], y[delim_index:]

    # Checking sets dimensions
    print('X_train dimensions: ', X_train.shape, 'y_train: ', y_train.shape)
    print('X_test dimensions:', X_test.shape, 'y_validation: ', y_test.shape)

    # Checking dimensions in percentages
    total = X_train.shape[0] + X_test.shape[0]
    print('X_train Percentage:', (X_train.shape[0]/total)*100, '%')
    print('X_test Percentage:', (X_test.shape[0]/total)*100, '%')

The output train test split result is shown below.

    X_train dimensions:  (32000000, 4) y_train:  (32000000,)
    X_test dimensions: (8000000, 4) y_validation:  (8000000,)
    X_train Percentage: 80.0 %
    X_test Percentage: 20.0 %

We are now ready to get started benchmarking the different approaches. In all
the following examples, we will be using [XGBoost (Gradient Boosted Decision
Trees)](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d)
as our classifier.

## 1) CPU

Training an XGBClassifier on my personal machine (without using a GPU), led to
the following results.

    %%time

    model = XGBClassifier(tree_method='hist')
    model.fit(X_train, y_train)



    CPU times: user 8min 1s, sys: 5.94 s, total: 8min 7s
    Wall time: 8min 6s
    XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                  colsample_bynode=1, colsample_bytree=1, gamma=0,
                  learning_rate=0.1, max_delta_step=0, max_depth=3,
                  min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
                  nthread=None, objective='binary:logistic', random_state=0,
                  reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
                  silent=None, subsample=1, tree_method='hist', verbosity=1)

Once trained our model, we can now check it's prediction accuracy.

    sk_pred = model.predict(X_test)
    sk_pred = np.round(sk_pred)
    sk_acc = round(accuracy_score(y_test, sk_pred), 2)
    print("XGB accuracy using Sklearn:", sk_acc*100, '%')



    XGB accuracy using Sklearn: 99.0 %

In summary, using a standard CPU machine, it took about 8 minutes to train our
classifier to achieve 99% accuracy.

## 2) GPU

I will now instead make use of an [NVIDIA TITAN RTX
GPU](https://www.nvidia.com/en-gb/deep-learning-ai/products/titan-rtx/) on my
personal machine to speed up the training. In this case, in order to activate
the GPU mode of XGB, we need to specify the **tree_method** as **gpu_hist**
instead of **hist**.

    %%time

    model = XGBClassifier(tree_method='gpu_hist')
    model.fit(X_train, y_train)

Using the TITAN RTX led in this example to just 8.85 seconds of execution time
(about 50 times faster than using just the CPU!).

    sk_pred = model.predict(X_test)
    sk_pred = np.round(sk_pred)
    sk_acc = round(accuracy_score(y_test, sk_pred), 2)
    print("XGB accuracy using Sklearn:", sk_acc*100, '%')


    XGB accuracy using Sklearn: 99.0 %

This considerable improvement in speed, was possible thanks to the ability of
GPUs of taking load off from the CPU, freeing up RAM memory and parallelizing
the execution of multiple tasks.

## 3) GPU Cloud Services

I will now provide you two examples of free GPU cloud services (Google Colab and
Kaggle) and show you what benchmark score they are able to achieve. In both
cases, we need to explicitly turn on the GPUs on the respective notebooks and
specify the XGBoost **tree_method** as **gpu_hist**.

### Google Colab

Using Google Colab NVIDIA TESLA T4 GPUs, the following scores have been
registered.

    CPU times: user 5.43 s, sys: 1.88 s, total: 7.31 s
    Wall time: 7.59 s

### Kaggle

Using Kaggle instead, led to a slightly higher execution time.

    CPU times: user 5.37 s, sys: 5.42 s, total: 10.8 s
    Wall time: 11.2 s
    XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                  colsample_bynode=1, colsample_bytree=1, gamma=0,
                  learning_rate=0.1, max_delta_step=0, max_depth=3,
                  min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
                  nthread=None, objective='binary:logistic', random_state=0,
                  reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
                  silent=None, subsample=1, tree_method='gpu_hist', verbosity=1)

Using either Google Colab or Kaggle led in both circumstances to a remarkable
decrease in execution time. One downside of using these services can be although
the limited amount of CPU and RAM available. In fact, slightly increasing the
dimensions of the example dataset used caused Google Colab to run out of RAM
memory (this problem was instead not registered when using the TITAN RTX). One
possible way to fix this type problem when working with constrained memory
devices is to optimise the code to  consume less memory as possible (eg. using
fixed points precision and more efficient data structures).

## 4) Bonus Point: RAPIDS

As an additional point, I will now introduce you to RAPIDS, an NVIDIA
open-source collection of Python libraries. In this example, we will make use of
it's integration with the XGBoost library to speed up our workflow in Google
Colab. The full notebook for this example (with instructions on how to set up
RAPIDS in Google Colab) is available
[here.](https://drive.google.com/open?id=1LZzK-iq9xEEuOfEpv2SLeCyV6ksx0kio)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    %%time

    params = {}
    booster_params = {}
    booster_params['tree_method'] = 'gpu_hist'
    params.update(booster_params)

    clf = xgb.train(params, dtrain)



    CPU times: user 1.42 s, sys: 719 ms, total: 2.14 s
    Wall time: 2.51 s

As we can see above, using RAPIDS it took just about 2.5 seconds to train our
model (decreasing time execution by almost 200 times!).

Finally, we can now check that using RAPIDS we obtained exactly the same
prediction accuracy registered in the other cases.

    rapids_pred = clf.predict(dtest)

    rapids_pred = np.round(rapids_pred)
    rapids_acc = round(accuracy_score(y_test, rapids_pred), 2)
    print("XGB accuracy using RAPIDS:", rapids_acc*100, '%')



    XGB accuracy using RAPIDS: 99.0 %

If you are interested in finding out more about RAPIDS, more information are
available at [this
link.](https://towardsdatascience.com/gpu-accelerated-data-analytics-machine-learning-963aebe956ce)

## Conclusion

Finally, we can now compare the execution time of the different methods used. As
shown in Figure 2, using GPU optimisation can substantially decrease execution
time especially if integrated with the use of RAPIDS libraries.

![](https://www.freecodecamp.org/news/content/images/2019/11/image-37.png) <br>
<span class="figcaption_hack">Figure 2: Execution Time comparison</span>

In Figure 3, is additionally shown how many times faster the GPUs models are
compared to our baseline CPU results.

![](https://www.freecodecamp.org/news/content/images/2019/11/image-38.png) <br>
<span class="figcaption_hack">Figure 3: Focus on CPU Execution TIme Comparison</span>
