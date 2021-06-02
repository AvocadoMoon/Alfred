class Node:
    def __init__(self, key_word, command=None, playlist=None, tts=None, keybind=None):
        self.command = command
        self.key_word = key_word
        self.playlist = playlist
        self.tts = tts
        self.keybind = keybind
    
    def __hash__(self):
        return hash(self.key_word)
    
    def items(self):
        return (self.key_word, self.command, self.playlist, self.tts, self.keybind)

class CustomSet:
    def __init__(self, size=10000):
        self._length = 0
        self._bucket_size = size
        self.BucketList = [[] for i in range(self._bucket_size)]
    
    def _double(self):
        oldbuckets = self.BucketList
        self._bucket_size *= 2
        self.BucketList = [[] for i in range(self._bucket_size)]
        for i in oldbuckets:
            for j in i:
                key_word, commmand, playlist, tts, keybind = j.items()
                h = hash(key_word) % self._bucket_size
                self.BucketList[h].append(Node(key_word, commmand, playlist, tts, keybind))

    def add(self, key_word, command=None, playlist=None, tts=None, keybind=None):
        if self._length < self._bucket_size:
            if self.__contains__(key_word):
                return
            else:
                self._length += 1
                j = self.custom_hash(key_word) % self._bucket_size
                self.BucketList[j].append(Node(key_word, command, playlist, tts, keybind))
        else:
            self._double()
            self.add(key_word, command, playlist, tts, keybind)
    
    def remove(self, item):
        if not(self.__contains__(item)):
            raise ValueError
        else:
            self._length -= 1
            j = self.custom_hash(item) % self._bucket_size
            l = self.BucketList[j]
            l.remove(item)

    def __len__(self):
        return self._length
    
    def __contains__(self, item):
        i = self.custom_hash(item) % self._bucket_size
        j = self.BucketList[i]
        for i in j:
            if i.key_word == item:
                return True
            else:
                return False
    
    def get(self, item):
        if self.__contains__(item):
            i = self.custom_hash(item) % self._bucket_size
            return self.BucketList[i][0]
        else:
            return None
    
    def custom_hash(self, key_word):
        total = 0
        if isinstance(key_word, int):
            return hash(key_word)
        for i in key_word:
            total += ord(i)
        return total


if __name__ == "__main__":
    cs = CustomSet()
    for i in range(10):
        cs.add(i, str(i), i)
    
    for i in range(10):
        assert(cs.get(i).command == str(i))
        assert(cs.get(i).playlist == i)
    cs = CustomSet()

    for i in range(10):
        cs.add(i)
        assert(cs.get(i).key_word == i)
        assert(cs.get(i).command == None)
    
    cs = CustomSet()

    for i in range(100):
        cs.add(i, str(i), -i, i, str(i))
        assert(cs.get(i).key_word == i)
        assert(cs.get(i).command == str(i))
        assert(cs.get(i).playlist == -i)
        assert(cs.get(i).tts == i)
        assert(cs.get(i).keybind == str(i))