## Linear Regression

In statistics, linear regression is a linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables). The case of one explanatory variable is called simple linear regression. For more than one explanatory variable, the process is called multiple linear regression. This term is distinct from multivariate linear regression, where multiple correlated dependent variables are predicted, rather than a single scalar variable.

In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Such models are called linear models. Most commonly, the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly, the conditional median or some other quantile is used. Like all forms of regression analysis, linear regression focuses on the conditional probability distribution of the response given the values of the predictors, rather than on the joint probability distribution of all of these variables, which is the domain of multivariate analysis.

## Implementing Linear Regression

We will use ordinary least square method to implement linear regression using python.
Let X be the independent variable and Y be the dependent variable. A loss function in machine learning is simply a measure of how different the predicted values are from the actual values.

Now, to minimize the loss function we use the least squares method. Thus, we can determine the values of slope(m) and intercept(c).

<img src="content\least_square_formula.png" alt="least-squares-formula">

_linear_regression.py_ contains the complete code implementation of linear regression using the least square method.
