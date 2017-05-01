import itertools
import numpy as np

from sklearn import svm, linear_model, cross_validation


def transform_pairwise(X, y):
    X_new = []
    y_new = []
    y = np.asarray(y)
    if y.ndim == 1:
        y = np.c_[y, np.ones(y.shape[0])]
    comb = itertools.combinations(range(X.shape[0]), 2)
    for k, (i, j) in enumerate(comb):
        if y[i, 0] == y[j, 0] or y[i, 1] != y[j, 1]:
            # skip if same target or different group
            continue
        X_new.append(X[i] - X[j])
        y_new.append(np.sign(y[i, 0] - y[j, 0]))
        # output balanced classes
        if y_new[-1] != (-1) ** k:
            y_new[-1] = - y_new[-1]
            X_new[-1] = - X_new[-1]
    return np.asarray(X_new), np.asarray(y_new).ravel()


class RankSVM(svm.LinearSVC):
   

    def fit(self, X, y):
        X_trans, y_trans = transform_pairwise(X, y)
        super(RankSVM, self).fit(X_trans, y_trans)
        return self

    def predict(self, X):
        if hasattr(self, 'coef_'):
            np.argsort(np.dot(X, self.coef_.T))
        else:
            raise ValueError("Must call fit() prior to predict()")

    def score(self, X, y):
        X_trans, y_trans = transform_pairwise(X, y)
        return np.mean(super(RankSVM, self).predict(X_trans) == y_trans)


if __name__ == '__main__':
    # as showcase, we will create some non-linear data
    # and print the performance of ranking vs linear regression

    np.random.seed(1)
    n_samples, n_features = 300, 5
    true_coef = np.random.randn(n_features)
    X = np.random.randn(n_samples, n_features)
    noise = np.random.randn(n_samples) / np.linalg.norm(true_coef)
    y = np.dot(X, true_coef)
    y = np.arctan(y) # add non-linearities
    y += .1 * noise  # add noise
    Y = np.c_[y, np.mod(np.arange(n_samples), 5)]  # add query fake id
    cv = cross_validation.KFold(n_samples, 5)
    train, test = iter(cv).next()

    # make a simple plot out of it
    import pylab as pl
    pl.scatter(np.dot(X, true_coef), y)
    pl.title('Data to be learned')
    pl.xlabel('<X, coef>')
    pl.ylabel('y')
    pl.show()

    # print the performance of ranking
    rank_svm = RankSVM().fit(X[train], Y[train])
    print 'Performance of ranking ', rank_svm.score(X[test], Y[test])

    # and that of linear regression
    ridge = linear_model.RidgeCV(fit_intercept=True)
    ridge.fit(X[train], y[train])
    X_test_trans, y_test_trans = transform_pairwise(X[test], y[test])
    score = np.mean(np.sign(np.dot(X_test_trans, ridge.coef_)) == y_test_trans)
    print 'Performance of linear regression ', score