import numpy as np
from keras.layers import SimpleRNN

inputs = np.random.random([32, 10, 8]).astype(np.float32)
print("Inputs: ")
print(inputs)

simple_rnn = SimpleRNN(4)

output = simple_rnn(inputs)  # The output has shape `[32, 4]`.
print("Output: ")
print(output)

simple_rnn = SimpleRNN(
    4, return_sequences=True, return_state=True)

# whole_sequence_output has shape `[32, 10, 4]`.
# final_state has shape `[32, 4]`.
whole_sequence_output, final_state = simple_rnn(inputs)