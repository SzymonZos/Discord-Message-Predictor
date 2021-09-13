import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing
from utils import deserialize

_model = tf.keras.models.load_model("./models/prototype")
_vocab = deserialize("./models/vocab.pickle")
_ids_from_chars = preprocessing.StringLookup(vocabulary=_vocab)
_chars_from_ids = preprocessing.StringLookup(
    vocabulary=_ids_from_chars.get_vocabulary(), invert=True)


class OneStep(tf.keras.Model):
    def __init__(self, model=_model, chars_from_ids=_chars_from_ids,
                 ids_from_chars=_ids_from_chars, temperature=1.0):
        super().__init__()
        self.temperature = temperature
        self.model = model
        self.chars_from_ids = chars_from_ids
        self.ids_from_chars = ids_from_chars

    @tf.function
    def generate_one_step(self, inputs, states=None):
        input_chars = tf.strings.unicode_split(inputs, 'UTF-8')
        input_ids = self.ids_from_chars(input_chars).to_tensor()

        predicted_logits, states = self.model(inputs=input_ids, states=states,
                                              return_state=True)
        predicted_logits = predicted_logits[:, -1, :]
        predicted_logits = predicted_logits / self.temperature

        predicted_ids = tf.random.categorical(predicted_logits, num_samples=1)
        predicted_ids = tf.squeeze(predicted_ids, axis=-1)

        predicted_chars = self.chars_from_ids(predicted_ids)
        return predicted_chars, states
