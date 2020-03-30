
# coding: utf-8

# In[1]:


import numpy as np
import scipy.special #for sigmoid function
import matplotlib.pyplot
# ensure the plots are inside this notebook, not an external window
get_ipython().run_line_magic('matplotlib', 'inline')


# In[68]:ú


#neural network class definition
class neuralNetwork:
    #initialise the neural núetwork
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        #link weight matrices, wih and whoú
        #weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        self.wih = np.random.normal(0.0,pow(self.hnodes, -0.5),(self.hnodes, self.inodes))
        self.who = np.random.normal(0.0,pow(self.onodes, -0.5),(self.onodes, self.hnodes))
        
        #learning rate
        self.lr = learningrate
        
        #activation function is the sigmoid function
        self.activation_function = lambda x:scipy.special.expit(x)
        
        pass
    
    #train the neural network
    def train(self, inputs_list, targets_list):
        #convert input list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        
        #calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        #calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        #calculate the signals into final output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        #calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        
        #output layer error is the (target - actual)
        output_errors = target - final_outputs
        #hidden layer erro is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = np.dot(self.who.T, output_errors)
        
        #update the weights for the links between the hidden and output lauers
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        
        #update the weights  for the link between the input and hidden layers
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs *(1.0 - hidden_outputs)), np.transpose(inputs))
        
        pass        
        
    
    #query the neural network
    def query(self, input_list):
        #convert inputs list to 2d array
        inputs = np.array(input_list, ndmin=2).T
        
        #calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        #calculate signals emerging from hidden layerit
        hidden_outputs = self.activation_function(hidden_inputs)
        
        #calculate signals inte tho final output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        #calculate the signals emerging from final output layer
        final_output = self.activation_function(final_inputs)
        
        return final_output


# In[81]:


#no of input, hidden and output
input_nodes = 24
hidden_nodes = 28
output_nodes = 1

#learning rate is 0.2
learning_rate = 0.2

#create instance of neural network
n = neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)

training_file = open("DATA/carrot_traindata.csv",'r')
training_list = training_file.readlines()
training_file.close

epochs = 12000
for e in range(epochs):
    for record in training_list:
        #train the nn
        all_data = record.split(',')
        target = (np.asfarray(all_data[1:2]) / 255.0 * 0.99) + 0.01     
        inputs = (np.asfarray(all_data[2:]) / 255.0 * 0.99) + 0.01
        n.train(inputs, target)                                                                 
        pass
    pass


# In[75]:


test_data_file = open("DATA/carrot_testdata.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()


# In[76]:


final_error = 0
for record in test_data_list:
    all_values = record.split(',')
    correct_value = (np.asfarray(all_values[1:2]) / 255.0 * 0.99) + 0.01
    inputs = (np.asfarray(all_values[2:]) / 255.0 * 0.99) + 0.01
    output = n.query(inputs)
    print("actual")
    print (all_values[1])
    print("predicted")
    actual_output = (output * (255.0 * 0.99)) - 0.01 
    print(actual_output)
    error = ((correct_value - output) / correct_value) * 100
    final_error = abs(error) + final_error
    


# In[77]:


error = (final_error/6)


# In[78]:


print (error)


# In[79]:


import pickle


# In[80]:


# carrot = {}
# carrot['title'] = 'carrot'
# carrot['hidden and output layers'] = n.who
# carrot['hidden and input layers'] = n.wih

# with open('Pickle/carrot.pickle', 'wb') as f:  
#     pickle.dump(carrot, f) 


# In[62]:




