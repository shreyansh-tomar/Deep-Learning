## Character Level LSTMs

This notebook is the implementation of character level [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory).The implementation trains neural network character by character on some text which then enables the learned model to predict the next character given the initial character provided.
The implementation is based off of the Andrej Karpathy's blogpost on [Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/).
The Architecture is given as follows:

>  <img src="https://user-images.githubusercontent.com/18248623/74175245-6c3ea080-4c5b-11ea-9d9b-57a558ab411a.jpeg" width="450" height="450"/>
