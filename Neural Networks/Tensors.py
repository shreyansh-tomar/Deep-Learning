#Getting Started with Tensors in Pytorch by building single layered and multilayered Neural Network
import torch

def activation(x):
    return 1/(1 + torch.exp(-x))

### Generate some data
torch.manual_seed(7) # Set the random seed so things are predictable

# Features are 5 random normal variables
features = torch.randn((1, 5))
# True weights for our data, random normal variables again
weights = torch.randn_like(features)
# and a true bias term
bias = torch.randn((1, 1))

##output of this network using the weights and bias tensors
y = activation(torch.sum(features*weights) + bias)
#OR
y = activation((features*weights).sum() + bias)
print(y)

## Calculate the output of this network using matrix multiplication
weights = weights.view(5,1)
y = activation(torch.mm(features, weights) + bias)

print(y)