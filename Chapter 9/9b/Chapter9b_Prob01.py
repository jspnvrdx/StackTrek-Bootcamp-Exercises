import os
os.system('cls||clear')

#----CODE STARTS HERE------

class Conversations:
      def __init__(self):
            self._messages = dict()

      def add_message(self, message):
            if message.sender_contact_number not in self._messages:
                  self._messages[message.sender_contact_number] = [message.text]
            else:
                  self._messages[message.sender_contact_number].append(message.text)

            

      def display_conversations(self):
            return self._messages

      def search(self, contact_number):
            for key, value in self._messages.items():
                  if key == contact_number:
                        return value
            return list()

class Message:
    def __init__(self, sender_contact_number, text):
          self.sender_contact_number = sender_contact_number
          self.text = text

conversations = Conversations()
# message1 = Message("09273966531", "hello")
# message2 = Message("09273966531", "God Bless!")
# message3 = Message("09090988888", "sorry")
# conversations.add_message(message1)
# conversations.add_message(message2)
# conversations.add_message(message3)
print(conversations.display_conversations())
print(conversations.search("0945635112"))