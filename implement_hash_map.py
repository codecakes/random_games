## for learning purpose only

from collections import deque

##The making of a hash Table
def hash_string(keyword,buckets):
    '''
    # takes as inputs a keyword
    # (string) and a number of buckets,
    # and returns a number representing
    # the bucket for that keyword.
    '''
    return sum(map(ord, keyword))%buckets

##Testing Hash string distribution using hash str function
def test_hash_func(fn, keys, bucSize):
    results = [0] * bucSize
    keys_used = set()
    for key in keys:
        if key and key not in keys_used:
            results[fn(key, bucSize)] += 1
            keys_used.add(key)
    return results


## Implementing a HashTable
## create buckets
create_table = lambda size: [[] for _ in xrange(size)]

##finding buckets
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

##adding to buckets
def hashtable_add(htable,key,value):
    # your code here
    pos = hash_string(key,len(htable))
    #O(k/bsize)
    for each in htable[pos]:
        if each[0] == key: break
    else:
        htable[pos].append([key, value])
    return htable

##look up value of a key
def hashtable_lookup(htable,key):
    pos = hash_string(key,len(htable))
    for each in htable[pos]:
        if each[0] == key: return each[1]
    return None

##Update a key if present else add it
def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            break
    else:
        hashtable_add(htable,key,value)
    return htable
        
class hashmap(object):
    
    def __init__(self, bsize=0):
        self.bsize = bsize or 20
        self.table = create_table(self.bsize)
        self.keyCount = 0
    
    def __str__(self):
        return self.table
    
    def __repr__(self):
        return "{}".format(self.__str__())
    
    def __len__(self): return len(self.table)
    
    def _getBucket(self, key):
        return hashtable_get_bucket(self.table, key)
    
    def _expandTable(self):
        self.bsize *= 2
        newtable = create_table(self.bsize)
        #print "new table %s" %newtable
        q = deque(maxlen=self.bsize)
        q.appendleft(self.table)
        #O(nlogn)
        while q:
            tbl = q.pop()
            ln = len(tbl)
            if ln > 1:
                q.appendleft(tbl[:ln//2])
                q.appendleft(tbl[ln//2:])
            else:
                #print "_expandTable else tbl is {}".format(tbl)
                for each_buck in tbl:
                    for each_key_list in each_buck:
                        if each_key_list:
                            #print "each key list is {}".format(each_key_list)
                            #print "_expandTable adding key {} val {}".format(each_key_list[0], each_key_list[1])
                            hashtable_add(newtable, each_key_list[0], each_key_list[1])
        assert len(self.table) < len(newtable)
        del self.table
        self.table = newtable
        return self.table
    
    def _addKey(self, key, value):
        if self.keyCount+1 > self.bsize:
            self._expandTable()
        
        bucket = self._getBucket(key)
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                break
        else:
            hashtable_add(self.table, key,value)
            self.keyCount += 1
    
    def _getVal(self, key): 
        return hashtable_lookup(self.table, key)
    
    def __getitem__(self, key):
        return self._getVal(key)
    
    def __setitem__(self, key, value):
        self._addKey(key, value)
    
    ##Delete a key if present else ignore
    def _hashtable_delete(self, key):
        bucket = hashtable_get_bucket(self.table, key)
        for entry in bucket:
            if entry[0]==key: 
                bucket.remove(entry)
                self.keyCount -= 1
    
    def remove(self, key):
        self._hashtable_delete(key)
    
    

if __name__ == "__main__":     
    table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
    ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]
    
    assert hashtable_get_bucket(table, "Zoe") == [['Bill', 17], ['Zoe', 14]]
    
    assert hashtable_get_bucket(table, "Brick") == []
    
    assert hashtable_get_bucket(table, "Lilith") == [['Louis', 29], ['Rochelle', 4], ['Nick', 2]] 

    table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
    [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
    
    hashtable_update(table, 'Bill', 42)
    hashtable_update(table, 'Rochelle', 94)
    hashtable_update(table, 'Zed', 68)
    assert table == [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], \
    [['Bill', 42], ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], \
    ['Nick', 2], ['Rochelle', 94]]]
    
    #d for dict
    d = hashmap(4)
    
    d['fdfds'] = 32423324
    
    d['fdfsfdsds'] = 32423324
    
    d['fdfsfdsdssdfsd'] = 32423324
    
    d['fdffsd'] = 32423324
    
    d['ffsd'] = 32423324
    d.remove('ffsd')
    
    assert d == [[], [], [], [['fdfsfdsdssdfsd', 32423324]], [], \
    [['fdffsd', 32423324]], [], [['fdfds', 32423324], ['fdfsfdsds', 32423324]]]
