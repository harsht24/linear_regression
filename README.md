# Linear Regression

In statistics, linear regression is a linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables). The case of one explanatory variable is called simple linear regression. For more than one explanatory variable, the process is called multiple linear regression. This term is distinct from multivariate linear regression, where multiple correlated dependent variables are predicted, rather than a single scalar variable.

In linear regression, the relationships are modeled using linear predictor functions whose unknown model parameters are estimated from the data. Such models are called linear models. Most commonly, the conditional mean of the response given the values of the explanatory variables (or predictors) is assumed to be an affine function of those values; less commonly, the conditional median or some other quantile is used. Like all forms of regression analysis, linear regression focuses on the conditional probability distribution of the response given the values of the predictors, rather than on the joint probability distribution of all of these variables, which is the domain of multivariate analysis.

## Implementing Linear Regression

We will use ordinary least square method to implement linear regression using python.
Let X be the independent variable and Y be the dependent variable. We will define a linear relationship between these two variables as follows:
<img src="content\basic_formula.png" alt="line-formula">

A loss function in machine learning is simply a measure of how different the predicted values are from the actual values.
Now, to minimize the loss function we use the least squares method. Thus, we can determine the values of slope(m) and intercept(c).
<img src="content\least_square_formula.png" alt="least-squares-formula">

## About the dataset

Our Dataset contains two columns. Suppose one column refers the amount of hours an individual dedicates and the another refers to the marks he obtains from all the hard-work. If we plot a graph between the first and second column, the result of the marked points would be linearly increasing. Thats funny because obviously the more you study the more marks you score. :satisfied:
<img src="content\initial_data.png" alt="data">

## Result

After we calculate the values of the slope and intercept, we would get an output similar to the below image:
<img src="content\final_output.png" alt="output">

## Accuracy

Now, how do we calculate the accuracy of the model we just build? For this, we use Root Mean Squared Error and the Coefficient of Determination(R2 Score).
Root Mean Squared Error is the square root of sum of all errors divided by number of values, or mathematically,
<img src="content\rmse.png" alt="root-mean-squared-error formula">

Now, to calculate R2 score, we follow the below formula,
<img src="content\r2_score.png" alt="r2_score formula">

Here, SSr is the total sum of squares and SSt is the total sum of squares of residuals.
R2 Score usually range from 0 to 1. It will also become negative if the model is completely wrong.

So, the accuracy we get from our approach is:
<img src="content\our_score.png" alt="R2 Score">